import os

totalTime = 36000
insertionRate = 190
for j in range(1, 2):
    # number of vehicles 90,190,290,390,490
    for i in range(1, 22):
        # number of vehicles 90=>110, 190=>210, 290=>310, 390=>410, 490=>510

        # init data of simulation   
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