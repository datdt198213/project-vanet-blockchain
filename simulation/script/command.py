import os

seeds = [41,42,43,44,45,46,47,48,49,50]
timeRound = 3600
b = 0
e = 3600
distance = 1000
numVehicles = 100
totalTime = 3600
for seed in seeds:
    # init data of simulation   
    command = "node JSMinerCoin.js " + str(timeRound) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(seed) + " " + str(numVehicles) + " " + str(totalTime)
    os.system(command)