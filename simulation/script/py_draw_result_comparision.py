    
import csv
import sys
import statistics

import matplotlib.pyplot as plt


# statistic the number of vehicle satisfy condition of algorithm in 1 hours (v2)
def statistic_difference(num):    
    csv_file_path1 = f'../data/Result_distance_average_algorithm/data_v2_{num}_dis_ave.csv'

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
    
    # Extracting relevant data for the first 10 points
    x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    y_labels = [0, 5, 10, 15, 20]
    values1 = [int(x) for x in nPoD1[1:11]]
    values2 = [int(x) for x in node_participate_pod1[1:11]]
    values3 = [int(x) for x in total_node[1:11]]

    # Plotting the bar chart
    width = 0.2
    index = range(len(x_labels))

    fig, ax = plt.subplots()
    
    ax.bar(index, values1, width, label="Vehicle received coin")
    ax.bar([i + width for i in index], values2, width, label="Vehicles satisfy conditions")
    ax.bar([i + 2 * width for i in index], values3, width, label="Total vehicles")


    # Adding labels and title
    ax.set_xlabel('Time (h)')
    ax.set_ylabel('Number of vehicles')
    ax.set_xticks([i + width for i in index])
    ax.set_xticklabels(x_labels)
    ax.set_yticks(y_labels)

    # ax.set_title(f'Average distance')
    ax.legend()

    plt.show()

# statistic the number of vehicle satisfy condition of algorithm in 3 hours (v2)
def statistic_difference_v3(num):    
    csv_file_path1 = f'../data/Result_accumulate_distance/data_v3_{num}.csv'

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
    
    # Extracting relevant data for the first 10 points
    x_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    y_labels = [0, 5, 10, 15, 20]
    values1 = [int(x) for x in nPoD1[1:11]]
    values2 = [int(x) for x in node_participate_pod1[1:11]]
    values3 = [int(x) for x in total_node[1:11]]

    # Plotting the bar chart
    width = 0.2
    index = range(len(x_labels))

    fig, ax = plt.subplots()
    
    ax.bar(index, values1, width, label="Vehicle received coin")
    ax.bar([i + width for i in index], values2, width, label="Vehicles satisfy conditions")
    ax.bar([i + 2 * width for i in index], values3, width, label="Total vehicles")


    # Adding labels and title
    ax.set_xlabel('Time (h)')
    ax.set_ylabel('Number of vehicles')
    ax.set_xticks([i + width for i in index])
    ax.set_xticklabels(x_labels)
    ax.set_yticks(y_labels)

    # ax.set_title(f'Average distance')
    ax.legend()

    plt.show()


