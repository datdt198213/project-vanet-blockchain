import csv
f = open('../data/data.csv', 'w')

writer = csv.writer(f)
writer.writerow(["Node", "Timestamp", "X", "Y", "Velocity", "Duration", "Road Type", "Road Condition", "Road Event", "Congestion"])

print(f'DONE add_header.py: add header to file data.csv')

