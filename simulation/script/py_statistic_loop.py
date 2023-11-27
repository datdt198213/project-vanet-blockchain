import os

insertion_rate = 290

for i in range(1, 22):
    command = f"py py_statistic.py {insertion_rate}"
    os.system(command)
    insertion_rate += 1

# ------------------------------------------------------------------
