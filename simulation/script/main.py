# Begin 

import os

endingTime = 32000

# Setting number of vehicle: numberOfVehice = (end - begin) / n
n = 16

# # init data of simulation
# command = "python3 init_simulation.py " + str(endingTime)
# os.system(command)

# # init data of vehicle
# command = "python3 init_vehicle.py " + str(endingTime) + " " + str(n)
# os.system(command)

# # convert xml data of vehicle to 
# command = "python3 convert_data.py"
# os.system(command)

# command = "python3 add_header.py"
# os.system(command)

timeRound = 3600 # seconds (s)
b = 0
e = timeRound

for i in range(1, 6):
    command = "node MinerCoin.js " + str(b) + " " + str(e)
    os.system(command)
    b += timeRound
    e += timeRound

# command = "python3 handle_data.py"
# os.system(command)