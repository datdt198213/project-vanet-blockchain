import json    
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

# statistic the number of vehicle satisfy condition of algorithm in 1 hours (v3)
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

def statistic_difficulty():
    file1 = "../data/Result_coin_average_algorithm/data_v1_20_coin_ave.csv"
    file2 = "../data/Result_distance_average_algorithm/data_v2_20_dis_ave.csv"
    file3 = "../data/Result_accumulate_distance/data_v3_20.csv"
    file4 = "../data/Result_accumulate_distance/data_v4_20.csv"
    
    # Get difficulty
    dif1 = get_average_difficulty(file1)
    dif2 = get_average_difficulty(file2)
    dif3 = get_average_difficulty(file3)
    dif4 = get_average_difficulty(file4)

    categories = ["Coin average", "Distance average", "Accumulate distance", "Total accumulated distance"]
    values = [dif1*100, dif2*100, dif3*100, dif4*100]

    plt.bar(categories, values, color=['blue', 'green', 'orange', 'red'])

    yticks = [0, 20, 40, 60, 80, 100]

    plt.yticks(yticks)
    # Add labels and title
    plt.xlabel('Threshold (m)')
    plt.ylabel('Difficulty (%)')

    # Show the plot
    plt.show()

    # print(dif1, dif2, dif3, dif4)

# Get average difficulty of senarios
def get_average_difficulty(csv_file_path):
    nPoD = []
    node_participate_pod = []

    # Read file 
    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            nPoD.append(row[6])
            node_participate_pod.append(row[7])

    percentages = []
    
    print(nPoD)
    ave = 0
    # Ignore a first element
    for i in range(1, len(nPoD)):
        
        percentages.append(int(nPoD[i]) / int(node_participate_pod[i]))
        ave += percentages[i-1]
    ave /= len(percentages)
    
    return ave

# statistic_difficulty()

# Lấy ra tỉ lệ (số xe nhận coin / tổng số xe)
def get_multi_average_winner(csv_file):
    # 60 dữ liệu 10p
    # 30 dữ liệu 20p
    # 20 dữ liệu 30p
    # 15 dữ liệu 40p
    # 12 dữ liệu 50p
    # 10 dữ liệu 60p

    nPoD = []
    total_node = []

    # Read file 
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            nPoD.append(row[6])
            total_node.append(row[5])

    percentages = []
    temp = 0
    ave = []
    
    # 600s
    for i in range(1, 61):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
        temp += percentages[i-1]
    
    temp/= 60
    ave.append(temp)

    temp = 0
    # 1200s
    for i in range(61, 91):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
        temp += percentages[i-1]

    temp /= 30
    ave.append(temp)

    temp = 0
    # 1800s
    for i in range(91, 111):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
        temp += percentages[i-1]

    temp /= 20
    ave.append(temp)

    # 2400
    temp = 0
    for i in range(111, 126):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
        temp += percentages[i-1]

    temp /= 15
    ave.append(temp)

    # 3000
    temp = 0
    for i in range(126, 138):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
        temp += percentages[i-1]

    temp /= 12
    ave.append(temp)

    # 3600
    temp = 0
    for i in range(137, 147):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
        temp += percentages[i-1]
    temp /= 10
    ave.append(temp)

    return ave

def statistic_difficulty_time(file):
    ave = get_multi_average_winner(file)

    categories = ["600", "1200", "1800", "2400", "3000","3600"]
    values = [ave[0]*100, ave[1]*100, ave[2]*100, ave[3]*100, ave[4]*100, ave[5]*100]

    plt.bar(categories, values, color=['blue', 'green', 'orange', 'red', "black", 'gray'])

    for i in range(len(categories)):
        plt.text(i, values[i] + 1, str(round(values[i], 1)), ha='center')

    yticks = [0, 20, 40, 60, 80, 100]

    plt.yticks(yticks)
    # Add labels and title
    plt.xlabel('Time (s)')
    plt.ylabel('Winner percentage (%)')

    # Show the plot
    plt.show()




