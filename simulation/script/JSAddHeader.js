const params = require("process");
const numVehicles = parseFloat(params.argv[2]);
const fs = require('fs');
const header = ['Timeslot', 'Begin', 'End', 'Distance', 'Node per round', 'Node PoD', 'Total time', 'Total node'];
const fName = "../data/data_statistic_" + numVehicles.toString() + ".csv"
var stream = fs.createWriteStream(fName, {'flags': 'a'});
// Running once time to add header
stream.once('open', function(fd) {
    stream.write(header+"\r\n");
  });