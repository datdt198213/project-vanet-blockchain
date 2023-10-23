const crypto = require("crypto");
const maxTime = require("process");
const fs = require('fs');

// Full time run simulation 
const timeslot = parseFloat(maxTime.argv[2]);
const beginTime = parseFloat(maxTime.argv[3]);
const endTime = parseFloat(maxTime.argv[4]);
const distance = parseFloat(maxTime.argv[5]);
const totalTime = parseFloat(maxTime.argv[6]);
const numVehicles = parseFloat(maxTime.argv[7]);

const filename = "../data/vehicle" + totalTime.toString() + "_" + numVehicles.toString() + ".json";
// const dataJson = require("../data/vehicle1.json");
const dataJson = require(filename);
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
        this.time = Number (time);
    }
}

// Hash string by sha512
function sha512(inputString) {
    return crypto.createHash("sha512").update(inputString).digest("hex");
}

function getFistElement(drivers) {
    return drivers.map((subarray) => subarray[0]);
}

// Get data from json and return list of vehicle in a period of time
function getDataFromJson(begin, end) {
    const data = dataJson["fcd-export"]["timestep"];

    dataList = [];

    data.forEach((element) => {
        time = Number(element.time);
        if (time >= begin && time <= end) {
            // Having a object
            if (element.vehicle.length == undefined) {
                // Push data to list
                dataList.push(new Vehicle(element.vehicle, element.time));
            }
            // Having object list
            else {
                // Push data to list
                element.vehicle.forEach((v) => {
                    dataList.push(new Vehicle(v, element.time));
                });
            }
        }
    });

    return dataList;
}

