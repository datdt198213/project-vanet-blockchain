const params = require("process");
const numVehicles = parseFloat(params.argv[2]);
const fs = require('fs');
const header = ['Timeslot', 'Begin', 'End', 'Distance', 'Total node', 'Node per round', 'Node filter by PoD', 'Node paticipate POD', 'Distance average', 'Total coin', 'Coin earning'];
const fName = "../data/data_v1_" + numVehicles.toString() + ".csv"
var stream = fs.createWriteStream(fName, {'flags': 'a'});
// Running once time to add header
stream.once('open', function(fd) {
    stream.write(header+"\r\n");
  });