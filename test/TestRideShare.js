const RideShare = artifacts.require("RideShare");

contract("RideShare", (accounts) => {
  let rideShareInstance;

  beforeEach(async () => {
    rideShareInstance = await RideShare.new({ from: accounts[0] });
  });

  it("should add a passenger", async () => {
    const passengerName = "Alice";
    const passengerPhoneNumber = "1234567890";
    const numberOfPeople = 2;
    const state = "initial";

    await rideShareInstance.addPassenger(
      passengerName,
      passengerPhoneNumber,
      numberOfPeople,
      state,
      { from: accounts[1] }
    );

    const passenger = await rideShareInstance.passengers(accounts[1], 0);
    assert.equal(passenger.name, passengerName);
  });

  it("should create a new ride", async () => {
    const drivingCost = web3.utils.toWei("1", "ether");
    const capacity = 4;
    const confirmedAt = Math.floor(Date.now() / 1000);
    const originAddress = "Origin";
    const destAddress = "Destination";

    await rideShareInstance.createRide(
      drivingCost,
      capacity,
      confirmedAt,
      originAddress,
      destAddress,
      { from: accounts[0], value: drivingCost }
    );

    const ride = await rideShareInstance.rides(0);
    assert.equal(ride.originAddress, originAddress);
  });

  it("should allow a passenger to join a ride", async () => {
    // Create a ride
    const drivingCost = web3.utils.toWei("1", "ether");
    const capacity = 4;
    const confirmedAt = Math.floor(Date.now() / 1000);
    const originAddress = "Origin";
    const destAddress = "Destination";

    await rideShareInstance.createRide(
      drivingCost,
      capacity,
      confirmedAt,
      originAddress,
      destAddress,
      { from: accounts[0], value: drivingCost }
    );

    // Passenger joins the ride
    await rideShareInstance.joinRide(0, {
      from: accounts[1],
      value: drivingCost,
    });

    const passengerAccounts = await rideShareInstance.retrieveAllPassengers(0);
    assert.equal(passengerAccounts.length, 1);
  });

  // Add more test cases for other functions as needed
  
});
