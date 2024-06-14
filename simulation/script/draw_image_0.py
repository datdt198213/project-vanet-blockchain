#  Số lượng xe được lọc bởi PoD trong vòng 10h (giống hình trong bài báo)
import random
import numpy as np
import json    
import csv
import sys
import statistics
import matplotlib.pyplot as plt

# Fig 4.1.3 Total wasted distance of 2 algorithm
def main4(file_name1, file_name2):
    
    distance1, total_distance = calculate_distance_not_reward(file_name1)
    distance2, total_distance1 = calculate_distance_not_reward(file_name2)

    # Vẽ với trường hợp chỉ có 2km với 2 thuật toán bài báo + tích lũy
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
    
    values = [int(distance1/1000), int(distance2/1000), int(total_distance/1000)]
    categories = ['Existing algorithm', 'Proposal algorithm', 'Total distance']

    plt.figure(figsize=(10, 6))
    bars = plt.bar(categories, values, color=colors)
    
    # Thêm tiêu đề và nhãn
    # plt.title('Quãng đường chưa được nhận coin')
    plt.ylabel('Distance (km)')

    for i, value in enumerate(values):
        plt.text(i, value + 100, f'{value:,}', ha='center', va='bottom')
    # Hiển thị biểu đồ
    plt.show()
    return

def calculate_distance_not_reward(file_name):
    with open(file_name, 'r') as file:
        vehicles1 = json.load(file)
    
    total_distance = 0
    timeslot1 = 3599.9
    distance1 = 0
    while (timeslot1 <= 36000):
        for i in range(0, len(vehicles1)):
            if ((float(vehicles1[i]['time'])) == timeslot1):
                total_distance += int(vehicles1[i]['distance']) 
                if(vehicles1[i]['mining'] == False):
                    distance1 += int(vehicles1[i]['distance'])
        timeslot1 += 3600
    return distance1, total_distance

# Fig 4.7. Winner small contribution, proposal algorithm
def main5(file_name):
    with open(file_name, 'r') as file:
        vehicles = json.load(file)
     
     # Chuyển đổi dữ liệu thành chuỗi JSON
    # vehicles = json.dumps(data, indent=4)

    # return
    timeslot1 = 3599.9

    num_vehicle = []
    node_satisfy_list = []
    node_small_list = []
    timeslot1 = 3599.9    # Data from 0 to 3600s
    while (timeslot1 <= 36000):
        node_small = 0
        no_vehicle = 0
        node_satisfy = 0
        for i in range(0, len(vehicles)):
            if (float(vehicles[i]['time']) == timeslot1):
                no_vehicle += 1
                if (vehicles[i]['mining'] == True): 
                    node_satisfy += 1
                    if (vehicles[i]['distance'] < vehicles[i]['threshold']):
                        node_small += 1
        # break
        timeslot1 += 3600
        num_vehicle.append(no_vehicle)
        node_small_list.append(node_small)
        node_satisfy_list.append(node_satisfy)
        
    print(node_satisfy_list)
    print(node_small_list)
    print(num_vehicle)
    
    n = len(node_satisfy_list)

    ind = np.arange(n)
    width = 0.2
    fig, ax = plt.subplots(figsize=(10, 6))

    bars1 = ax.bar(ind, node_small_list, width, label='No. winners with small contribution')

    bars2 = ax.bar(ind + width, node_satisfy_list, width, label='No. winners')
    
    bars3 = ax.bar(ind + 2 * width, num_vehicle, width, label='Total vehicles')

    ax.set_xlabel('Time (h)')
    ax.set_ylabel('No. Vehicles')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(['%d' % (i+1) for i in range(n)])
    ax.legend()

    # plt.xticks(x)
    plt.yticks([0,100,200,300])

    # Hiển thị giá trị trên đỉnh mỗi cột
    for bar in bars1:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom')

    for bar in bars2:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom')

    for bar in bars3:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom')

    # Hiển thị biểu đồ
    plt.show()

