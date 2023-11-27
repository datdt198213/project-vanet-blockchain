import csv
import sys

insertionRate = sys.argv[1]
f = open(f'../data/data_test_{insertionRate}.csv', 'w', newline='')

writer = csv.writer(f)
writer.writerow(['Timeslot', 'Begin', 'End', 'Distance', 'Node per round', 'Node filter by PoD', 'Total time', 'Total node', 'Node paticipate POD', 'Distance average', 'Total coin', 'Coin earning'])

