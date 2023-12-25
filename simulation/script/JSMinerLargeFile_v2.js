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
    
        for (let d = 1000; d <= 2000; d += 100) {
          // Declare variable totalDistance, totalCoin, nodeInPOD, coinEarning
          let totalDistance = 0;
          var totalCoin = 0;
          let nodeInPOD = 0;
          let coinEarning = 0;
          
          const coinList = newCalculateCoin(classList, d, e);
          
          // Calculate the number of distances and coins in a time round of proof of driving algorithms
          for (let i = 0; i < coinList.length; i++) {
            totalDistance += coinList[i].distance;
            totalCoin += coinList[i].coin;
            // Add number of node participating in proof of driving algorithms
            if (coinList[i].distance >= d) nodeInPOD++;
          }
          
          // Get nodes are filter by proof of driving algorithm
          const nodeFilterPOD = rule(coinList, d);

          // Calculate number of coins of all vehicles in a time round  
          for (let i = 0; i < nodeFilterPOD.length; i++) {
            coinEarning += nodeFilterPOD[i].coin;
          }

          // Calculate the average distance of all vehicle in a round
          const distanceAverage = totalDistance / coinList.length;
          console.log(distanceAverage, totalCoin, nodeFilterPOD.length)
    
          // Statistic
          const data = [
            [
              3600,
              b,
              e - 0.1,
              d,
              numVehicles,
              coinList.length,
              nodeFilterPOD.length,
              nodeInPOD,
              distanceAverage,
              totalCoin,
              coinEarning,
            ],
          ];
          
          // Write data to file 
          const fName = "../data/data_v2_" + numVehicles.toString() + ".csv";
          var stream = fs.createWriteStream(fName, { flags: "a" });
    
          stream.once("open", function (fd) {
            stream.write(data + "\r\n");
          });
          console.log("Filename: " + fName);
        }
      }
});

function newCalculateCoin(vehicles, distance, end) {
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
          totalDistance += d;
          const coin = parseInt(d / distance);
          totalCoin += coin;
          const dr = new Driver(vehicles[idx - 1].id, d, end, coin);
          drivers.push(dr);
          d = 0;
        }
      } else if (idx === vehicles.length - 1) {
        totalDistance += d;
        const coin = parseInt(d / distance);
        totalCoin += coin;
        const dr = new Driver(vehicles[idx - 1].id, d, end, coin);
        drivers.push(dr);
        d = 0;
      }
    }
  
    return drivers;
  }
  

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


