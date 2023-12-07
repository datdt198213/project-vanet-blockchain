import os
import time

start = time.time()

totalTime = 36000
insertionRate = 508

# for j in range(1, 3):
for i in range(1, 4):
    print(insertionRate)
    command = f"node JSHTest.js {insertionRate}"
    os.system(command)
    # command = f"node JSTest.js {insertionRate}"
    command = f"node JSMinerCoin_v1.js {insertionRate}"
    os.system(command)

    insertionRate += 1
    # insertionRate += 79

end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")