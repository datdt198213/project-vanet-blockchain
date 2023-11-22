import os
import sys

totalTime = int(sys.argv[1])
insertionRate = int(sys.argv[2])
distance = 1000

command = "node JSAddHeader.js " + str(insertionRate)
os.system(command)

# Distance 1km, 1.5km, 2km
for k in range(1, 4):
    timeslot = 3600
    # Timeslot 1h, 2h, 3h, 4h
    for j in range(1, 5):
        b = 0
        e = timeslot
        # Loop TimeSlot 5 times
        while(1):
            if (b < totalTime): 
                if (e > totalTime):
                    e = totalTime
                command = "py py_mine_coin.py " + str(timeslot) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(insertionRate) + " " + str(totalTime)
                # command = "node JSMinerCoin.js " + str(timeslot) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(insertionRate) + " " + str(totalTime)
                os.system(command)
                b += timeslot
                e += timeslot
            else:
                print("WARNING: Time end at " + str(totalTime))
                break
        timeslot += 3600
    distance += 500

   
