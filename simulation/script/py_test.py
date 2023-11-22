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

csv_file_path = f'../data/result_{result}.csv'


timeslot = []
average = []
distance = []
with open(csv_file_path, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Read and print each row in the CSV file
    for row in csv_reader:
        # print(row[4])
        timeslot.append(row[0])
        average.append(row[1])
        distance.append(row[2])

print(len(timeslot))
for i in range(1, len(timeslot)):
    if timeslot[i] == '3600':
        file_name = f'../data/vehicle_{result}_1h.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([timeslot[i], average[i], distance[i]])
    
    if timeslot[i] == '7200':
        file_name = f'../data/vehicle_{result}_2h.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([timeslot[i], average[i], distance[i]])

    if timeslot[i] == '10800':
        file_name = f'../data/vehicle_{result}_3h.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([timeslot[i], average[i], distance[i]])
    
    if timeslot[i] == '14400':
        file_name = f'../data/vehicle_{result}_4h.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([timeslot[i], average[i], distance[i]])

    if distance[i] == '1000':
        file_name = f'../data/vehicle_{result}_1000.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([timeslot[i], average[i], distance[i]])

    if distance[i] == '1500':
        file_name = f'../data/vehicle_{result}_1500.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([timeslot[i], average[i], distance[i]])

    if distance[i] == '2000':
        file_name = f'../data/vehicle_{result}_2000.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([timeslot[i], average[i], distance[i]])
