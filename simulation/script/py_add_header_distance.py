import csv
import sys

insertionRate = sys.argv[1]
f = open(f'../data/test{insertionRate}.csv', 'w')

writer = csv.writer(f)
writer.writerow(['Timeslot', 'Begin', 'End', 'Distance', 'Node per round', 'Node PoD', 'Total time', 'Total node', 'Total distance', 'Total coin', 'Received coin'])