# Fig 5.3.Thống kê số giá trị coin và distance khác nhau trong mỗi round
def main6(file_coin, file_distance):
    with open(file_coin, 'r') as file:
        vehicle1 = json.load(file)
    
    with open(file_distance, 'r') as file:
        vehicle2 = json.load(file)
    
    statistic_times1 = []
    statistic_times2 = []
    total_vehicle = []
    timeslot = 3599.9
    while (timeslot <= 36000):
        coin_vehicles = []
        distance_vehicles = []
        count_vehicle = 0
        for i in range(0, len(vehicle1)):
            if (vehicle1[i]['time'] == timeslot):
                count_vehicle += 1
                if (vehicle1[i]['coin'] not in coin_vehicles):
                    coin_vehicles.append(vehicle1[i]['coin'])
        
        for i in range(0, len(vehicle2)):
            if (vehicle2[i]['time'] == timeslot):
                if (vehicle2[i]['coin'] not in coin_vehicles):
                    coin_vehicles.append(vehicle2[i]['coin'])
                if (vehicle2[i]['distance'] not in distance_vehicles):
                    distance_vehicles.append(vehicle2[i]['distance'])
        statistic_times1.append(len(coin_vehicles))
        statistic_times2.append(len(distance_vehicles))
        total_vehicle.append(count_vehicle)
        timeslot += 3600

    n = len(total_vehicle)

    ind = np.arange(n)
    width = 0.25
 
    fig, ax = plt.subplots(figsize=(10, 6))
 
    bars1 = ax.bar(ind, statistic_times1, width, label=chr(945)+' in existing algorithm')
 
    bars2 = ax.bar(ind + width, statistic_times2, width, label=chr(945)+' in proposal algorithm')
    bars3 = ax.bar(ind + 2 * width, total_vehicle, width, label=chr(946))
 
    ax.set_xlabel('Time (h)')
    ax.set_ylabel('No. Value')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(['%d' % (i+1) for i in range(n)])
    ax.legend()
 
    # plt.xticks(x)
    plt.yticks([0,100,200,300])
 
    # Hiển thị giá trị trên đỉnh mỗi cột
    for bar in bars1 + bars2 + bars3:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom', fontsize=7)
 
    # Hiển thị biểu đồ
    plt.show()

# Fig 4.1.1. Wasted distance of 2 algorithms
def main7(file1, file2):
    with open(file1, 'r') as file:
        vehicle1 = json.load(file)
    with open(file2, 'r') as file:
        vehicle2 = json.load(file)

    timeslot = 3599.9
    distance_array_1 = [] # Số km thừa trong 1 round của giải thuật existing
    distance_array_2 = [] # Số km thừa trong 1 round của giải thuật đề xuất
    total_distance_list = []

    while (timeslot <= 36000):
        distance_redundant = 0
        total_distance = 0
        for i in range(len(vehicle1)):
            if (vehicle1[i]['time'] == timeslot):
                distance = vehicle1[i]["distance"]
                total_distance += distance
                threshold = vehicle1[i]["threshold"]
                if (vehicle1[i]['mining'] == False):
                    distance_redundant += distance
                else:
                    distance_redundant += distance % threshold
        distance_array_1.append(distance_redundant)
        total_distance_list.append(total_distance)
        
        distance_redundant = 0
        for i in range(len(vehicle2)):
            if (vehicle2[i]['time'] == timeslot):
                distance = vehicle2[i]["distance"]
                threshold = vehicle2[i]["threshold"]
                if (vehicle2[i]["mining"] == False):
                    distance_redundant += distance % threshold 
        distance_array_2.append(distance_redundant)
        timeslot += 3600
    
    for i in range(1, len(total_distance_list)):
        total_distance_list[i] += total_distance_list[i - 1]

    for i in range(1, len(distance_array_1)):
        distance_array_1[i] += distance_array_1[i - 1]
    
    for i in range(0, len(total_distance_list)):
        total_distance_list[i] = int(total_distance_list[i]/1000)

    for i in range(0, len(distance_array_1)):
        distance_array_1[i] = int(distance_array_1[i] / 1000)
    
    for i in range(0, len(distance_array_2)):
        distance_array_2[i] = int(distance_array_2[i] / 1000)
    

    print((total_distance_list))
    print((distance_array_1))
    print((distance_array_2))

    n = len(distance_array_2)

    ind = np.arange(n)
    width = 0.2
    fig, ax = plt.subplots(figsize=(10, 6))

    bars1 = ax.bar(ind, distance_array_1, width, label='No. Wasted distance of existing algorithm')

    bars2 = ax.bar(ind + width, distance_array_2, width, label='No. Wasted distance of proposal algorithm')
    
    bars3 = ax.bar(ind + 2 * width, total_distance_list, width, label='Total distance')

    ax.set_xlabel('Time (h)')
    ax.set_ylabel('Distance (km)')
    ax.set_xticks(ind + width)
    ax.set_xticklabels(['%d' % (i+1) for i in range(n)])
    ax.legend()

    # plt.xticks(x)
    plt.yticks([0,1000,2000, 3000, 4000, 5000, 6000, 7000])

    # Hiển thị giá trị trên đỉnh mỗi cột
    for bar in bars1:
        height = bar.get_height()

    for bar in bars2:
        height = bar.get_height()

    for bar in bars3:
        height = bar.get_height()

    # Hiển thị biểu đồ
    plt.show()

