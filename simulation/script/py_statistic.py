import csv
import sys

num = int(sys.argv[1])
# Specify the path to your CSV file
csv_file_path = f'../data/data_statistic_{num}.csv'

# Open the CSV file

timeslot = []
begin = []
end = [] 
distance = []
numNode = []
nPoD = []
totalTime = []
totalNode = []

with open(csv_file_path, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Read and print each row in the CSV file
    for row in csv_reader:
        # print(row[4])
        timeslot.append(row[0])
        begin.append(row[1])
        end.append(row[2])
        distance.append(row[3])
        numNode.append(row[4])
        nPoD.append(row[5])
        totalTime.append(row[6])
        totalNode.append(row[7])

percentages = []
tmpTimeslot = []
tmpDistance = []
for i in range(1, len(distance)):
    percent = int(nPoD[i]) / int(numNode[i]) 
    tmpTimeslot.append(timeslot[i])
    tmpDistance.append(distance[i])
    percentages.append(percent)
    # print(percent)

    
data = []

times = 0
for j in range(1, 4):
    begin = times
    end = times + 10
    p = 0
    for i in range(begin, end): # 0,10
        # print(f"{timeslot[i]} + {i}")
        p += percentages[i]
    p /= 10
    d1 = {"Timeslot": tmpTimeslot[times], "Average": p, "Distance": tmpDistance[times]}
    data.append(d1)
    print(f"{p}, {tmpTimeslot[times]}, {tmpDistance[times]}")
    # write to file
    
    times += 10
    begin = times
    end = times + 5
    p = 0
    for i in range(begin, end): # 10, 15
        # print(f"{timeslot[i]} + {i}")
        p += percentages[i]
    p/= 5
    d1= {"Timeslot": tmpTimeslot[times], "Average": p, "Distance": tmpDistance[times]}
    data.append(d1)
    print(f"{p}, {tmpTimeslot[times]}, {tmpDistance[times]}")

    # write to file

    times += 5
    begin = times
    end = times + 3
    p = 0
    for i in range(begin, end): # 15, 18
        # print(f"{timeslot[i]} + {i}")
        p+= percentages[i]
    p /= 4
    d1= {"Timeslot": tmpTimeslot[times], "Average": p, "Distance": tmpDistance[times]}
    data.append(d1)
    print(f"{p}, {tmpTimeslot[times]}, {tmpDistance[times]}")
    # write to file

    times += 3
    begin = times
    end = times + 2
    p = 0
    for i in range(begin, end): # 19, 21
        p+= percentages[i]
    p /= 3
    d1= {"Timeslot": tmpTimeslot[times], "Average": p, "Distance": tmpDistance[times]}
    data.append(d1)
    print(f"{p}, {tmpTimeslot[times]},  {tmpDistance[times]}")
    times += 2
    
# Write the data

result = 100 

if num >= 90 and num <= 110:
    result = 100

elif num >= 190 and num <= 210:
    result = 200

elif num >= 290 and num <= 310:
    result = 300

elif num >= 390 and num <= 410:
    result = 400

elif num >= 490 and num <= 510:
    result = 500


file_name = f'../data/result_{result}.csv'
f = open(file_name, 'a', newline='')

fieldnames = ["Timeslot", "Average", "Distance"]

csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
csv_writer.writerows(data)