import csv
import sys

result = int(sys.argv[1])

if result >= 90 and result <= 110:
    result = 100

elif result >= 190 and result <= 210:
    result = 200

elif result >= 290 and result <= 310:
    result = 300

elif result >= 390 and result <= 410:
    result = 400

elif result >= 490 and result <= 510:
    result = 500


file_name = f'../data/result_{result}.csv'

f = open(file_name, 'w', newline='')

writer = csv.writer(f)
writer.writerow(["Timeslot", "Average", "Distance"])
# writer.writerow(["Timeslot", "Average", "Distance", 'Total distance', 'Total coin', 'Received coin'])
