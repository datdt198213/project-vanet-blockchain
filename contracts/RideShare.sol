// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract RideShare {

    struct Passenger {
        uint id;
        string name;
        string phoneNumber;
        uint256 numberOfPeople;
        string state;
    }
    
    mapping(address => mapping(uint => Passenger)) public passengers;
    mapping(address => uint) public passengerCounter;

    struct Ride {
        uint id;
        address driver;
        uint256 drivingCost;
        uint256 capacity;
        uint256 confirmedAt;
        string originAddress;
        string desAddress;
        address payable[] passengerAccounts;
    }

    Ride[] public rides;
    uint256 public rideCounter;

    uint256 public startTime; 
    uint256 public endTime; 
    uint256 public limitTime = 3;

    function addPassenger(
        string memory _name,
        string memory _phoneNumber,
        uint256 _numberOfPeople,
        string memory _state
    ) public {
        // emit LogPassenger(_name, _phoneNumber, _numberOfPeople, _state);
        uint psgCount = passengerCounter[msg.sender];

        Passenger memory newPassenger = Passenger({
            id: psgCount,
            name: _name,
            phoneNumber: _phoneNumber,
            numberOfPeople: _numberOfPeople,
            state: _state
        });

        passengers[msg.sender][psgCount] = newPassenger;

        // emit PassengerAdded(psgCount, _name, _phoneNumber, _numberOfPeople, _state);
        passengerCounter[msg.sender]++;
    }


    // Function to create a new ride
    function createRide (
        uint256 _drivingCost,
        uint256 _capacity,
        uint256 _confirmedAt,
        string memory _originAddress,
        string memory _destAddress
    ) public payable{
        Ride memory newRide = Ride({
            id: rideCounter,
            driver: msg.sender,
            drivingCost: _drivingCost,
            capacity: _capacity,
            confirmedAt: _confirmedAt,
            originAddress: _originAddress,
            desAddress: _destAddress,
            passengerAccounts: new address payable[](0)
        });

        require(uint256(msg.value) == uint256(_drivingCost), "Create: Not enough ether!");

        startTime = block.timestamp;
        rides.push(newRide);
        rideCounter++;
    }

    function retrieveRide(uint _index) view  public returns (Ride memory) {
        return rides[_index];
    }

    function retrieveAllPassengers(uint256 _idxRide) public view returns  (address payable[]  memory) {
        return rides[_idxRide].passengerAccounts;
    }
   
    // Lấy ra địa chỉ của khách hàng tham gia vào chuyến đi thứ index
    function retrieveOnePassenger(uint256 _idxRide) public view returns (address) {
        address pAddress;
        for (uint256 i = 0; i < rides[_idxRide].passengerAccounts.length; i++) {
            // Kiểm tra thằng sender (thằng gửi đồng ý tham gia transaction) có trong chuyến đi hay không
            if (msg.sender == rides[_idxRide].passengerAccounts[i]){
                pAddress = rides[_idxRide].passengerAccounts[i];
                break;
            }
        }
        
        require(pAddress != address(0), "Retrieve One Passenger: This account does not participate in the ride");
        return pAddress;
    }

    // 1. Khách hàng xác nhận tham gia vào transaction (đặt xe) - Khách hàng (làm hành động gì đó trên giao diện)
    function joinRide(uint256 _idxRide) public payable{
        require(msg.sender != rides[_idxRide].driver, "Join Ride: This is driver address, the ride need a passenger join");

        // Đơn vị được sử dụng ở đây là wei 
        require(uint256(msg.value) == uint256(rides[_idxRide].drivingCost), "Join Ride: Not enough ether!");
        rides[_idxRide].passengerAccounts.push(payable(msg.sender));

        // 2. Cập nhật trạng thái của khách hàng khi mới tham gia vào mạng (Sau khi joinRide) - Hệ thống
        passengers[msg.sender][_idxRide].state = "initial";
    }

    // 3. Cập nhật trạng thái của khách hàng khi được chấp nhận chuyến đi của tài xế - Tài xế  (làm hành động gì đó trên giao diện)
    function confirmDriverMet(uint256 _idxRide) public {
        address pAddress = retrieveOnePassenger(_idxRide);
        passengers[pAddress][_idxRide].state = "confirm";
    }

    // 4. Khi kết thúc chuyến đi, tài xế sẽ thực hiện lấy tiền của hành khách
    function arrived(uint256 _idxRide) public {
        require(
            msg.sender == rides[_idxRide].driver,
            "Only driver of the ride can call this function"
        );
        
        (bool callSuccess, ) = payable(msg.sender).call{value: address(this).balance}("");
        require(callSuccess, "Withdraw coin in the contract failed");

        address payable[] memory allPassenger = retrieveAllPassengers(_idxRide);
        for (uint256 i = 0; i < allPassenger.length; i++) {
            // Convert address payable to address
            address pAddress = address(allPassenger[i]);
            passengers[pAddress][_idxRide].state = "completion";

            rides[_idxRide].passengerAccounts[i] = rides[_idxRide].passengerAccounts[allPassenger.length - 1];
            rides[_idxRide].passengerAccounts.pop();
        }
    }

    event TransferReceived(address _from, uint _amout);

    // 5. Khi 1 trong 2 bên hủy chuyến đi 
    function cancel(uint256 _idxRide) public payable {
        address payable[] memory allPassenger = retrieveAllPassengers(_idxRide);
        uint256 length = allPassenger.length;

        // Khi transaction quá thời gian, coin được trả về cho tài xế         

        // Khi tài xế hủy
        if(msg.sender == rides[_idxRide].driver) {  
            uint256 share = msg.value / allPassenger.length;
            for (uint256 i = 0; i < length; i++) {
                // Convert address payable to address
                address pAddress = address(allPassenger[i]);
                (bool callSuccess, ) = payable(pAddress).call{value: share}("");
                require(callSuccess, "Cancel: Transfer coin from driver to passenger failed");

                // Xóa phần tử ra khỏi mảng các chuyến đi rides 
                rides[_idxRide].passengerAccounts[i] = rides[_idxRide].passengerAccounts[length - 1];
                rides[_idxRide].passengerAccounts.pop();
            }
            emit TransferReceived(msg.sender, msg.value);
        } 
        else // khi khách hàng hủy
        {               
            for (uint256 i = 0; i < length; i++) {
                // Convert address payable to address
                address pAddress = address(allPassenger[i]);
                if(msg.sender == pAddress) {
                    (bool callSuccess, ) = payable(msg.sender).call{value: rides[_idxRide].drivingCost}("");
                    require(callSuccess, "Cancel: Transfer coin from passenger to driver failed");

                    // Xóa phần tử ra khỏi mảng các chuyến đi rides 
                    rides[_idxRide].passengerAccounts[i] = rides[_idxRide].passengerAccounts[length - 1];
                    rides[_idxRide].passengerAccounts.pop();
                }
                emit TransferReceived(msg.sender, msg.value);
            }
        } 

    }

}