# Statistic the fixed threshold of v1
def statistic_rate_difference(num):
    csv_file_path1 = f'../data/Result_coin_average_algorithm/data_v1_{num}_25000.csv'
    csv_file_path2 = f'../data/Result_coin_average_algorithm/data_v1_{num}_30000.csv'
    csv_file_path3 = f'../data/Result_coin_average_algorithm/data_v1_{num}_35000.csv'
    csv_file_path4 = f'../data/Result_coin_average_algorithm/data_v1_{num}_40000.csv'

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
    total_node = []
    distance_average2 = []   
    total_coin2 = []
    coin_earning2 = []

    # Read file 
    with open(csv_file_path2, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot2.append(row[0])
            begin2.append(row[1])
            end2.append(row[2])
            distance2.append(row[3])
            numNode2.append(row[4])
            total_node.append(row[5])
            nPoD2.append(row[6])
            node_participate_pod2.append(row[7])
            distance_average2.append(row[8])
            total_coin2.append(row[9])
            coin_earning2.append(row[10])

    timeslot3 = []
    begin3 = []
    end3 = [] 
    distance3 = []
    numNode3 = []
    nPoD3 = []
    node_participate_pod3 = []
    total_node = []
    distance_average3 = []   
    total_coin3 = []
    coin_earning3 = []

    # Read file 
    with open(csv_file_path3, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot3.append(row[0])
            begin3.append(row[1])
            end3.append(row[2])
            distance3.append(row[3])
            numNode3.append(row[4])
            total_node.append(row[5])
            nPoD3.append(row[6])
            node_participate_pod3.append(row[7])
            distance_average3.append(row[8])
            total_coin3.append(row[9])
            coin_earning3.append(row[10])

    timeslot4 = []
    begin4 = []
    end4 = [] 
    distance4 = []
    numNode4 = []
    nPoD4 = []
    node_participate_pod4 = []
    total_node4 = []
    distance_average4 = []   
    total_coin4 = []
    coin_earning4 = []

    # Read file 
    with open(csv_file_path4, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot4.append(row[0])
            begin4.append(row[1])
            end4.append(row[2])
            distance4.append(row[3])
            numNode4.append(row[4])
            total_node4.append(row[5])
            nPoD4.append(row[6])
            node_participate_pod4.append(row[7])
            distance_average4.append(row[8])
            total_coin4.append(row[9])
            coin_earning4.append(row[10])

    percent1 = 0
    percent2 = 0
    percent3 = 0
    percent4 = 0
    for i in range(1,11):        
        percent1 += int(nPoD1[i]) / int(node_participate_pod1[i])
        percent2 += int(nPoD2[i]) / int(node_participate_pod2[i])
        if (int(node_participate_pod3[i]) != 0):
            percent3 += int(nPoD3[i]) / int(node_participate_pod3[i])
        if (int(node_participate_pod4[i]) != 0):
            percent4 += int(nPoD4[i]) / int(node_participate_pod4[i])
  
    average1 = (percent1 / 10) * 100
    average2 = (percent2 / 10) * 100
    average3 = (percent3 / 10) * 100
    average4 = (percent4 / 10) * 100

    # Your data
    categories = ["25000", "30000", "35000", "40000"]
    values = [average1, average2, average3, average4]
     # Create a bar chart
    plt.bar(categories, values, color=['blue', 'blue', 'blue', 'blue'])

    yticks = [0, 20, 40, 60, 80, 100]
    plt.yticks(yticks)
    # Add labels and title
    plt.xlabel('Threshold (m)')
    plt.ylabel('Percentage (%)')

    # Show the plot
    plt.show()

# Statistic the difference of fixed and dynamic threshold of v1 and v2
def statistic_rate_difference_dynamic(num):
    csv_file_path1 = f'../data/Result_distance_average_algorithm/data_v2_{num}_25000.csv'
    csv_file_path2 = f'../data/Result_distance_average_algorithm/data_v2_{num}_30000.csv'
    csv_file_path3 = f'../data/Result_distance_average_algorithm/data_v2_{num}_35000.csv'
    csv_file_path4 = f'../data/Result_distance_average_algorithm/data_v2_{num}_40000.csv'
    csv_file_path5 = f'../data/Result_distance_average_algorithm/data_v2_{num}_dis_ave.csv'

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
    total_node = []
    distance_average2 = []   
    total_coin2 = []
    coin_earning2 = []

    # Read file 
    with open(csv_file_path2, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot2.append(row[0])
            begin2.append(row[1])
            end2.append(row[2])
            distance2.append(row[3])
            numNode2.append(row[4])
            total_node.append(row[5])
            nPoD2.append(row[6])
            node_participate_pod2.append(row[7])
            distance_average2.append(row[8])
            total_coin2.append(row[9])
            coin_earning2.append(row[10])

    timeslot3 = []
    begin3 = []
    end3 = [] 
    distance3 = []
    numNode3 = []
    nPoD3 = []
    node_participate_pod3 = []
    total_node = []
    distance_average3 = []   
    total_coin3 = []
    coin_earning3 = []

    # Read file 
    with open(csv_file_path3, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot3.append(row[0])
            begin3.append(row[1])
            end3.append(row[2])
            distance3.append(row[3])
            numNode3.append(row[4])
            total_node.append(row[5])
            nPoD3.append(row[6])
            node_participate_pod3.append(row[7])
            distance_average3.append(row[8])
            total_coin3.append(row[9])
            coin_earning3.append(row[10])

    timeslot4 = []
    begin4 = []
    end4 = [] 
    distance4 = []
    numNode4 = []
    nPoD4 = []
    node_participate_pod4 = []
    total_node4 = []
    distance_average4 = []   
    total_coin4 = []
    coin_earning4 = []

    # Read file 
    with open(csv_file_path4, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot4.append(row[0])
            begin4.append(row[1])
            end4.append(row[2])
            distance4.append(row[3])
            numNode4.append(row[4])
            total_node4.append(row[5])
            nPoD4.append(row[6])
            node_participate_pod4.append(row[7])
            distance_average4.append(row[8])
            total_coin4.append(row[9])
            coin_earning4.append(row[10])

    timeslot5 = []
    begin5 = []
    end5 = [] 
    distance5 = []
    numNode5 = []
    nPoD5 = []
    node_participate_pod5 = []
    total_node5 = []
    distance_average5 = []   
    total_coin5 = []
    coin_earning5 = []

    with open(csv_file_path5, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot5.append(row[0])
            begin5.append(row[1])
            end5.append(row[2])
            distance5.append(row[3])
            numNode5.append(row[4])
            total_node5.append(row[5])
            nPoD5.append(row[6])
            node_participate_pod5.append(row[7])
            distance_average5.append(row[8])
            total_coin5.append(row[9])
            coin_earning5.append(row[10])

    percent1 = 0
    percent2 = 0
    percent3 = 0
    percent4 = 0
    percent5 = 0
    for i in range(1,11):        
        percent1 += int(nPoD1[i]) / int(node_participate_pod1[i])
        percent2 += int(nPoD2[i]) / int(node_participate_pod2[i])
        if (int(node_participate_pod3[i]) != 0):
            percent3 += int(nPoD3[i]) / int(node_participate_pod3[i])
        if (int(node_participate_pod4[i]) != 0):
            percent4 += int(nPoD4[i]) / int(node_participate_pod4[i])
        percent5 += int(nPoD5[i]) / int(node_participate_pod5[i])

    print(percent5)
    average1 = (percent1 / 10) * 100
    average2 = (percent2 / 10) * 100
    average3 = (percent3 / 10) * 100
    average4 = (percent4 / 10) * 100
    average5 = (percent5 / 10) * 100

    # Your data
    categories = ["25000", "30000", "35000", "40000", "Dynamic"]
    values = [average1, average2, average3, average4, average5]
     # Create a bar chart
    plt.bar(categories, values, color=['blue', 'blue', 'blue', 'blue', 'green'])

    yticks = [0, 20, 40, 60, 80, 100]
    plt.yticks(yticks)
    # Add labels and title
    plt.xlabel('Threshold (m)')
    plt.ylabel('Percentage (%)')

    # Show the plot
    plt.show()

# Statistic the number of timeslots does not have vehicles 
def statistic_timeslot_not_have_vehicles(num):    
    csv_file_path1 = f'../data/Result_distance_average_algorithm/data_v2_{num}_25000.csv'
    csv_file_path2 = f'../data/Result_distance_average_algorithm/data_v2_{num}_30000.csv'
    csv_file_path3 = f'../data/Result_distance_average_algorithm/data_v2_{num}_35000.csv'
    csv_file_path4 = f'../data/Result_distance_average_algorithm/data_v2_{num}_40000.csv'
    csv_file_path5 = f'../data/Result_distance_average_algorithm/data_v2_{num}_dis_ave.csv'

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
    total_node = []
    distance_average2 = []   
    total_coin2 = []
    coin_earning2 = []

    # Read file 
    with open(csv_file_path2, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot2.append(row[0])
            begin2.append(row[1])
            end2.append(row[2])
            distance2.append(row[3])
            numNode2.append(row[4])
            total_node.append(row[5])
            nPoD2.append(row[6])
            node_participate_pod2.append(row[7])
            distance_average2.append(row[8])
            total_coin2.append(row[9])
            coin_earning2.append(row[10])

    timeslot3 = []
    begin3 = []
    end3 = [] 
    distance3 = []
    numNode3 = []
    nPoD3 = []
    node_participate_pod3 = []
    total_node = []
    distance_average3 = []   
    total_coin3 = []
    coin_earning3 = []

    # Read file 
    with open(csv_file_path3, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot3.append(row[0])
            begin3.append(row[1])
            end3.append(row[2])
            distance3.append(row[3])
            numNode3.append(row[4])
            total_node.append(row[5])
            nPoD3.append(row[6])
            node_participate_pod3.append(row[7])
            distance_average3.append(row[8])
            total_coin3.append(row[9])
            coin_earning3.append(row[10])

    timeslot4 = []
    begin4 = []
    end4 = [] 
    distance4 = []
    numNode4 = []
    nPoD4 = []
    node_participate_pod4 = []
    total_node = []
    distance_average4 = []   
    total_coin4 = []
    coin_earning4 = []

    # Read file 
    with open(csv_file_path4, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot4.append(row[0])
            begin4.append(row[1])
            end4.append(row[2])
            distance4.append(row[3])
            numNode4.append(row[4])
            total_node.append(row[5])
            nPoD4.append(row[6])
            node_participate_pod4.append(row[7])
            distance_average4.append(row[8])
            total_coin4.append(row[9])
            coin_earning4.append(row[10])

    timeslot5 = []
    begin5 = []
    end5 = [] 
    distance5 = []
    numNode5 = []
    nPoD5 = []
    node_participate_pod5 = []
    total_node5 = []
    distance_average5 = []   
    total_coin5 = []
    coin_earning5 = []

    with open(csv_file_path5, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot5.append(row[0])
            begin5.append(row[1])
            end5.append(row[2])
            distance5.append(row[3])
            numNode5.append(row[4])
            total_node5.append(row[5])
            nPoD5.append(row[6])
            node_participate_pod5.append(row[7])
            distance_average5.append(row[8])
            total_coin5.append(row[9])
            coin_earning5.append(row[10])

    percent1 = []
    percent2 = []
    percent3 = []
    percent4 = []
    percent5 = []
    for i in range(1, 11):
        percent1.append(int(nPoD1[i]) / int(node_participate_pod1[i]))
        percent2.append(int(nPoD2[i]) / int(node_participate_pod2[i]))
        if(int(node_participate_pod3[i]) != 0):
            percent3.append(int(nPoD3[i]) / int(node_participate_pod3[i]))
        else:
            percent3.append(0)
        if(int(node_participate_pod4[i]) != 0):
            percent4.append(int(nPoD4[i]) / int(node_participate_pod4[i]))
        else:
            percent4.append(0)
        percent5.append(int(nPoD5[i]) / int(total_node5[i]))

    count1 = percent1.count(0)
    print(f"Number of timeslot have all vehicles: {count1}")

    count2 = percent2.count(0)
    print(f"Number of timeslot have all vehicles: {count2}")

    count3 = percent3.count(0)
    print(f"Number of timeslot have all vehicles: {count3}")

    count4 = percent4.count(0)
    print(f"Number of timeslot have all vehicles: {count4}")

    count5 = percent5.count(0)
    print(f"Number of timeslot have all vehicles: {count5}")

    categories = ["25000", "30000", "35000", "40000", "Dynamic"]
    values = [count1*10, count2*10, count3*10, count4*10, count5*10]
     # Create a bar chart
    plt.bar(categories, values, color=['blue', 'blue', 'blue', 'blue', 'green'])

    yticks = [0, 20, 40, 60, 80, 100]

    plt.yticks(yticks)
    # Add labels and title
    plt.xlabel('Threshold (m)')
    plt.ylabel('Timeslot (%)')

    # Show the plot
    plt.show()

# Statistic the number of timeslots have all vehicels
def statistic_timeslot_have_all_vehicles(num):    
    csv_file_path1 = f'../data/Result_distance_average_algorithm/data_v2_{num}_25000.csv'
    csv_file_path2 = f'../data/Result_distance_average_algorithm/data_v2_{num}_30000.csv'
    csv_file_path3 = f'../data/Result_distance_average_algorithm/data_v2_{num}_35000.csv'
    csv_file_path4 = f'../data/Result_distance_average_algorithm/data_v2_{num}_40000.csv'
    csv_file_path5 = f'../data/Result_distance_average_algorithm/data_v2_{num}_dis_ave.csv'

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
    total_node = []
    distance_average2 = []   
    total_coin2 = []
    coin_earning2 = []

    # Read file 
    with open(csv_file_path2, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot2.append(row[0])
            begin2.append(row[1])
            end2.append(row[2])
            distance2.append(row[3])
            numNode2.append(row[4])
            total_node.append(row[5])
            nPoD2.append(row[6])
            node_participate_pod2.append(row[7])
            distance_average2.append(row[8])
            total_coin2.append(row[9])
            coin_earning2.append(row[10])

    timeslot3 = []
    begin3 = []
    end3 = [] 
    distance3 = []
    numNode3 = []
    nPoD3 = []
    node_participate_pod3 = []
    total_node = []
    distance_average3 = []   
    total_coin3 = []
    coin_earning3 = []

    # Read file 
    with open(csv_file_path3, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot3.append(row[0])
            begin3.append(row[1])
            end3.append(row[2])
            distance3.append(row[3])
            numNode3.append(row[4])
            total_node.append(row[5])
            nPoD3.append(row[6])
            node_participate_pod3.append(row[7])
            distance_average3.append(row[8])
            total_coin3.append(row[9])
            coin_earning3.append(row[10])

    timeslot4 = []
    begin4 = []
    end4 = [] 
    distance4 = []
    numNode4 = []
    nPoD4 = []
    node_participate_pod4 = []
    total_node = []
    distance_average4 = []   
    total_coin4 = []
    coin_earning4 = []

    # Read file 
    with open(csv_file_path4, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot4.append(row[0])
            begin4.append(row[1])
            end4.append(row[2])
            distance4.append(row[3])
            numNode4.append(row[4])
            total_node.append(row[5])
            nPoD4.append(row[6])
            node_participate_pod4.append(row[7])
            distance_average4.append(row[8])
            total_coin4.append(row[9])
            coin_earning4.append(row[10])

    timeslot5 = []
    begin5 = []
    end5 = [] 
    distance5 = []
    numNode5 = []
    nPoD5 = []
    node_participate_pod5 = []
    total_node5 = []
    distance_average5 = []   
    total_coin5 = []
    coin_earning5 = []

    with open(csv_file_path5, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            timeslot5.append(row[0])
            begin5.append(row[1])
            end5.append(row[2])
            distance5.append(row[3])
            numNode5.append(row[4])
            total_node5.append(row[5])
            nPoD5.append(row[6])
            node_participate_pod5.append(row[7])
            distance_average5.append(row[8])
            total_coin5.append(row[9])
            coin_earning5.append(row[10])

    percent1 = []
    percent2 = []
    percent3 = []
    percent4 = []
    percent5 = []
    for i in range(1, 11):
        percent1.append(int(nPoD1[i]) / int(node_participate_pod1[i]))
        percent2.append(int(nPoD2[i]) / int(node_participate_pod2[i]))
        if(int(node_participate_pod3[i]) != 0):
            percent3.append(int(nPoD3[i]) / int(node_participate_pod3[i]))
        else:
            percent3.append(0)
        percent5.append(int(nPoD5[i]) / int(total_node5[i]))
        if(int(node_participate_pod4[i]) != 0):
            percent4.append(int(nPoD4[i]) / int(node_participate_pod4[i]))
        else:
            percent4.append(0)

    count1 = percent1.count(1)
    print(f"Number of timeslot have all vehicles: {count1}")

    count2 = percent2.count(1)
    print(f"Number of timeslot have all vehicles: {count2}")

    count3 = percent3.count(1)
    print(f"Number of timeslot have all vehicles: {count3}")

    count4 = percent4.count(1)
    print(f"Number of timeslot have all vehicles: {count4}")

    count5 = percent5.count(1)
    print(f"Number of timeslot have all vehicles: {count5}")

    categories = ["25000", "30000", "35000", "40000", "Dynamic"]
    values = [count1*10, count2*10, count3*10, count4*10, count5*10]
     # Create a bar chart
    plt.bar(categories, values, color=['blue', 'blue', 'blue', 'blue', 'green'])

    yticks = [0, 20, 40, 60, 80, 100]

    plt.yticks(yticks)
    # Add labels and title
    plt.xlabel('Threshold (m)')
    plt.ylabel('Timeslot (%)')

    # Show the plot
    plt.show()


# Statistic the number of timeslots have all vehicels
# statistic_timeslot_have_all_vehicles(20)

# Statistic the number of timeslots does not have vehicles 
# statistic_timeslot_not_have_vehicles(20)

statistic_difference_v3(20)
# statistic_rate_difference(20)
# statistic_rate_difference_dynamic(20)