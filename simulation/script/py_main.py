import os
import time

start = time.time()

totalTime = 36000
insertionRate = 90

for j in range(1, 3):
    for i in range(1, 22):
        print(insertionRate)
        command = f"node JSAddHeader_v1.js {insertionRate}"
        os.system(command)
        # command = f"node JSTest.js {insertionRate}"
        command = f"node JSMinerCoin_v1.js {insertionRate}"
        os.system(command)

        insertionRate += 1
    insertionRate += 79

end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")