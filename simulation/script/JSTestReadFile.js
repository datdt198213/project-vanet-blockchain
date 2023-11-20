const fs = require('fs');

const filename = "../sumo/vehicle41.json";
const JSONStream = require('JSONStream');

const readStream = fs.createReadStream(filename);
const parser = JSONStream.parse('*');

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