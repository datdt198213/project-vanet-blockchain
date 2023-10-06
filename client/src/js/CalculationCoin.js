const crypto = require("crypto");
const dataJson = require("../data/vehicle.json");
const maxTime = require("process");
const endTime = parseFloat(maxTime.argv[2])

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

// Calculate distance of a vehicle list, return a driver list
function calculateDistanceList(vehicles, distance, end) {
    drivers = [];

    d = 0;
    c = 0;
    for (let idx = 1; idx < vehicles.length; idx++) {
        if (vehicles[idx].id === vehicles[idx - 1].id) {
            timestep = vehicles[idx].time - vehicles[idx - 1].time;
            roundTime = parseFloat(timestep.toFixed(1));

            if (roundTime === 0.1) {
                d += Math.sqrt((vehicles[idx].x - vehicles[idx - 1].x) ** 2 + (vehicles[idx].y - vehicles[idx-1].y) ** 2);

                if (d >= distance) {
                    c = c + parseInt(d / distance);
                    d = d % distance;
                }
            }
        }

        if (vehicles[idx].time === end) {
            const dr = new Driver(vehicles[idx].id, d, end, c);
            drivers.push(dr);

            d = 0;
            c = 0;
        }
    }

    return drivers;
}

// Return satisfy node proof of driving
function rule(drivers) {
    nodePod = [];

    w = 0;
    drivers.forEach(d => {
        w += d.coin;
    })

    w = w / drivers.length;

    //  Get hash value of w
    let hashW = sha512(w.toString());

    for (let i = 0; i < drivers.length; i++) {
        //  Get hash value of driver
        hashCurrent = sha512(drivers[i].coin.toString());

        if (hashCurrent.localeCompare(hashW) <= 0) {
            nodePod.push(drivers[i]);
        }
    }

    return nodePod;
}

function main() {
    let begin = 0;
    let end = 2;
    let t = end - begin;
    let distance = 0.1;
    const count = Math.ceil(endTime / t);

    const output = [];

    for (let i = 0; i < count; i++) {
        let coins = [];

        const inputData = getDataFromJson(begin, end);

        const classList = classifyList(inputData);

        const distanceList = calculateDistanceList(classList, distance, end);
        
        const nPOD = rule(distanceList);

        nPOD.forEach((v) => {
            output.push(v);
        });

        begin += t;
        end += t;
        if (end > endTime) end = endTime;
    }

    output.forEach((v) => console.log(v));
}
const start = Date.now();
main();
const end = Date.now();
console.log(`Execution time: ${end - start} ms`);

module.exports = {
    rule
};