def line_graph_difficulty():
    file1 = "../data/Result_consider_time/data_v5_20.csv"
    file2 = "../data/Result_consider_time/data_v6_20.csv"
    file3 = "../data/Result_consider_time/data_v7_20.csv"
    file4 = "../data/Result_consider_time/data_v8_20.csv"
    ave1 = get_multi_average_winner(file1)
    ave2 = get_multi_average_winner(file2)
    ave3 = get_multi_average_winner(file3)
    ave4 = get_multi_average_winner(file4)

    new_x_values = [600, 1200, 1800, 2400, 3000, 3600]
    plt.plot(new_x_values, ave1, label='Coin trung bình')
    plt.plot(new_x_values, ave2, label='Không có tích lũy')
    plt.plot(new_x_values, ave3, label='Có tích lũy, ave = 1 round')
    plt.plot(new_x_values, ave4, label='Có tích lũy ave = nhiều round')

    plt.title('Tỉ lệ Winner của 4 trường hợp')
    plt.xlabel('Time (s)')
    plt.xticks(new_x_values)
    plt.ylabel('Winner percentage (%)')
    plt.legend()
    plt.show()

def get_min_max_ave(percentages):
    min_value = float('inf')  # Khởi tạo min_value là vô cùng
    max_value = float('-inf') # Khởi tạo max_value là âm vô cùng
    for percentage in percentages:
        if percentage < min_value:
            min_value = percentage
        if percentage > max_value:
            max_value = percentage

    ave_value = (min_value + max_value) / 2
    return min_value, max_value, ave_value

