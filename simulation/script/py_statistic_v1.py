import csv
import sys
import statistics

def statistic(num):
    csv_file_path = f'../data/data_v1_{num}.csv'

    timeslot = []
    begin = []
    end = [] 
    distance = []
    numNode = []
    nPoD = []
    node_participate_pod = []
    total_node = []
    distance_average = []   
    total_coin = []
    coin_earning = []

    # Read file 
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot.append(row[0])
            begin.append(row[1])
            end.append(row[2])
            distance.append(row[3])
            numNode.append(row[4])
            total_node.append(row[5])
            nPoD.append(row[6])
            node_participate_pod.append(row[7])
            distance_average.append(row[8])
            total_coin.append(row[9])
            coin_earning.append(row[10])

    percentages = []
    tmp_timeslot = []
    tmp_distance = []
    tmp_distance_average = []
    tmp_total_coin = []
    tmp_coin_earning = []
    
    # Ignore a first element
    for i in range(1, len(distance)):
        percent = 0
        # if(int(node_participate_pod[i]) != 0):
        percent = int(nPoD[i]) / int(total_node[i]) 
        percentages.append(percent)
        tmp_timeslot.append(timeslot[i])
        tmp_distance.append(distance[i])
        tmp_distance_average.append(distance_average[i])
        tmp_total_coin.append(total_coin[i])
        tmp_coin_earning.append(coin_earning[i])

    timeslot = []
    average = []
    distance = []
    times = 0

    # Calculate average of a scenario (90 vehicles => 110 vehilces)
    for j in range(1, 12):
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
    percentage_distance = []
    b = 0
    e = 10
    for i in range(1, 12):
        d = []
        for j in range(b, e):
            d.append(percentages[j])    
        percentage_distance.append(d)
        b+=10
        e+=10

    std_dev_list = []
    for i in range(len(percentage_distance)):
        std_dev_list.append(statistics.stdev(percentage_distance[i]))

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
        file_name = f'../data/v_{result}_d_{distance[i]}_v1.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([timeslot[i], average[i], std_dev_list[i], distance[i]])

def loop_statistic():
    numVehicles = 90
    for j in range(1, 6):
        for i in range(1,22):
            statistic(numVehicles)
            numVehicles += 1
        numVehicles+=79

if __name__ == '__main__':
    loop_statistic()