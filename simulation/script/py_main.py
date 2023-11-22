import os

totalTime = 36000
insertionRate = 90

# command = "python3 py_init.py " + str(totalTime) + " " + str(insertionRate)
# os.system(command)
# command = "python3 py_mining_coin.py " + str(totalTime) + " " + str(insertionRate)
# os.system(command)

# timeslot = 3600
# b = 0
# e = 3600
# distance = 1000
# command = "py py_mine_coin.py " + str(timeslot) + " " + str(b) + " " + str(e) + " " + str(distance) + " " + str(insertionRate) + " " + str(totalTime)
# os.system(command)


for j in range(1, 4):
    
    # number of vehicles 90,190,290,390,490
    for i in range(1, 22):
        # number of vehicles 90=>110, 190=>210, 290=>310, 390=>410, 490=>510
   
        # command = "python3 py_init.py " + str(totalTime) + " " + str(insertionRate)
        # os.system(command)

        command = "python3 py_mining_coin.py " + str(totalTime) + " " + str(insertionRate)
        os.system(command)

        insertionRate += 1

    insertionRate += 79
# command = "python3 py_add_header.py"
# os.system(command)

# command = "python3 py_handle_data.py"
# os.system(command)