def statistic_min_max_ave(csv_file):
    
    max_arr = []
    min_arr = []
    ave_arr = []

    
    algorithm = ''
    if ('v5' in csv_file):
        algorithm = '1'
    if ('v6' in csv_file):
        algorithm = '2'
    if ('v7' in csv_file):
        algorithm = '3'
    if ('v8' in csv_file):
        algorithm = '4'
    
    nPoD = []
    total_node = []

    # Read file 
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            nPoD.append(row[6])
            total_node.append(row[5])

    
    # 600s
    percentages = []
    for i in range(1, 61):
        percentages.append(int(nPoD[i]) / int(total_node[i]))

    min, max, ave = get_min_max_ave(percentages)
    min_arr.append(min)
    max_arr.append(max)
    ave_arr.append(ave)

    # 1200s
    percentages = []
    for i in range(61, 91):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    min, max, ave = get_min_max_ave(percentages)
    min_arr.append(min)
    max_arr.append(max)
    ave_arr.append(ave)

    # 1800s
    percentages = []
    for i in range(91, 111):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    min, max, ave = get_min_max_ave(percentages)
    min_arr.append(min)
    max_arr.append(max)
    ave_arr.append(ave)

    # 2400
    percentages = []
    for i in range(111, 126):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    min, max, ave = get_min_max_ave(percentages)
    min_arr.append(min)
    max_arr.append(max)
    ave_arr.append(ave)

    # 3000
    percentages = []
    for i in range(126, 138):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    min, max, ave = get_min_max_ave(percentages)
    min_arr.append(min)
    max_arr.append(max)
    ave_arr.append(ave)
   
    # 3600
    percentages = []
    for i in range(137, 147):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    min, max, ave = get_min_max_ave(percentages)
    min_arr.append(min)
    max_arr.append(max)
    ave_arr.append(ave)

    print(f"Min: {min_arr} \nMax: {max_arr} \nAve: {ave_arr}")

    # Dữ liệu
    time_intervals = ['1', '2', '3', '4', '5', '6']

    # Vẽ biểu đồ
    plt.figure(figsize=(10, 6))
    plt.plot(time_intervals, min_arr, label='Min')
    plt.plot(time_intervals, max_arr, label='Max')
    plt.plot(time_intervals, ave_arr, label='Ave')
    plt.xlabel('Time Intervals')
    plt.ylabel('Values')
    plt.title('Min, Max, and Ave Values over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

    # for i in range(0, len(max) - 1):
    #     a = (float(max[i]) + float(min[i])) / 2
    #     ave.append(a)

def draw_standard_deviation(csv_file, csv_file2):
    mean  = []
    sd = []
    time_intervals = ['600', '1200', '1800', '2400', '3000', '3600', 'Dynamic']

    nPoD = []
    total_node = []

    # Read file 
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            nPoD.append(row[6])
            total_node.append(row[5])

    percentages = []
    
    # 600s
    for i in range(1, 61):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    mean.append(statistics.mean(percentages)) 
    sd.append(statistics.stdev(percentages))

    # 1200s
    percentages = []
    for i in range(61, 91):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    mean.append(statistics.mean(percentages)) 
    sd.append(statistics.stdev(percentages))

    # 1800s
    percentages = []
    for i in range(91, 111):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    mean.append(statistics.mean(percentages)) 
    sd.append(statistics.stdev(percentages))

    # 2400
    percentages = []
    for i in range(111, 126):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    mean.append(statistics.mean(percentages)) 
    sd.append(statistics.stdev(percentages))

    # 3000
    percentages = []
    for i in range(126, 138):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    mean.append(statistics.mean(percentages)) 
    sd.append(statistics.stdev(percentages))

    # 3600
    percentages = []
    for i in range(137, 147):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    mean.append(statistics.mean(percentages)) 
    sd.append(statistics.stdev(percentages))

    # print(mean, sd)
    # Dynamic

    nPoD = []
    total_node = []
    # read_file
    with open(csv_file2, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            nPoD.append(row[6])
            total_node.append(row[5])

    percentages = []
    for i in range(1, len(nPoD)):
        percentages.append(int(nPoD[i]) / int(total_node[i]))
    mean.append(statistics.mean(percentages)) 
    sd.append(statistics.stdev(percentages))
    print(mean, sd)


    algorithm = ''
    if ('v5' in csv_file):
        algorithm = '1'
    if ('v6' in csv_file):
        algorithm = '2'
    if ('v7' in csv_file):
        algorithm = '3'
    if ('v8' in csv_file):
        algorithm = '4'

    plt.figure(figsize=(10, 6))
    plt.boxplot([[mean[0], sd[0]], [mean[1], sd[1]], [mean[2], sd[2]], [mean[3], sd[3]], [mean[4], sd[4]], [mean[5], sd[5]], [mean[6], sd[6]]], labels=time_intervals)
    plt.ylabel('Winner percentage')
    plt.title(f'Standard deviation thuật toán {algorithm}')
    plt.grid(True)
    plt.show()
    
    return mean, sd

def main():
    file = "../data/Result_consider_time/data_v8_20.csv"
    file2 = "../data/Result_consider_time/data_v9_20.csv"
    draw_standard_deviation(file, file2)
    
    
    # statistic_difficulty_time(file)
    
    # line_graph_difficulty()
    # Statistic the number of timeslots have all vehicels
    # statistic_timeslot_have_all_vehicles(20)

    # Statistic the number of timeslots does not have vehicles 
    # statistic_timeslot_not_have_vehicles(20)

    # statistic_difference(20)
    # statistic_difference_v3(20)
    # statistic_rate_difference(20)
    # statistic_rate_difference_dynamic(20)
    # statistic_min_max_ave(file)

# main()

with open('../data/Result_problem_statement/data_v1_3_20_0.1AverageDistance_Not_Parse_Int.json', 'r') as file:
    # Load the JSON data
    vehicles = json.load(file)

id_list = []
time_list = []
distance_list = []
mining_list = []
average_distance = 0

timeslot1 = 3600    # Data from 0 to 3600s
timeslot2 = 7200    # Data from 3600s to 7200s
timeslot3 = 10800   # Data from 7200s to 10800s
timeslot4 = 14400   # Data from 10800s to 14400s
timeslot5 = 18000   # Data from 14400s to 18000s
timeslot6 = 21600   # Data from 18000s to 21600s
timeslot7 = 25200   # Data from 21600s to 25200s
timeslot8 = 28800   # Data from 25200s to 28800s
timeslot9 = 32400   # Data from 28800s to 32400s
timeslot10 = 36000  # Data from 32400s to 36000s

for i in range(0, len(vehicles)):
    if (int(vehicles[i]['time']) == timeslot1):
        id = vehicles[i]['id']
        time = vehicles[i]['time']
        distance = vehicles[i]['distance']
        mining = vehicles[i]['mining']
        average_distance = vehicles[i]['averageDistance']
        id_list.append(id)
        time_list.append(time)
        distance_list.append(distance)
        mining_list.append(mining)

    
colors = ['red' if not mining else 'green' for mining in mining_list]
print(average_distance)
plt.bar(id_list, distance_list, color=colors)
plt.axhline(y=average_distance, color='blue', linestyle='--', label='Average Distance')


# Adding labels and title
plt.xlabel('ID')
plt.ylabel('Distance')
# plt.title('Time = 600')

# Custom legend
legend_labels = ['Not Mining', 'Mining', 'Average Distance']
colors_legend = ['red', 'green', 'blue']
legend_patches = [plt.Line2D([0], [0], color=color, label=label, linewidth=3) for label, color in zip(legend_labels, colors_legend)]
plt.legend(handles=legend_patches)

# Display the plot
plt.show()