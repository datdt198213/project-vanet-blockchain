import os

totalTime = 36000
insertionRate = 296

for i in range(1, 3):
    # number of vehicles 90=>110, 190=>210, 290=>310, 390=>410, 490=>510

    # # init data of simulation   
    # command = "python3 py_init_simulation.py " + str(totalTime) + " " + str(insertionRate)
    # os.system(command)

    # # init data of vehicle
    # command = "python3 py_init_vehicle.py " + str(totalTime) + " " + str(insertionRate)
    # os.system(command)

    # # convert xml data of vehicle to 
    # command = "python3 py_convert_data.py " + str(totalTime) + " " + str(insertionRate)
    # os.system(command)
    command = f"node JSAddHeader.js {insertionRate}"
    os.system(command)

    distance = 1000
    # d = 1000, 1500, 2000
    for k in range(1, 15):
        timeslot = 3600
        # Timeslot 1h, 2h, 3h, 4h
        # for j in range(1, 5):
        #     b = 0
        #     e = timeslot
        #     # Loop TimeSlot 5 times
        #     while(1):
        #         if (b < totalTime): 
        #             if (e > totalTime):
        #                 e = totalTime
        #             command = "python3 py_mine_coin.py " + str(timeslot) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(insertionRate) + " " + str(totalTime)
        #             # command = "node JSMinerCoin.js " + str(timeslot) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(insertionRate) + " " + str(totalTime)
        #             os.system(command)
        #             b += timeslot
        #             e += timeslot
        #         else:
        #             print("WARNING: Time end at " + str(totalTime))
        #             break
        #     timeslot += 3600
        
        b = 0
        e = timeslot
        
        while(1):
            if (b < totalTime): 
                if (e > totalTime):
                    e = totalTime
                # command = "python3 py_mine_coin.py " + str(timeslot) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(insertionRate) + " " + str(totalTime)
                # command = "node JSMinerCoin.js " + str(timeslot) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(insertionRate) + " " + str(totalTime)
                command = "node JSMinerLargeFile.js " + str(timeslot) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(insertionRate) + " " + str(totalTime)
                os.system(command)
                b += timeslot
                e += timeslot
            else:
                print("WARNING: Time end at " + str(totalTime))
                break
        distance += 500

    insertionRate += 1

# command = "python3 py_add_header.py"
# os.system(command)

# command = "python3 py_handle_data.py"
# os.system(command)