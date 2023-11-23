import os

insertionRate = 190

command = f"py py_add_statistic_header.py {insertionRate}"
os.system(command)

for i in range(1, 22):
    command = f"py py_statistic.py {insertionRate}"
    os.system(command)
    insertionRate += 1

insertionRate -= 1
command = f"py py_test.py {insertionRate}"
os.system(command)
# ------------------------------------
