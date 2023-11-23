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
total_time = []
total_node = []
# total_distance = []
# total_coin = []
# received_coin = []

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
        total_time.append(row[6])
        total_node.append(row[7])
        # total_distance.append(row[8])
        # total_coin.append(row[9])
        # received_coin.append(row[10])

percentages = []
tmp_timeslot = []
tmp_distance = []
tmp_total_coin = []
tmp_total_distance = []
tmp_received_coin = []

for i in range(1, len(distance)):
    percent = int(nPoD[i]) / int(numNode[i]) 
    percentages.append(percent)
    tmp_timeslot.append(timeslot[i])
    tmp_distance.append(distance[i])
    # tmp_total_coin.append(float(total_coin[i]))
    # tmp_total_distance.append(float(total_distance[i]))
    # tmp_received_coin.append(float(received_coin[i]))
    # print(percent)

    
data = []

times = 0
for j in range(1, 4):
    begin = times
    end = times + 10
    p = 0
    # tc = 0
    # td = 0
    # rc = 0
    for i in range(begin, end): # 0,10
        # print(f"{timeslot[i]} + {i}")
        p += percentages[i]
        # tc += tmp_total_coin[i]
        # td += tmp_total_distance[i]
        # rc += tmp_received_coin[i]
    p /= 10
    # tc /= 10
    # td /= 10
    # rc /= 10
    # d1 = {"Timeslot": tmp_timeslot[times], "Average": p, "Distance": tmp_distance[times], "Total distance": td, "Total coin": tc, "Received coin": rc }
    d1 = {"Timeslot": tmp_timeslot[times], "Average": p, "Distance": tmp_distance[times] }
    data.append(d1)
    print(f"{p}, {tmp_timeslot[times]}, {tmp_distance[times]}")
    # write to file
    
    times += 10
    begin = times
    end = times + 5
    p = 0
    # tc = 0
    # td = 0
    # rc = 0
    for i in range(begin, end): # 10, 15
        # print(f"{timeslot[i]} + {i}")
        p += percentages[i]
        # tc += tmp_total_coin[i]
        # td += tmp_total_distance[i]
        # rc += tmp_received_coin[i]
    p/= 5
    # tc /= 5
    # td /= 5
    # rc /= 5
    # d1 = {"Timeslot": tmp_timeslot[times], "Average": p, "Distance": tmp_distance[times], "Total distance": td, "Total coin": tc, "Received coin": rc }
    d1 = {"Timeslot": tmp_timeslot[times], "Average": p, "Distance": tmp_distance[times] }
    data.append(d1)
    print(f"{p}, {tmp_timeslot[times]}, {tmp_distance[times]}")

    # write to file

    times += 5
    begin = times
    end = times + 3
    p = 0
    # tc = 0
    # td = 0
    # rc = 0
    for i in range(begin, end): # 15, 18
        # print(f"{timeslot[i]} + {i}")
        p+= percentages[i]
        # tc += tmp_total_coin[i]
        # td += tmp_total_distance[i]
        # rc += tmp_received_coin[i]
    p /= 4
    # tc /= 4
    # td /= 4
    # rc /= 4
    # d1 = {"Timeslot": tmp_timeslot[times], "Average": p, "Distance": tmp_distance[times], "Total distance": td, "Total coin": tc, "Received coin": rc }
    d1 = {"Timeslot": tmp_timeslot[times], "Average": p, "Distance": tmp_distance[times] }
    data.append(d1)
    print(f"{p}, {tmp_timeslot[times]}, {tmp_distance[times]}")
    # write to file

    times += 3
    begin = times
    end = times + 2
    p = 0
    # tc = 0
    # td = 0
    # rc = 0
    for i in range(begin, end): # 19, 21
        p+= percentages[i]
        # tc += tmp_total_coin[i]
        # td += tmp_total_distance[i]
        # rc += tmp_received_coin[i]
    p /= 3
    # tc /= 4
    # td /= 4
    # rc /= 4
    # d1 = {"Timeslot": tmp_timeslot[times], "Average": p, "Distance": tmp_distance[times], "Total distance": td, "Total coin": tc, "Received coin": rc }
    d1 = {"Timeslot": tmp_timeslot[times], "Average": p, "Distance": tmp_distance[times] }
    data.append(d1)
    print(f"{p}, {tmp_timeslot[times]},  {tmp_distance[times]}")
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

# fieldnames = ["Timeslot", "Average", "Distance", "Total distance", "Total coin", "Received coin"]
fieldnames = ["Timeslot", "Average", "Distance"]

csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
csv_writer.writerows(data)