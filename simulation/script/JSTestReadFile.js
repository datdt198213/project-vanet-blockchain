const fs = require('fs');
const crypto = require("crypto");
const maxTime = require("process");
const JSONStream = require('JSONStream');

const filename = "../sumo/vehicle1.json";

// Full time run simulation 
const timeslot = parseFloat(maxTime.argv[2]);
const beginTime = parseFloat(maxTime.argv[3]);
const endTime = parseFloat(maxTime.argv[4]);
const distance = parseFloat(maxTime.argv[5]);
const times = parseFloat(maxTime.argv[6]);
const numVehicles = parseFloat(maxTime.argv[7]);
const totalTime = parseFloat(maxTime.argv[8]);
// const filename = "../sumo/vehicle" + times.toString() + ".json";

const readStream = fs.createReadStream(filename);
const parser = JSONStream.parse("*");

readStream.pipe(parser);

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
    // Process each chunk of parsed JSON data
    
    let begin = beginTime;                  // Beginning time calculates distances and coins in 1 round (s)
    let end = endTime;     
    if (isNaN(end)) console.log("Warning: Please enter beginning time parameter in running command");
    if (isNaN(begin)) console.log("Warning: Please enter ending time parameter in running command");
    if (isNaN(distance)) console.log("Warning: Please enter distance parameter in running command");
    if (endTime) console.log("\nTime begin = " + begin + " Time end = " + end);

    const inputData = getDataFromJson(begin, end, data);

    const classList = classifyList(inputData);
    
    const distanceList = calculateDistanceList(classList, distance, end);
    const nPOD = rule(distanceList);

    // Statistic

    const dataArrays = [[timeslot, begin, end - 0.1, distance, distanceList.length, nPOD.length, totalTime, numVehicles]]
    
    const fName = "../data/data_statistic_" + numVehicles.toString() + ".csv"
    var stream = fs.createWriteStream(fName, {'flags': 'a'});
    
    stream.once('open', function(fd) {
      stream.write(dataArrays+"\r\n");
      stream.end()
    });
    console.log("Filename: " + fName);
});

function getDataFromJson(begin, end, data) {

    dataList = [];

    data.timestep.forEach((element) => {
        time = Number(element.time);
        if (time >= begin && time <= end) {
            // Having a object
            if (element.vehicle != undefined) {
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
    // console.log("DONE calculate distance: Number of vehicle = " + drivers.length);
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

    // console.log("DONE rule: Number of node POD = " + nodePod.length);
    // nodePod.forEach((v) => console.log(v));
    return nodePod;
}

parser.on('end', () => {
    // The entire JSON file has been processed
    console.log('Finished reading JSON file.');
});

parser.on('error', (err) => {
    // Handle errors
    console.error('Error parsing JSON:', err);
});