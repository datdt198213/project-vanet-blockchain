import csv
f = open('../data/result_100.csv', 'w')

writer = csv.writer(f)
writer.writerow(["Timeslot", "Average", "Distance"])

print(f'DONE add_header.py: add header to file data.csv')

