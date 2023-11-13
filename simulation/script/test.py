import os

totalTime = 3600
insertionRate = 100
seeds = [41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60, 61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
numVehicles = insertionRate # number of vehicle
timeRound = 3600
b = 0
e = 3600
distances = [1000,1500,2000,2500,3000,3500,4000]
numVehicles = 100
totalTime = 3600

# init data of vehicle
for seed in seeds:
    # init data of simulation   
    command = "python3 test_init_simulation.py " + str(totalTime) + " " + str(seed)
    os.system(command)

    command = "python3 test_init_vehicle.py " + str(totalTime) + " " + str(insertionRate) + " " + str(seed)
    os.system(command)

    # convert xml data of vehicle to 
    command = "python3 test_convert_data.py " + str(totalTime) + " " + str(seed)
    os.system(command)

    for distance in distances:
        command = "node JSMinerCoin.js " + str(timeRound) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(seed) + " " + str(numVehicles) + " " + str(totalTime)
        os.system(command)
        distance += 200  
