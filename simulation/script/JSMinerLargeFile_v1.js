const fs = require('fs');
const crypto = require("crypto");
const maxTime = require("process");
const JSONStream = require('JSONStream');
const numVehicles = parseFloat(maxTime.argv[2]);
const filename = "../sumo/vehicle" + numVehicles.toString() + ".json";
const readStream = fs.createReadStream(filename);
const parser = JSONStream.parse("*");
readStream.pipe(parser);

var totalCoin = 0;
var totalDistance = 0;
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
        this.time = Number (time);
    }
}
parser.on('data', (data) => {
    for (let b = 0; b < 36000; b += 3600) {
        e = b + 3600;
        const inputData = getDataFromJson(b, e, data);
        const classList = classifyList(inputData);

        // for (let d = 32500; d <= 33000; d += 1000) {
          // Declare variable totalDistance, totalCoin, nodeInPOD, coinEarning   
          let totalDistance = 0;
          var totalCoin = 0;
          let nodeInPOD = 0;
          let coinEarning = 0;
          const distanceList = calculateDistances(classList, e);
          
          // Calculate the total of distances in a time round of proof of driving algorithms
          for (let i = 0; i < distanceList.length; i++) {
            totalDistance += distanceList[i].distance;
          }

          // Calculate the average distance of all vehicle in a round
          const averageDistance = totalDistance / distanceList.length;
          
          // Count number of nodes participating in proof of driving algorithms
          for (let i = 0; i < distanceList.length; i++) {
            if (distanceList[i].distance >= averageDistance) nodeInPOD++;
          }
          
          // Calculate the number of coins in each vehicles
          const coinList = calculateCoins(distanceList, averageDistance)
          // const coinList = newCalculateCoin(classList, averageDistance, e);
          console.log(coinList)

          // Calculate the total of coins in a time round of proof of driving algorithms
          for (let i =0; i < coinList.length; i++) {
            totalCoin += coinList[i].coin;
          }

          // Get nodes are filter by proof of driving algorithm
          const nodeFilterPOD = rule(coinList);

          // Calculate number of coins of all vehicles in a time round 
          for (let i = 0; i < nodeFilterPOD.length; i++) {
            coinEarning += nodeFilterPOD[i].coin;
          }
    
          console.log(averageDistance, totalCoin, nodeFilterPOD.length)

          // Statistic
          const myData = [
            [
              3600,
              b,
              e - 0.1,
              averageDistance,
              numVehicles,
              coinList.length,
              nodeFilterPOD.length,
              nodeInPOD,
              averageDistance,
              totalCoin,
              coinEarning,
            ],
          ];
    
          // Write data to file
          const fName = "../data/data_v1_" + numVehicles.toString() + ".csv";
          var stream = fs.createWriteStream(fName, { flags: "a" });
    
          stream.once("open", function (fd) {
            stream.write(myData + "\r\n");
          });
          console.log("Filename: " + fName);
        }
      // }
    });

function calculateCoins(vehicles, averageDistance) {
  for(i= 0; i < vehicles.length; i++) {
    if (vehicles[i].distance >= averageDistance) {
      let coin = parseInt(vehicles[i].distance / averageDistance);
      vehicles[i].coin = coin;
    }
  }
  return vehicles;
}

// Calculate distance of a vehicle list, return a driver list
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

// Calculate distance of a vehicle list, return a driver list
// function newCalculateCoin(vehicles, distance, end) {
//     let drivers = [];
//     let d = 0;
  
//     for (let idx = 1; idx < vehicles.length; idx++) {
//       if (vehicles[idx].id === vehicles[idx - 1].id) {
//         const timestep = vehicles[idx].time - vehicles[idx - 1].time;
//         const roundTime = parseFloat(timestep.toFixed(1));
//         if (roundTime === 0.1) {
//           d += haversine(
//             vehicles[idx].x,
//             vehicles[idx].y,
//             vehicles[idx - 1].x,
//             vehicles[idx - 1].y
//           );
//         }
//       }
  
//       if (idx < vehicles.length - 1) {
//         if (vehicles[idx - 1].id !== vehicles[idx].id) {
//           const coin = parseInt(d / distance);
//           const dr = new Driver(vehicles[idx - 1].id, d, end, coin);
//           drivers.push(dr);
//           d = 0;
//         }
//       } else if (idx === vehicles.length - 1) {
//         const coin = parseInt(d / distance);
//         const dr = new Driver(vehicles[idx - 1].id, d, end, coin);
//         drivers.push(dr);
//         d = 0;
//       }
//     }
  
//     return drivers;
// }
  

function getDataFromJson(begin, end, data) {
    dataList = [];
    data.timestep.forEach((element) => {
        time = Number(element.time);
        if (time >= begin && time <= end) {
            if (element.vehicle != undefined) {
                if (element.vehicle.length == undefined) {
                    dataList.push(new Vehicle(element.vehicle, element.time));
                }
                else {
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
    const R = 6371; 
    const dLat = (lat2 - lat1) * (Math.PI / 180);
    const dLon = (lon2 - lon1) * (Math.PI / 180);
    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * (Math.PI / 180)) * Math.cos(lat2 * (Math.PI / 180)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    var distance = R * c; 
    distance *= 1000;
    return distance;
}



// Hash string by sha512
function sha512(inputString) {
    return crypto.createHash("sha512").update(inputString).digest("hex");
}

// Return satisfy node proof of driving
function rule(drivers) {
  nodePod = [];

  let w = 0;
  drivers.forEach((d) => {
    w += d.coin;
  });
  w = w / drivers.length;

  //  Get hash value of w
  let hashW = sha512(w.toString());

  for (let i = 0; i < drivers.length; i++) {
    //  Get hash coin value of a driver
    if (drivers[i].coin != 0) {
      hashCurrent = sha512(drivers[i].coin.toString());
      if (hashCurrent.localeCompare(hashW) <= 0) {
        nodePod.push(drivers[i]);
      }
    }
  }
  return nodePod;
}


parser.on('end', () => {
    console.log('Finished reading JSON file.');
});

parser.on('error', (err) => {
    console.error('Error parsing JSON:', err);
});


