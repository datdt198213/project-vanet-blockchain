const fs = require('fs');
const readline = require('readline');

const filename = "../sumo/vehicle41.json";
const readStream = fs.createReadStream(filename);
const rl = readline.createInterface({
  input: readStream,
  crlfDelay: Infinity
});

// Create an empty string to store the JSON data
let jsonData = '';

rl.on('line', (line) => {
  // Process each line of the file
  jsonData += line;
});

rl.on('close', () => {
  // Parse the accumulated JSON data
  const parsedData = JSON.parse(jsonData);

  // Now you can work with the parsed data
  console.log(parsedData);
});