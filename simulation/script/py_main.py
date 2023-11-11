# Begin 

import os

totalTime = 100
times = 1
insertionRate = 10
# number of vehicles 100, 200, 300, 400, 500
for i in range(1, 5):
    numVehicles = insertionRate # number of vehicle

    # init data of simulation   
    command = "python3 py_init_simulation.py " + str(totalTime) + " " + str(insertionRate) + " " + str(times)
    os.system(command)

    # init data of vehicle
    command = "python3 py_init_vehicle.py " + str(totalTime) + " " + str(insertionRate) + " " + str(times)
    os.system(command)

    # convert xml data of vehicle to 
    command = "python3 py_convert_data.py " + str(times) + " " + str(insertionRate) + " " + str(times)
    os.system(command)

    # Adding header in file csv
    command = "node JSAddHeader.js " + str(numVehicles)    
    os.system(command)

    distance = 1000

    # Distance 1km, 1.5km, 2km
    for k in range(1, 4):
        timeRound = 3600
        
        # Timeslot 1h, 2h, 3h, 4h
        for j in range(1, 5):
            b = 0
            e = timeRound
            # Loop TimeSlot 5 times
            while(1):
                if (b < totalTime): 
                    if (e > totalTime):
                        e = totalTime
                    command = "node JSMinerCoin.js " + str(timeRound) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(times) + " " + str(numVehicles)
                    os.system(command)
                    b += timeRound
                    e += timeRound
                else:
                    print("WARNING: Time end at " + str(totalTime))
                    break
            timeRound += 3600

        distance += 500
    
    times += 1
    insertionRate += 100

# command = "python3 py_add_header.py"
# os.system(command)

# command = "python3 py_handle_data.py"
# os.system(command)