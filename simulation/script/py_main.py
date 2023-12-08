import os
import time

start = time.time()

totalTime = 36000
insertionRate = 290

for j in range(1, 4):
    for i in range(1, 22):
        print(insertionRate)
        command = f"node JSAddHeader_v1.js {insertionRate}"
        os.system(command)
        command = f"node JSMinerLargeFile_v1.js {insertionRate}"
        # command = f"node JSMinerLargeFile_v1.js {insertionRate}"
        os.system(command)

        insertionRate += 1
    insertionRate += 79

end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")