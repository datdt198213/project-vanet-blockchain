Folder 'simulation/script' generate vehilce simulation data
Change directory to 'simulation/script' and run files below

# 1. Generating file vehicle.json, run file main.py 
### main.py 
Running 3 file Initial simulation => Initial Vehicle => Convert Data

### init_simulation.py
init_simulation.py initialize file simulation.sumo.cfg
Edit ending time in this file to change running time 

### init_vehicle.py
init_vehicle.py initialize file vehicle.sumo.xml
Edit ending time in this file to change running time

### convert_data.py
convert_data.py convert data from xml to json

# 2. Generating file data.csv, run file handle_data.py
### handle_data.py 
Running file add_header.py to add header in file data.csv
Generated Data use to traffic jam prediction 

# 3. Miner coin with POD algorithms
Run file MinerCoin.js to calculate number of coin vehicles earning from moving

```
node MinerCoin.js 0 1000
```

```0 is starting time running simulation, 1000 is ending time running simulation```

# 4. Statistic data
Run file statistic.py to draw diagram 