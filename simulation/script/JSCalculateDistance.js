// Add header
const params = require("process");
const numVehicles = parseFloat(params.argv[2]);
const fs = require("fs");
const fName = "../data/data_distance_" + numVehicles.toString() + ".csv";
const header = [
  "Timeslot",
  "Begin",
  "End",
  "ID",
  "Distance",
];
var stream = fs.createWriteStream(fName, { flags: "a" });
stream.once("open", function (fd) {
  stream.write(header + "\r\n");
});

const crypto = require("crypto");
const JSONStream = require("JSONStream");
const filename = "../sumo/vehicle" + numVehicles.toString() + ".json";
const readStream = fs.createReadStream(filename);
const parser = JSONStream.parse("*");
readStream.pipe(parser);

// Define driver class
class Driver {
  constructor(id, distance, time, coin) {
    this.id = id;
    this.distance = Number(distance);
    this.time = Number(time);
    this.coin = Number(coin);
  }

  display() {
    console.log(
      "id: " +
        this.id +
        ", Distance: " +
        this.distance +
        ", Time: " +
        this.time +
        " , Coin: " +
        this.coin
    );
  }
}

// Define vehicle class
class Vehicle {
  constructor(vehicle, time) {
    this.id = vehicle.id;
    this.x = vehicle.x;
    this.y = vehicle.y;
    this.angle = vehicle.angle;
    this.type = vehicle.type;
    this.speed = vehicle.speed;
    this.pos = vehicle.pos;
    this.lane = vehicle.lane;
    this.slope = vehicle.slope;
    this.time = Number(time);
  }
}

// Hash string by sha512
function sha512(inputString) {
  return crypto.createHash("sha512").update(inputString).digest("hex");
}

// Get data from json and return list of vehicle in a period of time
function getDataFromJson(begin, end, data) {
  dataList = [];
  data.timestep.forEach((element) => {
    time = Number(element.time);
    if (time >= begin && time <= end) {
      if (element.vehicle != undefined) {
        if (element.vehicle.length == undefined) {
          dataList.push(new Vehicle(element.vehicle, element.time));
        } else {
          element.vehicle.forEach((v) => {
            dataList.push(new Vehicle(v, element.time));
          });
        }
      }
    }
  });
  return dataList;
}

// Classify data of a node, return new array is classified
function classifyList(drivers) {
  newDrivers = [];

  check = [];

  for (let i = 0; i < drivers.length; i++) {
    check.push(false);
  }

  for (let i = 0; i < drivers.length; i++) {
    list = [];
    if (check[i] == false) {
      list.push(drivers[i]);
      check[i] = true;
      for (let j = i + 1; j < drivers.length; j++) {
        if (drivers[i].id === drivers[j].id && check[j] == false) {
          list.push(drivers[j]);
          check[j] = true;
        }
      }
      list.forEach((l) => newDrivers.push(l));
    }
  }

  return newDrivers;
}

// calculate distance by haversine formal (miles)
function haversine(lat1, lon1, lat2, lon2) {
  const R = 6371; // Radius of the Earth in kilometers
  const dLat = (lat2 - lat1) * (Math.PI / 180);
  const dLon = (lon2 - lon1) * (Math.PI / 180);

  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(lat1 * (Math.PI / 180)) *
      Math.cos(lat2 * (Math.PI / 180)) *
      Math.sin(dLon / 2) *
      Math.sin(dLon / 2);

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

  var distance = R * c; // The distance in kilometers
  distance *= 1000; // km => m
  return distance;
}

function calculateDistances(vehicles, end) {
  let drivers = [];
  let d = 0;

  for (let idx = 1; idx < vehicles.length; idx++) {
    if (vehicles[idx].id === vehicles[idx - 1].id) {
      const timestep = vehicles[idx].time - vehicles[idx - 1].time;
      const roundTime = parseFloat(timestep.toFixed(1));
      if (roundTime === 0.1) {
        d += haversine(
          vehicles[idx].x,
          vehicles[idx].y,
          vehicles[idx - 1].x,
          vehicles[idx - 1].y
        );
      }
    }

    if (idx < vehicles.length - 1) {
      if (vehicles[idx - 1].id !== vehicles[idx].id) {
        const dr = new Driver(vehicles[idx - 1].id, d, end, 0);
        drivers.push(dr);
        d = 0;
      }
    } else if (idx === vehicles.length - 1) {
      const dr = new Driver(vehicles[idx - 1].id, d, end, 0);
      drivers.push(dr);
      d = 0;
    }
  }

  return drivers;
}

parser.on("data", (data) => {
  for (let b = 0; b < 36000; b += 3600) {
    e = b + 3600;
    const inputData = getDataFromJson(b, e, data);
    const classList = classifyList(inputData);
    const distanceList = calculateDistances(classList, e);

    for (let i = 0; i < distanceList.length; i++) {
      console.log(distanceList[i].id, distanceList[i].distance);
      const data = [
        [3600, b, e - 0.1, distanceList[i].id, distanceList[i].distance],
      ];
      const fName = "../data/data_distance_" + numVehicles.toString() + ".csv";
      var stream = fs.createWriteStream(fName, { flags: "a" });

      stream.once("open", function (fd) {
        stream.write(data + "\r\n");
      });
      console.log("Filename: " + fName);
    }
  }
});
