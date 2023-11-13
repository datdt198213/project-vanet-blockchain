# Begin 

import os

totalTime = 3600
times = 3600
insertionRate = 100

numVehicles = insertionRate # number of vehicle

# init data of simulation   
command = "python3 py_init_simulation.py " + str(totalTime) + " " + str(insertionRate) + " " + str(times)
os.system(command)

# init data of vehicle
command = "python3 py_init_vehicle.py " + str(totalTime) + " " + str(insertionRate) + " " + str(times)
os.system(command)

# convert xml data of vehicle to 
command = "python3 py_convert_data.py " + str(totalTime) + " " + str(insertionRate) + " " + str(times)
os.system(command)