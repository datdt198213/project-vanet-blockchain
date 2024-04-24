// Thuật toán POD khi quãng đường của các xe được tích lũy qua từng round 

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

// Có tích lũy quãng đường - v3
parser.on('data', (data) => {
    let oldVehicles = [];
    timeslot = 1200
    for (let b = 0; b < 36000; b += timeslot) {
        let e = b + timeslot;
        const inputData = getDataFromJson(b, e, data);
        const classList = classifyList(inputData);
        let totalDistance = 0;
        var totalCoin = 0;
        let nodeInPOD = 0;
        let coinEarning = 0;
        const newVehicles = calculateDistances(classList, e);
        console.log("Hello")
        // console.log(oldVehicles)
        
        
        // Calculate the total of distances in a time round of proof of driving algorithms
        for (let i = 0; i < newVehicles.length; i++) {
          totalDistance += newVehicles[i].distance;
        }
        
        // Calculate the average distance of all vehicle in a round
        const averageDistance = totalDistance / newVehicles.length;
        // const averageDistance = 40000;
        
        // Count number of nodes participating in proof of driving algorithms
        const distanceList = accumulateDistance(oldVehicles, newVehicles);
        for (let i = 0; i < distanceList.length; i++) {
          if (distanceList[i].distance >= averageDistance) nodeInPOD++;
        }
        
        // Calculate the number of coins in each vehicles
        const coinList = calculateCoins(distanceList, averageDistance)

        // Calculate the total of coins in a time round of proof of driving algorithms
        for (let i =0; i < coinList.length; i++) {
          totalCoin += coinList[i].coin;
        }

        // Get nodes are filter by proof of driving algorithm
        const nodeFilterPOD = rule(coinList, averageDistance);

        // Calculate number of coins of all vehicles in a time round 
        for (let i = 0; i < nodeFilterPOD.length; i++) {
          coinEarning += nodeFilterPOD[i].coin;
        }
  
        console.log(`Average Distance: ${averageDistance}, Total coin ${totalCoin}, Num POD: ${nodeFilterPOD.length}`)

        // Statistic
        const myData = [
          [
            timeslot,
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

        // If implement in blockchain, we need to store current state of distance of vehicles in the system
        oldVehicles = updateDistance(distanceList, averageDistance)
  
        // Write data to file
        const fName = "../data/Result_consider_time/data_v5_" + numVehicles.toString() + ".csv";
        var stream = fs.createWriteStream(fName, { flags: "a" });
  
        stream.once("open", function (fd) {
          stream.write(myData + "\r\n");
        });
        console.log("Filename: " + fName);
    }
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

function updateDistance(vehicles, averageDistance) {
  for(i= 0; i < vehicles.length; i++) {
    if (vehicles[i].distance >= averageDistance) {
      vehicles[i].distance = vehicles[i].distance % averageDistance;
    }
  }
  return vehicles;
}

function accumulateDistance(oldVehicles, newVehicles) {
  let tempVehicles = newVehicles;
  if(oldVehicles.length > 0) {
    for (let i = 0; i < oldVehicles.length - 1; i++) {
      for (let j = 0; j < tempVehicles.length - 1; j++) {
        if (tempVehicles[i].id === oldVehicles[i].id) {
          tempVehicles[i].distance += oldVehicles[i].distance;
          break;
        }
      }
    }
  }  
  return tempVehicles;
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

// function newCalculateCoin(vehicles, distance, end) {
//     let drivers = [];
//     let d = 0;
  
//     for (let idx = 1; idx < vehicles.length; idx++) {
//       if (vehicles[idx].id === vehicles[idx - 1].id) {
//         const timestep = vehicles[idx].time - vehicles[idx - 1].time;
//         const roundTime = parseFloat(timestep.toFixed(1));
//         if (roundTime === 0.1) {
//           d += haversine(vehicles[idx].x, vehicles[idx].y, vehicles[idx - 1].x, vehicles[idx - 1].y);
//         }
//       }
  
//       if (idx < vehicles.length - 1) {
//         if (vehicles[idx - 1].id !== vehicles[idx].id) {
//           totalDistance += d;
//           const coin = parseInt(d / distance);
//           totalCoin += coin;
//           const dr = new Driver(vehicles[idx - 1].id, d, end, coin);
//           drivers.push(dr);
//           d = 0;
//         }
//       } else if (idx === vehicles.length - 1) {
//         totalDistance += d;
//         const coin = parseInt(d / distance);
//         totalCoin += coin;
//         const dr = new Driver(vehicles[idx - 1].id, d, end, coin);
//         drivers.push(dr);
//         d = 0;
//       }
//     }
  
//     return drivers;
//   }
  

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

// Calculate distance of a vehicle list, return a driver list
function calculateDistanceList(vehicles, distance, end) {
    
    var drivers = [];
    d = 0;
    c = 0;
    for (let idx = 1; idx < vehicles.length; idx++) {
        if (vehicles[idx].id === vehicles[idx - 1].id) {
            timestep = vehicles[idx].time - vehicles[idx - 1].time;
            roundTime = parseFloat(timestep.toFixed(1));

            if (roundTime === 0.1) {
                d += haversine(vehicles[idx].x, vehicles[idx].y, vehicles[idx-1].x, vehicles[idx-1].y);
                if (d >= distance) {
                    c = c + parseInt(d / distance);
                    d = d % distance;
                }
            }
        } 

        if (idx < vehicles.length - 1) {
            if (vehicles[idx - 1].id != vehicles[idx].id) {
                const dr = new Driver(vehicles[idx - 1].id, d, end, c);
                drivers.push(dr);
                d = 0;
                c = 0;
            }  
        } else if (idx == vehicles.length - 1) {
            const dr = new Driver(vehicles[idx - 1].id, d, end, c);
            drivers.push(dr);
            d = 0;
            c = 0;
        }
           
    }
    return drivers;
}

// Hash string by sha512
function sha512(inputString) {
    return crypto.createHash("sha512").update(inputString).digest("hex");
}

// Return satisfy node proof of driving
function rule(drivers, distance) {
    // console.log("INPUT rule: number of drivers = " + drivers.length);
  
    nodePod = [];
  
    //let w = 0;
    let totalDistance = 0;
    drivers.forEach((d) => {
      // w += d.coin;
      totalDistance += d.distance;
    });
    let distanceAverage = totalDistance / drivers.length;
    // w = w / drivers.length;
  
    //  Get hash value of w
    // let hashW = sha512(w.toString());
    let hashD = sha512(distanceAverage.toString());
  
    for (let i = 0; i < drivers.length; i++) {
      //  Get hash value of driver
      // if (drivers[i].coin != 0) {
      //   hashCurrent = sha512(drivers[i].coin.toString());
      //   if (hashCurrent.localeCompare(hashW) <= 0) {
      //     nodePod.push(drivers[i]);
      //   }
      // }
      if (drivers[i].distance > distance) {
        hashCurrent = sha512(drivers[i].distance.toString());
        if (hashCurrent.localeCompare(hashD) <= 0) {
          nodePod.push(drivers[i]);
        }
      }
    }
  
    // console.log("DONE rule: Number of node POD = " + nodePod.length);
    return nodePod;
  }

parser.on('end', () => {
    console.log('Finished reading JSON file.');
});

parser.on('error', (err) => {
    console.error('Error parsing JSON:', err);
});


