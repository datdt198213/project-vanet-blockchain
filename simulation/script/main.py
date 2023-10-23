# Begin 

import os

totalTime = 1000

# Setting number of vehicle: numberOfVehice = (end - begin) / n
n = 4
numVehicles = totalTime / n


# # init data of simulation   
# command = "python3 init_simulation.py " + str(totalTime) + " " + str(n)
# os.system(command)

# # init data of vehicle
# command = "python3 init_vehicle.py " + str(totalTime) + " " + str(n)
# os.system(command)

# # convert xml data of vehicle to 
# command = "python3 convert_data.py " + str(totalTime) + " " + str(n)
# os.system(command)

# command = "python3 add_header.py"
# os.system(command)

timeRound = 7200 + 1800 # seconds (s)
b = 0
e = timeRound
distance = 2000

for i in range(1, 6):
    if (b < totalTime): 
        if (e > totalTime):
            e = totalTime
        command = "node MinerCoin.js " + str(timeRound) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(totalTime) + " " + str(numVehicles)
        os.system(command)
        b += timeRound
        e += timeRound
    else:
        print("WARNING: Time end at " + str(totalTime))
        break

# command = "python3 handle_data.py"
# os.system(command)