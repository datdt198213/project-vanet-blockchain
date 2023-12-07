import csv
import sys
import statistics

num = int(sys.argv[1])
csv_file_path = f'../data/data_statistic_{num}.csv'

timeslot = []
begin = []
end = [] 
distance = []
numNode = []
nPoD = []
total_time = []
total_node = []


with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        timeslot.append(row[0])
        begin.append(row[1])
        end.append(row[2])
        distance.append(row[3])
        numNode.append(row[4])
        nPoD.append(row[5])
        total_time.append(row[6])
        total_node.append(row[7])

percentages = []
tmp_timeslot = []
tmp_distance = []

for i in range(1, len(distance)):
    print(nPoD[i])
    percent = int(nPoD[i]) / int(numNode[i]) 
    percentages.append(percent)
    tmp_timeslot.append(timeslot[i])
    tmp_distance.append(distance[i])

    
data = []
timeslot = []
average = []
distance = []

times = 0
for j in range(1, 4):
    begin = times
    end = times + 10
    ave = 0
    for i in range(begin, end): # 0,10
        ave += percentages[i]
    ave /= 10
    average.append(ave)
    timeslot.append(tmp_timeslot[times])
    distance.append(tmp_distance[times])
    times += 10

d1 = []
d2 = []
d3 = []

for i in range(0, 10):
    d1.append(percentages[i]) 

for i in range(10, 20):
    d2.append(percentages[i]) 

for i in range(20, 30):
    d3.append(percentages[i]) 

std_dev1 = statistics.stdev(d1)
std_dev2 = statistics.stdev(d2)
std_dev3 = statistics.stdev(d3)

# Write data to file
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

for i in range(len(timeslot)):
    if distance[i] == '1000':
        file_name = f'../data/v_{result}_d_1000.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([timeslot[i], average[i], std_dev1, distance[i]])

    if distance[i] == '1500':
        file_name = f'../data/v_{result}_d_1500.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([timeslot[i], average[i], std_dev2, distance[i]])

    if distance[i] == '2000':
        file_name = f'../data/v_{result}_d_2000.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([timeslot[i], average[i], std_dev3, distance[i]])
