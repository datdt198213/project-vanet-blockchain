# Begin 

import os

totalTime = 3600
times = 3600
insertionRate = 100
seeds = [41,42,43,44,45,46,47,48,49,50]
numVehicles = insertionRate # number of vehicle

# init data of simulation   
command = "python3 py_init_simulation.py " + str(totalTime) + " " + str(insertionRate) + " " + str(times)
os.system(command)
# for seed in seeds:
#     # init data of vehicle
#     command = "python3 py_init_vehicle.py " + str(totalTime) + " " + str(insertionRate) + " " + str(times) + " " + str(seed)
#     os.system(command)
command = "python3 py_init_vehicle.py " + str(totalTime) + " " + str(insertionRate) + " " + str(times)
os.system(command)
# convert xml data of vehicle to 
command = "python3 py_convert_data.py " + str(totalTime) + " " + str(insertionRate) + " " + str(times)
os.system(command)