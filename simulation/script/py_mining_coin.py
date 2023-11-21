import os

totalTime = 36000
times = 1
insertionRate = 90

# number of vehicles 100, 200, 300, 400, 500
for i in range(1, 22):
    numVehicles = insertionRate # number of vehicle
    distance = 1000
    command = "node JSAddHeader.js " + str(numVehicles)
    os.system(command)

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
                    command = "node JSMinerCoin.js " + str(timeRound) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(times) + " " + str(numVehicles) + " " + str(totalTime)
                    os.system(command)
                    b += timeRound
                    e += timeRound
                else:
                    print("WARNING: Time end at " + str(totalTime))
                    break
            timeRound += 3600

        distance += 500
        
    times += 1
    insertionRate += 1

   
