import os

insertion_rate = 490

for i in range(1, 22):
    # command = f"py py_statistic_result_v1.py {insertion_rate}"
    command = f"py py_statistic_result_v2.py {insertion_rate}"
    os.system(command)
    insertion_rate += 1

# ------------------------------------------------------------------