# Hình 4.9. Tổng số xe trong mỗi round
def main8(file_name):
    with open(file_name, 'r') as file:
        vehicles = json.load(file)
     
     # Chuyển đổi dữ liệu thành chuỗi JSON
    # vehicles = json.dumps(data, indent=4)

    # return
    timeslot1 = 3599.9

    num_vehicle = []
    node_satisfy_list = []
    node_small_list = []
    timeslot1 = 3599.9    # Data from 0 to 3600s
    while (timeslot1 <= 36000):
        node_small = 0
        no_vehicle = 0
        node_satisfy = 0
        for i in range(0, len(vehicles)):
            if (float(vehicles[i]['time']) == timeslot1):
                no_vehicle += 1
                if (vehicles[i]['mining'] == True): 
                    node_satisfy += 1
                    if (vehicles[i]['distance'] < vehicles[i]['threshold']):
                        node_small += 1
        # break
        timeslot1 += 3600
        num_vehicle.append(no_vehicle)
        node_small_list.append(node_small)
        node_satisfy_list.append(node_satisfy)
        
    print(node_satisfy_list)
    print(node_small_list)
    print(num_vehicle)
    
    n = len(node_satisfy_list)

    ind = np.arange(n)
    width = 0.75
    fig, ax = plt.subplots(figsize=(10, 6))

    # bars1 = ax.bar(ind, node_small_list, width, label='No. winners with small contribution')

    # bars2 = ax.bar(ind + width, node_satisfy_list, width, label='No. winners')
    
    bars3 = ax.bar(ind, num_vehicle, width, label='Total vehicles', color="green")

    ax.set_xlabel('Time (h)')
    ax.set_ylabel('No. Vehicles')
    ax.set_xticks(ind)
    ax.set_xticklabels(['%d' % (i+1) for i in range(n)])
    ax.legend()

    # plt.xticks(x)
    plt.yticks([0,100,200,300])

    # Hiển thị giá trị trên đỉnh mỗi cột
    # for bar in bars1:
    #     height = bar.get_height()
    #     ax.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom')

    # for bar in bars2:
    #     height = bar.get_height()
    #     ax.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom')

    for bar in bars3:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom')

    # Hiển thị biểu đồ
    plt.show()

