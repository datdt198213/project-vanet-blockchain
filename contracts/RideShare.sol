// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract RideShare {
    // state variable
    struct Passenger {
        uint256 price;
        string state;
    }

    // state variable
    struct Ride {
        address driver;
        uint256 drivingCost;
        uint256 capacity;
        uint256 confirmedAt;
        string originAddress;
        string desAddress;
        address payable[] passengerAccts;
    }

    mapping(address => uint256) addressToIndexPassengerAccts;
    mapping(address => Passenger) passengers;

    uint256 public passengerAcctsCount;

    Ride[] public rides;
    uint256 public rideCount;

    // Function to create a new ride
    function createRide(
        address _driver,
        uint256 _drivingCost,
        uint256 _capacity,
        uint256 _confirmedAt,
        string memory _originAddress,
        string memory _destAddress
    ) public virtual {
        Ride memory newRide = Ride({
            driver: _driver,
            drivingCost: _drivingCost,
            capacity: _capacity,
            confirmedAt: _confirmedAt,
            originAddress: _originAddress,
            desAddress: _destAddress,
            passengerAccts: new address payable[](0)
        });
        rides.push(newRide);
        rideCount++;
    }

    // Function to create a new passenger
    function addPassenger(uint256 _price, string memory _state) public {
        Passenger memory newPassenger = Passenger({
            price: _price,
            state: _state
        });
        passengers[msg.sender] = newPassenger;
    }

    function retrievePassenger() public view returns (Passenger memory) {
        return passengers[msg.sender];
    }

    function retrieveRide(uint256 _rideIndex) public view returns (Ride memory) {
        return rides[_rideIndex];
    }

    // Function to check a legal transaction for joining a ride
    function joinRide(uint256 _rideIndex) public payable {
        Ride storage curRide = rides[_rideIndex];

        require(
            curRide.passengerAccts.length < curRide.capacity,
            "Ride is already full!"
        );
        require(
            passengers[msg.sender].price == 0,
            "You have already joined this ride"
        );
        require(
            msg.value == curRide.drivingCost,
            "Insufficient payment for joining the ride"
        );

        // Add new passenger into passenger list
        addPassenger(msg.value, "initial");

        // Add passenger address to passenger account list
        curRide.passengerAccts.push(payable(msg.sender));

        // In case number of passenger account in a ride larger than capacity
        if (passengerAcctsCount > curRide.capacity) passengerAcctsCount = 0;

        // Store current address with index of array passenger account to access
        addressToIndexPassengerAccts[msg.sender] = passengerAcctsCount;
        passengerAcctsCount++;
    }

    // Function to confirm Driver and Passenger have met
    function confirmDriverMet(uint256 _rideIndex) public {
        Ride storage curRide = rides[_rideIndex];

        uint256 curIndexPassengerAccts = addressToIndexPassengerAccts[
            msg.sender
        ];
        address payable addressPassengerAcct = curRide.passengerAccts[
            curIndexPassengerAccts
        ];
        Passenger storage passenger = passengers[addressPassengerAcct];

        require(
            bytes(passenger.state).length != 0,
            "You haven't joined this ride"
        );
        passenger.state = "driverConfirmed";
    }

    // Function to payment from passenger to driver when complete the trip
    function arrived(uint256 _rideIndex) public {
        Ride storage curRide = rides[_rideIndex];
        require(
            msg.sender == curRide.driver,
            "Only driver of the ride can call this function"
        );
        uint256 totalPayment = 0;
        for (uint256 i = 0; i < curRide.passengerAccts.length; i++) {
            address payable addressPassengerAcct = curRide.passengerAccts[i];
            Passenger storage passenger = passengers[addressPassengerAcct];
            // Check if state is driverConfirmed and not empty
            if (
                bytes(passenger.state).length != 0 &&
                bytes(passenger.state)[0] == "d"
            ) {
                totalPayment += passenger.price;
                passenger.state = "completion";
            }
        }
        // The address needs to be address payable to be used for transfer
        payable(curRide.driver).transfer(totalPayment);
    }

    //
    function cancelRide(uint256 _rideIndex) public {
        Ride storage curRide = rides[_rideIndex];
        require(
            block.timestamp <= curRide.confirmedAt,
            "Ride has already been confirmed"
        );
        if (msg.sender == curRide.driver) {
            curRide.passengerAccts[0].transfer(curRide.drivingCost);
        } else {
            Passenger storage passenger = passengers[msg.sender];
            require(
                bytes(passenger.state).length != 0,
                "You haven't joined this ride"
            );
            payable(msg.sender).transfer(passenger.price);
        }
    }
}