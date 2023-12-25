    
import csv
import sys
import statistics

import matplotlib.pyplot as plt

def statistic_difference_v1_v2(num):    
    csv_file_path1 = f'../data/data_v1_{num}.csv'
    csv_file_path2 = f'../data/data_v2_{num}.csv'

    timeslot1 = []
    begin1 = []
    end1 = [] 
    distance1 = []
    numNode1 = []
    nPoD1 = []
    node_participate_pod1 = []
    total_node = []
    distance_average1 = []   
    total_coin1 = []
    coin_earning1 = []

    # Read file 
    with open(csv_file_path1, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot1.append(row[0])
            begin1.append(row[1])
            end1.append(row[2])
            distance1.append(row[3])
            numNode1.append(row[4])
            total_node.append(row[5])
            nPoD1.append(row[6])
            node_participate_pod1.append(row[7])
            distance_average1.append(row[8])
            total_coin1.append(row[9])
            coin_earning1.append(row[10])

    timeslot2 = []
    begin2 = []
    end2 = [] 
    distance2 = []
    numNode2 = []
    nPoD2 = []
    node_participate_pod2 = []
    total_node2 = []
    distance_average2 = []   
    total_coin2 = []
    coin_earning2 = []

    with open(csv_file_path2, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot2.append(row[0])
            begin2.append(row[1])
            end2.append(row[2])
            distance2.append(row[3])
            numNode2.append(row[4])
            total_node2.append(row[5])
            nPoD2.append(row[6])
            node_participate_pod2.append(row[7])
            distance_average2.append(row[8])
            total_coin2.append(row[9])
            coin_earning2.append(row[10])

    print(nPoD1)
    print("___________________")
    print(nPoD2)
    print("___________________")
    print(total_node)

    # Extracting relevant data for the first 10 points
    labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    values1 = [int(x) for x in nPoD1[1:11]]
    values2 = [int(x) for x in nPoD2[1:11]]
    values3 = [int(x) for x in node_participate_pod1[1:11]]
    values4 = [int(x) for x in total_node[1:11]]

    # Plotting the bar chart
    bar_width = 0.2
    index = range(len(labels))

    fig, ax = plt.subplots()
    bar1 = ax.bar(index, values1, bar_width, label="Vehicle receving coin by comparing coin")
    bar2 = ax.bar([i + bar_width for i in index], values2, bar_width, label="Vehicle receving coin by comparing distance")
    bar3 = ax.bar([i + 2 * bar_width for i in index], values3, bar_width, label="Vehicle participated in proof of driving")
    bar4 = ax.bar([i + 3 * bar_width for i in index], values4, bar_width, label="Total vehicles")

    # Adding labels and title
    ax.set_xlabel('Time (h)')
    ax.set_ylabel('Number of vehicles (vehicle)')
    ax.set_title(f'Statistic the number of vehicles in two proof of driving algorithms')
    ax.set_xticks([i + bar_width for i in index])
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()

def statistic_rate_difference_v1_v2(num):
    csv_file_path1 = f'../data/data_v1_{num}.csv'
    csv_file_path2 = f'../data/data_v2_{num}.csv'

    timeslot1 = []
    begin1 = []
    end1 = [] 
    distance1 = []
    numNode1 = []
    nPoD1 = []
    node_participate_pod1 = []
    total_node = []
    distance_average1 = []   
    total_coin1 = []
    coin_earning1 = []

    # Read file 
    with open(csv_file_path1, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot1.append(row[0])
            begin1.append(row[1])
            end1.append(row[2])
            distance1.append(row[3])
            numNode1.append(row[4])
            total_node.append(row[5])
            nPoD1.append(row[6])
            node_participate_pod1.append(row[7])
            distance_average1.append(row[8])
            total_coin1.append(row[9])
            coin_earning1.append(row[10])

    timeslot2 = []
    begin2 = []
    end2 = [] 
    distance2 = []
    numNode2 = []
    nPoD2 = []
    node_participate_pod2 = []
    total_node2 = []
    distance_average2 = []   
    total_coin2 = []
    coin_earning2 = []

    with open(csv_file_path2, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot2.append(row[0])
            begin2.append(row[1])
            end2.append(row[2])
            distance2.append(row[3])
            numNode2.append(row[4])
            total_node2.append(row[5])
            nPoD2.append(row[6])
            node_participate_pod2.append(row[7])
            distance_average2.append(row[8])
            total_coin2.append(row[9])
            coin_earning2.append(row[10])

    percent1 = 0
    percent2 = 0
    for i in range(1,11):        
        percent1 += int(nPoD1[i] )
        percent2 += int(nPoD2[i])

    percent1 /= 10
    percent2 /= 10

    # Your data
    categories = ['Vehicle filtered by comparing coin', 'Node filtered by comparing distance']
    values = [percent1, percent2]
     # Create a bar chart
    plt.bar(categories, values, color=['blue', 'green'])

    # Add labels and title
    plt.xlabel('Type of algorithms')
    plt.ylabel('Number of vehicles')
    plt.title('Average number of vehicles of 2 algorithms')

    # Show the plot
    plt.show()

statistic_difference_v1_v2(20)
# statistic_rate_difference_v1_v2(20)