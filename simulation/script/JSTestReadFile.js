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
    begin = 0, end = 3600
    dataList = getDataFromJson(begin, end, data);
    console.log(dataList)
});

function getDataFromJson(begin, end, data) {

    dataList = [];

    data.timeslot.forEach((element) => {
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

    // Clear the cache to "close" the file (force a reload if needed)
    delete require.cache[require.resolve(filename)];
    
    return dataList;
}

parser.on('end', () => {
    // The entire JSON file has been processed
    console.log('Finished reading JSON file.');
});

parser.on('error', (err) => {
    // Handle errors
    console.error('Error parsing JSON:', err);
});