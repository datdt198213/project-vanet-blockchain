const fs = require('fs');
const crypto = require("crypto");
const maxTime = require("process");
const JSONStream = require('JSONStream');

const filename = "../sumo/vehicle1.json";

// Full time run simulation 
// const timeslot = parseFloat(maxTime.argv[2]);
// const beginTime = parseFloat(maxTime.argv[3]);
// const endTime = parseFloat(maxTime.argv[4]);
// const distance = parseFloat(maxTime.argv[5]);
// const times = parseFloat(maxTime.argv[6]);
// const numVehicles = parseFloat(maxTime.argv[7]);
// const totalTime = parseFloat(maxTime.argv[8]);
// const filename = "../sumo/vehicle" + times.toString() + ".json";

const readStream = fs.createReadStream(filename);
const parser = JSONStream.parse(['timestep', true]);

readStream.pipe(parser);

parser.on('data', (data) => {
  // Process each chunk of parsed JSON data
  console.log(data);
});

parser.on('end', () => {
  // The entire JSON file has been processed
  console.log('Finished reading JSON file.');
});

parser.on('error', (err) => {
  // Handle errors
  console.error('Error parsing JSON:', err);
});