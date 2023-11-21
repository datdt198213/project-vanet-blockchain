import os
import sys

totalTime = int(sys.argv[1])
insertionRate = int(sys.argv[2]) # number vehicles

# init data of simulation   
command = "python3 py_init_simulation.py " + str(totalTime) + " " + str(insertionRate)
os.system(command)

# init data of vehicle
command = "python3 py_init_vehicle.py " + str(totalTime) + " " + str(insertionRate)
os.system(command)

# convert xml data of vehicle to 
command = "python3 py_convert_data.py " + str(totalTime) + " " + str(insertionRate)
os.system(command)
