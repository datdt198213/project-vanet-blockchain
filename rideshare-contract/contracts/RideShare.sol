// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.24;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Rideshare {
    IERC20 public token;  // Địa chỉ của hợp đồng token ERC20

    constructor(address _tokenAddress) {
        token = IERC20(_tokenAddress);
    }

    struct Coordinate {
        uint256 latitude;
        uint256 longitude; 
    }

    struct RideRequest {
        address passenger;
        uint256 drivingCost;
        uint64 capacity;
        string origin;
        string destination;
        bool isAccepted;
        bool isConfirmed;
        address driver;
        bool isCompletedByDriver;
        bool isConfirmedByPassenger;
        Coordinate[] coordinates;
    }
    
    mapping(address => RideRequest) public rideRequests;

    event RideRequested(address indexed passenger, string origin, string destination, uint64 capacity);
    event RideAccepted(address indexed passenger, address indexed driver, uint256 drivingCost);
    event RideConfirmed(address indexed passenger, address indexed driver, uint256 drivingCost);
    event RideCompletedByDriver(address indexed passenger, address indexed driver);
    event RideConfirmedByPassenger(address indexed passenger, address indexed driver, uint256 drivingCost);
    event RideCoordinatesSubmitted(address indexed driver, address indexed passenger, Coordinate[] coordinates); 

    function requestRide(string memory _origin, string memory _destination, uint64 _capacity) public {
        require(!rideRequests[msg.sender].isAccepted, "You already have a pending ride request.");

        rideRequests[msg.sender].passenger = msg.sender;
        rideRequests[msg.sender].drivingCost = 0;
        rideRequests[msg.sender].capacity = _capacity;
        rideRequests[msg.sender].origin = _origin;
        rideRequests[msg.sender].destination = _destination;
        rideRequests[msg.sender].driver = address(0);
        rideRequests[msg.sender].isAccepted = false;
        rideRequests[msg.sender].isConfirmed = false;
        rideRequests[msg.sender].isCompletedByDriver = false;
        rideRequests[msg.sender].isConfirmedByPassenger = false;

        emit RideRequested(msg.sender, _origin, _destination, _capacity);
    }

    function acceptRide(address _passenger, uint256 _drivingCost) public {
        require(rideRequests[_passenger].passenger == _passenger, "Ride request does not exist.");
        require(!rideRequests[_passenger].isAccepted, "Ride request has already been accepted.");

        uint256 allowance = token.allowance(msg.sender, address(this));
        require(allowance >= _drivingCost, "Check the token allowance.");
        require(token.balanceOf(msg.sender) >= _drivingCost, "Insufficient balance.");
        require(token.transferFrom(msg.sender, address(this), _drivingCost), "Token transfer failed.");

        // Cập nhật thông tin yêu cầu đi xe
        rideRequests[_passenger].drivingCost = _drivingCost;
        rideRequests[_passenger].isAccepted = true;
        rideRequests[_passenger].driver = msg.sender;

        emit RideAccepted(_passenger, msg.sender, _drivingCost);
    }

    function confirmRide() public {
        require(rideRequests[msg.sender].passenger == msg.sender, "Ride request does not exist.");
        require(!rideRequests[msg.sender].isConfirmed, "Ride request has already been confirmed.");

        uint256 _drivingCost = rideRequests[msg.sender].drivingCost;
        require(token.transferFrom(msg.sender, address(this), _drivingCost), "Token transfer failed.");
        address _driver = rideRequests[msg.sender].driver;
        rideRequests[msg.sender].isConfirmed = true;

        emit RideConfirmed(msg.sender, _driver, _drivingCost);
    }

    function completeRide(address _passenger) public {
        RideRequest storage request = rideRequests[_passenger];
        require(request.isAccepted, "Ride request is not accepted.");
        require(request.isConfirmed, "Ride request is not confirmed.");
        require(request.driver == msg.sender, "Only the driver can complete the ride.");

        // Đánh dấu chuyến đi là đã hoàn thành bởi tài xế
        request.isCompletedByDriver = true;

        emit RideCompletedByDriver(_passenger, msg.sender);
    }

    function confirmRideCompletion() public {
        RideRequest storage request = rideRequests[msg.sender];
        require(request.passenger == msg.sender, "Only the passenger can confirm the ride completion.");
        require(request.isCompletedByDriver, "Ride has not been marked as completed by the driver.");
        require(!request.isConfirmedByPassenger, "Ride has already been confirmed by the passenger.");

        // Đánh dấu chuyến đi là đã xác nhận bởi hành khách
        request.isConfirmedByPassenger = true;

        uint256 drivingCost = request.drivingCost;
        address driver = request.driver;

        // Chuyển token từ hợp đồng đến tài xế
        require(token.transfer(driver, drivingCost + drivingCost), "Token transfer to driver failed.");

        emit RideConfirmedByPassenger(msg.sender, driver, drivingCost);
    }

    function submitRideCoordinates(address _passenger, Coordinate[] memory _coordinates) public {
        RideRequest storage request = rideRequests[_passenger];
        require(request.driver == msg.sender, "Only the driver can submit ride coordinates.");
        require(request.isConfirmedByPassenger, "Ride must be marked as completed by the passenger first.");

        // Lưu trữ tọa độ của chuyến đi
        for (uint i = 0; i < _coordinates.length; i++) {
            request.coordinates.push(_coordinates[i]);
        }

        // Đặt lại yêu cầu đi xe
        delete rideRequests[_passenger];

        emit RideCoordinatesSubmitted(msg.sender, _passenger, _coordinates);
    }

    function getRideStatus(address _passenger) public view returns (uint256, uint64, string memory, string memory, bool, address, bool, bool) {
        RideRequest memory request = rideRequests[_passenger];
        return (
            request.drivingCost,
            request.capacity,
            request.origin,
            request.destination,
            request.isAccepted,
            request.driver,
            request.isCompletedByDriver,
            request.isConfirmedByPassenger
        );
    }

    function getRideCoordinates(address _passenger) public view returns (Coordinate[] memory) {
        RideRequest memory request = rideRequests[_passenger];
        return request.coordinates;
    }
}