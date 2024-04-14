const RideShare = artifacts.require("RideShare");

contract("RideShare", (accounts) => {
  let rideShareInstance;

  beforeEach(async () => {
    rideShareInstance = await RideShare.new({ from: accounts[0] });
  });

  it.skip("Test 1: add a passenger", async () => {
    const passengerName = "Alice";
    const passengerPhoneNumber = "1234567890";
    const numberOfPeople = 2;
    const state = "initial";

    await rideShareInstance.addPassenger(
      passengerName,
      passengerPhoneNumber,
      numberOfPeople,
      state,
      { from: accounts[0] }
    );

    const passenger = await rideShareInstance.passengers(accounts[0], 0);
    assert.equal(passenger.id, 0, "Id was not equal")
    assert.equal(passenger.name, passengerName, "Name was not equal");
    assert.equal(passenger.phoneNumber, passengerPhoneNumber, "phone number was not equal");
    assert.equal(passenger.numberOfPeople, numberOfPeople, "Number of people was not equal");
    assert.equal(passenger.state, state, "State was not equal");
  });

  it.skip("Test 2: create a new ride", async () => {
    const drivingCost = web3.utils.toWei("1", "ether");
    const capacity = 4;
    const confirmedAt = Math.floor(Date.now() / 1000);
    const originAddress = "Ha Noi";
    const destAddress = "Hai Phong";

    await rideShareInstance.createRide(
      drivingCost,
      capacity,
      confirmedAt,
      originAddress,
      destAddress,
      { from: accounts[0], value: drivingCost }
    );

    const ride = await rideShareInstance.rides(0);
    assert.equal(ride.drivingCost, drivingCost, "Cost is not equal");
    assert.equal(ride.capacity, capacity, "Capacity is not equal");
    assert.equal(ride.confirmedAt, confirmedAt, "Confirmed at is not equal");
    assert.equal(ride.originAddress, originAddress, "Origin address is not equal");
    assert.equal(ride.destAddress, destAddress, "Origin address is not equal");
  });

  it.skip("Test 3: Create ride and join a ride", async () => {
    // Create a ride
    const drivingCost = web3.utils.toWei("1", "ether");
    const capacity = 4;
    const confirmedAt = Math.floor(Date.now() / 1000);
    const originAddress = "Ha Noi";
    const destAddress = "Quang Ninh";

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
    // console.log(passengerAccounts)
    assert.equal(passengerAccounts.length, 1);
  });

  it.skip("Test 4: Create ride and join a ride", async () => {
    // Create a ride
    const drivingCost = web3.utils.toWei("1", "ether");
    const capacity = 4;
    const confirmedAt = Math.floor(Date.now() / 1000);
    const originAddress = "Ha Noi";
    const destAddress = "Quang Ninh";

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
      from: accounts[0],
      value: drivingCost,
    });

    const passengerAccounts = await rideShareInstance.retrieveAllPassengers(0);
    // console.log(passengerAccounts)
    assert.equal(passengerAccounts.length, 1);
  });

  it.skip("Test 5: Create ride and join a ride", async () => {
    // Create a ride
    const drivingCost = web3.utils.toWei("1", "ether");
    const capacity = 4;
    const confirmedAt = Math.floor(Date.now() / 1000);
    const originAddress = "Ha Noi";
    const destAddress = "Quang Ninh";

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

    await rideShareInstance.joinRide(0, {
      from: accounts[2],
      value: drivingCost,
    });

    const passengerAccounts = await rideShareInstance.retrieveAllPassengers(0);
    // console.log(passengerAccounts)
    assert.equal(passengerAccounts.length, 2, "Adding fail");
    assert.equal(passengerAccounts[0], accounts[1], "Account 1 was not participate in the ride" );
    assert.equal(passengerAccounts[1], accounts[2], "Account 2 was not participate in the ride" );
  });

  it.skip("Test 6: AddPassenger, CreateRide, JoinRide and ConfirmDriverMet", async () => {
    // Create a ride
    const drivingCost = web3.utils.toWei("1", "ether");
    const capacity = 4;
    const confirmedAt = Math.floor(Date.now() / 1000);
    const originAddress = "Ha Noi";
    const destAddress = "Quang Ninh";

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

    await rideShareInstance.confirmDriverMet(0, {from: accounts[0]})
    
    const rides = await rideShareInstance.rides(0);
    const passenger = await rideShareInstance.passengers(accounts[1], 0);

    assert.equal(passenger.state, "confirm", "State is not confirm")
    // console.log(passenger)
  });

  it.skip("Test 7: AddPassenger, CreateRide, JoinRide, ConfirmDriverMet and Arrived", async () => {
    // Create a ride
    const drivingCost = web3.utils.toWei("1", "ether");
    const capacity = 4;
    const confirmedAt = Math.floor(Date.now() / 1000);
    const originAddress = "Ha Noi";
    const destAddress = "Quang Ninh";

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

    await rideShareInstance.joinRide(0, {
      from: accounts[2],
      value: drivingCost,
    });

    await rideShareInstance.confirmDriverMet(0, {from: accounts[0]})

    await rideShareInstance.arrived(0, {from: accounts[0]})
    
    const rides = await rideShareInstance.rides(0);
    const passenger1 = await rideShareInstance.passengers(accounts[1], 0);
    const passenger2 = await rideShareInstance.passengers(accounts[2], 0);

    assert.equal(passenger1.state, "completion", "State is not completion")
    assert.equal(passenger2.state, "completion", "State is not completion")

    // console.log(rides)
  });

  it.skip("Test 8: AddPassenger, CreateRide, JoinRide, ConfirmDriverMet and Cancel from Driver", async () => {
    // Create a ride
    const drivingCost = web3.utils.toWei("1", "ether");
    const capacity = 4;
    const confirmedAt = Math.floor(Date.now() / 1000);
    const originAddress = "Ha Noi";
    const destAddress = "Quang Ninh";

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

    await rideShareInstance.joinRide(0, {
      from: accounts[2],
      value: drivingCost,
    });

    await rideShareInstance.confirmDriverMet(0, {from: accounts[0]})

    await rideShareInstance.cancel(0, {from: accounts[0]})
    
    const rides = await rideShareInstance.rides(0);
    const passenger1 = await rideShareInstance.passengers(accounts[1], 0);
    const passenger2 = await rideShareInstance.passengers(accounts[2], 0);

    assert.equal(passenger1.state, "Cancel from driver", "State is not cancel from driver")
    assert.equal(passenger2.state, "Cancel from driver", "State is not cancel from driver")

    // console.log(rides)
  });

  it.skip("Test 9: AddPassenger, CreateRide, JoinRide, ConfirmDriverMet and Cancel from Passenger", async () => {
    // Create a ride
    const drivingCost = web3.utils.toWei("1", "ether");
    const capacity = 4;
    const confirmedAt = Math.floor(Date.now() / 1000);
    const originAddress = "Ha Noi";
    const destAddress = "Quang Ninh";

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

    await rideShareInstance.confirmDriverMet(0, {from: accounts[0]})

    await rideShareInstance.cancel(0, {from: accounts[1]})
    
    const rides = await rideShareInstance.rides(0);
    const p = await rideShareInstance.passengers(accounts[1], 0);

    assert.equal(p.state, "Cancel from passenger", "State is not cancel from passenger")
  });

  it.skip("Test 10: AddPassenger, CreateRide, JoinRide, ConfirmDriverMet and Cancel from Passenger", async () => {
    // Create a ride
    const drivingCost = web3.utils.toWei("1", "ether");
    const capacity = 4;
    const confirmedAt = Math.floor(Date.now() / 1000);
    const originAddress = "Ha Noi";
    const destAddress = "Quang Ninh";

    const passengerName = "Alice";
    const passengerPhoneNumber = "1234567890";
    const numberOfPeople = 2;
    const state = "initial";

    const passengerName1 = "Bob";
    const passengerPhoneNumber1 = "0348237932";
    const numberOfPeople1 = 1;
    const state1 = "initial";

    await rideShareInstance.addPassenger(
      passengerName,
      passengerPhoneNumber,
      numberOfPeople,
      state,
      { from: accounts[1] }
    );

    await rideShareInstance.addPassenger(
      passengerName1,
      passengerPhoneNumber1,
      numberOfPeople1,
      state1,
      { from: accounts[2] }
    );

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

    await rideShareInstance.joinRide(0, {
      from: accounts[2],
      value: drivingCost,
    });

    await rideShareInstance.confirmDriverMet(0, {from: accounts[0]})

    await rideShareInstance.cancel(0, {from: accounts[1]})
    await rideShareInstance.arrived(0, {from: accounts[0]})
    
    const rides = await rideShareInstance.rides(0);
    const p = await rideShareInstance.passengers(accounts[1], 0);

    assert.equal(p.state, "Cancel from passenger", "State is not cancel from passenger")
  });
  // Add more test cases for other functions as needed
});