function getAllDataJson() {
    const data = dataJson["fcd-export"]["timestep"];

    dataList = [];

    data.forEach((element) => {
        // Having a object
        if (element.vehicle.length === undefined) {
            // Push data to list
            dataList.push(new Vehicle(element.vehicle, element.time));
        }
        // Having object list
        else {
            // Push data to list
            element.vehicle.forEach((v) => {
                dataList.push(new Vehicle(v, element.time));
            });
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

    // newDrivers.forEach((v) => {console.log(v)})
    // console.log("DONE Classify list: Length = " + newDrivers.length)
    return newDrivers;
}

// calculate distance by haversine formal (miles)
function haversine(lat1, lon1, lat2, lon2) {
    const R = 6371; // Radius of the Earth in kilometers
    const dLat = (lat2 - lat1) * (Math.PI / 180);
    const dLon = (lon2 - lon1) * (Math.PI / 180);

    const a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.cos(lat1 * (Math.PI / 180)) * Math.cos(lat2 * (Math.PI / 180)) *
        Math.sin(dLon / 2) * Math.sin(dLon / 2);

    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    var distance = R * c; // The distance in kilometers
    distance *= 1000; // km => m
    return distance;
}

// Calculate distance of a vehicle list, return a driver list
function calculateDistanceList(vehicles, distance, end) {
    // console.log("Vehicle length in calculate distance: " + vehicles.length);
    // vehicles.forEach((v) => {console.log(v)})
    // console.log("INPUT calculate distance: Length = " + vehicles.length);
    
    var drivers = [];
    d = 0;
    c = 0;
    for (let idx = 1; idx < vehicles.length; idx++) {
        // console.log("calculateDistanceList: ")
        if (vehicles[idx].id === vehicles[idx - 1].id) {
            timestep = vehicles[idx].time - vehicles[idx - 1].time;
            roundTime = parseFloat(timestep.toFixed(1));

            if (roundTime === 0.1) {
                d += haversine(vehicles[idx].x, vehicles[idx].y, vehicles[idx-1].x, vehicles[idx-1].y);
                // console.log("Distance = ", d)
                if (d >= distance) {
                    c = c + parseInt(d / distance);
                    d = d % distance;
                }
                // console.log("Coin = ", c)
            }
        } 

        if (idx < vehicles.length - 1) {
            if (vehicles[idx - 1].id != vehicles[idx].id) {
                const dr = new Driver(vehicles[idx - 1].id, d, end, c);
                // console.log(dr)
                drivers.push(dr);
                // console.log("Dr Coin", dr.coin)
                d = 0;
                c = 0;
            }  
        } else if (idx == vehicles.length - 1) {
            const dr = new Driver(vehicles[idx - 1].id, d, end, c);
            // console.log(dr)
            drivers.push(dr);
            // console.log("Dr Coin", dr.coin)
            d = 0;
            c = 0;
        }
           
    }

    // drivers.forEach(v => console.log(v))
    console.log("DONE calculate distance: Number of vehicle = " + drivers.length);

    return drivers;
}

// Return satisfy node proof of driving
function rule(drivers) {
    // console.log("INPUT rule: number of drivers = " + drivers.length);

    nodePod = [];

    w = 0;
    drivers.forEach(d => {
        // console.log("d: " + d.coin)
        w += d.coin;
    })
    // console.log("w: " + w)
    // console.log("driver.length:  " + drivers.length)
    w = w / drivers.length;

    //  Get hash value of w
    let hashW = sha512(w.toString());

    for (let i = 0; i < drivers.length; i++) {
        //  Get hash value of driver
        if (drivers[i].coin != 0) {
            hashCurrent = sha512(drivers[i].coin.toString());

            if (hashCurrent.localeCompare(hashW) <= 0) {
                nodePod.push(drivers[i]);
            }
        }
    }

    console.log("DONE rule: Number of node POD = " + nodePod.length);
    // nodePod.forEach((v) => console.log(v));
    return nodePod;
}

function countNumberOfVehicle(listVehicle) {
    // Starting counter at first element in list vehicle
    let count = 0;
    if (listVehicle.length != 0) {
        count = 1;
        for (let i = 0; i < listVehicle.length - 1; i++) 
            if (listVehicle[i].id === listVehicle[i+1].id) continue
            else count++
    }
        
    return count;
}

function main() {
    let begin = beginTime;                  // Beginning time calculates distances and coins in 1 round (s)
    let end = endTime;     
    if (isNaN(end)) console.log("Warning: Please enter beginning time parameter in running command");
    if (isNaN(begin)) console.log("Warning: Please enter ending time parameter in running command");
    if (isNaN(distance)) console.log("Warning: Please enter distance parameter in running command");
    if (endTime)
    console.log("\nTime begin = " + begin + " Time end = " + end);

    let d = distance;            // Distance to earning coin (m)
    const count = Math.ceil(endTime / timeslot);
    // console.log("Count: " + count);

    const output = [];

    const inputData = getDataFromJson(begin, end);

    const classList = classifyList(inputData);
    
    const distanceList = calculateDistanceList(classList, distance, end);

    

    const nPOD = rule(distanceList);
    // console.log(inputData)
    // console.log(classList.length);
    

    // for (let i = 0; i < count; i++) {
    //     let coins = [];

    //     const inputData = getDataFromJson(begin, end);

    //     const classList = classifyList(inputData);
        
    //     const distanceList = calculateDistanceList(classList, distance, end);

    //     const nPOD = rule(distanceList);

    //     nPOD.forEach((v) => {
    //         // console.log(v)
    //         output.push(v);
    //     });

    //     if (end === 3600) {
    //         console.log("Time end = " + end);
    //         console.log(inputData)
    //         // console.log(classList)
    //         // console.log(distanceList)
    //         // console.log(nPOD)
    //     }

    //     begin += timeslot;
    //     end += timeslot;
    //     if (end > endTime) end = endTime;
    // }

    // output.forEach((v) => console.log(v));

    // Statistics
    // var allDataJson = getAllDataJson();
    // var classifyAllData = classifyList(allDataJson);
    // var numberOfVehicle = countNumberOfVehicle(classifyAllData);
    // console.log("Number of vehicle ", numberOfVehicle)
    
    
    // Statistic
    const header = ['Timeslot', 'Begin', 'End', 'Distance', 'Total node', 'Node received coin'];
    const dataArrays = [
    [timeslot, begin, end, distance, distanceList.length, nPOD.length]]
    

    var stream = fs.createWriteStream("../data/data_statistic.csv", {'flags': 'a'});
    
    // Running once time to add header
    // stream.once('open', function(fd) {
    //     stream.write(header+"\r\n");
    //   });
    
    stream.once('open', function(fd) {
      stream.write(dataArrays+"\r\n");
    });
}
const start = Date.now();
main();
const end = Date.now();
console.log(`Execution time: ${end - start} ms`);

module.exports = {
    rule
};