# Fig 4.5 & Fig 4.6
def main9(file_existing_algorithm, file_proposal_algorithm, noVehicle=False):
    with open(file_existing_algorithm, 'r') as file:
        existing_algorithm_vehicles = json.load(file)
    
    with open(file_proposal_algorithm, 'r') as file:
        proposal_algorithm_vehicles = json.load(file)
    
    timeslot = 3599.9
    existing_algorithm_column = []
    proposal_algorithm_column = []
    proposal_algorithm_candidate_column = []
    total_distance_column = []

    while (timeslot < 36000):
        existing_algorithm_no_vehicle = 0
        proposal_algorithm_no_vehicle = 0
        existing_algorithm_distance = 0
        proposal_algorithm_distance = 0
        proposal_algorithm_candidate = 0
        total_distance = 0
        total_distance_no_vehicle = 0
        
        for i in range(len(existing_algorithm_vehicles)):
            if (existing_algorithm_vehicles[i]['time'] == timeslot):
                if (existing_algorithm_vehicles[i]['mining'] == True):
                    existing_algorithm_distance += existing_algorithm_vehicles[i]['distance']
                    existing_algorithm_no_vehicle += 1
                    
        for i in range(len(proposal_algorithm_vehicles)):
            if (proposal_algorithm_vehicles[i]['time'] == timeslot):
                if (proposal_algorithm_vehicles[i]['distance'] > proposal_algorithm_vehicles[i]['threshold']):
                    proposal_algorithm_candidate += 1

                if (proposal_algorithm_vehicles[i]['mining'] == True):
                    proposal_algorithm_distance += proposal_algorithm_vehicles[i]['distance']
                    proposal_algorithm_no_vehicle += 1

        for i in range(len(existing_algorithm_vehicles)):
            if (existing_algorithm_vehicles[i]['time'] == timeslot):
                total_distance += existing_algorithm_vehicles[i]['distance']
                total_distance_no_vehicle += 1

        if (noVehicle == False):
            # Append array to draw graph
            if (existing_algorithm_no_vehicle != 0):
                existing_algorithm_distance = existing_algorithm_distance/existing_algorithm_no_vehicle
            existing_algorithm_column.append(int(existing_algorithm_distance))
            
            if (proposal_algorithm_no_vehicle != 0):
                proposal_algorithm_distance = proposal_algorithm_distance/proposal_algorithm_no_vehicle
            proposal_algorithm_column.append(int(proposal_algorithm_distance))
            
            total_distance_column.append(int(total_distance/total_distance_no_vehicle))
        else:
            existing_algorithm_column.append(existing_algorithm_no_vehicle)
            proposal_algorithm_column.append(proposal_algorithm_no_vehicle)
            proposal_algorithm_candidate_column.append(proposal_algorithm_candidate) # Đang đến đoạn này
            total_distance_column.append(total_distance_no_vehicle)

        timeslot += 3600
    print(existing_algorithm_column)
    print(proposal_algorithm_column)
    print(total_distance_column)
    

    if (noVehicle == False):
        for i in range(0, len(existing_algorithm_column)):
            existing_algorithm_column[i] = int(existing_algorithm_column[i]/1000)

        for i in range(0, len(proposal_algorithm_column)):
            proposal_algorithm_column[i] = int(proposal_algorithm_column[i]/1000)
        
        for i in range(0, len(total_distance_column)):
            total_distance_column[i] = int(total_distance_column[i]/1000)
        
        n = len(total_distance_column)
        ind = np.arange(n)
        width = 0.2
        fig, ax = plt.subplots(figsize=(10, 6))

        bars1 = ax.bar(ind, existing_algorithm_column, width, label='No. average contributed distance of existing algorithm')

        bars2 = ax.bar(ind + width, proposal_algorithm_column, width, label='No. average contributed distance of proposal algorithm')
    
        bars3 = ax.bar(ind + 2 * width, total_distance_column, width, label='No. average total distance')
        
        ax.set_xlabel('Time (h)')
        ax.set_ylabel('Distance (km)')
        ax.set_xticks(ind + width)
        ax.set_xticklabels(['%d' % (i+1) for i in range(n)])
        ax.legend()
        yticks = [0,50,70]

        plt.yticks(yticks)
        # Hiển thị giá trị trên đỉnh mỗi cột
        for bar in bars1 + bars2 + bars3:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom', fontsize=8)

    else:
        n = len(total_distance_column)
        ind = np.arange(n)
        width = 0.20
        fig, ax = plt.subplots(figsize=(10, 6))

        bars1 = ax.bar(ind, existing_algorithm_column, width, color='#1f77b4', label='No. vehicles of existing algorithm')
        bars2 = ax.bar(ind + width, proposal_algorithm_column, width, color='#ff7f0e', label='No. vehicles of proposal algorithm')
        bars3 = ax.bar(ind + 2 * width, proposal_algorithm_candidate_column, width,color='#d62728', label='No. candidates of proposal algorithm')
        bars4 = ax.bar(ind + 3 * width, total_distance_column, width, color='#2ca02c', label='Total vehicles')

        yticks = [0,100,200,300]
        ax.set_xlabel('Time (h)')
        ax.set_ylabel('No. Vehicles')
        ax.set_xticks(ind + width)
        ax.set_xticklabels(['%d' % (i+1) for i in range(n)])
        ax.legend()

        plt.yticks(yticks)

        # Hiển thị giá trị trên đỉnh mỗi cột
        for bar in bars1 + bars2 + bars3 + bars4:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width() / 2, height, '%d' % int(height), ha='center', va='bottom', fontsize=8)

    plt.show()

# Fig 4.1.3 Total wasted distance of 2 algorithm
# main4("v2.1.json", "v4.5_statistic_hash_distance_average.json")

# main5("v4.7_hash_distance_average_not_filter.json") # Fig 4.7 Winner small contribution, proposal algorithm

# Hình 5.3. Thống kê số giá trị coin và distance khác nhau trong mỗi round
# main6("v2.1.json", "v4.6_hash_distance_average.json")

# Fig 4.1.1. Wasted distance of 2 algorithms
# main7("v2.1.json", "v4.6_hash_distance_average.json")

# Hình 4.9. Tổng số xe trong mỗi round
# main8("v4.6_hash_distance_average.json")

# main9("./v2.1.json", "./v4.6_hash_distance_average.json")   # Fig 4.5. Contributed distance 
# main9("./v2.1.json", "./v4.6_hash_distance_average.json", noVehicle=True)   # Vẽ hình 4.6. No. winners of 2 algorithm