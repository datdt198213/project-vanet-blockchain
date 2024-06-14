import fileinput
import time
import math
import hashlib
import json

def main (filename):
    with open(filename, 'r') as file:
        vehicle_list = json.load(file)
        
    # Các khoảng thời gian cần thay thế
    time_ranges = [(0, 3599.9), (3600, 7199.9), (7200, 10799.9), (10800, 14399.9), 
                (14400, 17999.9), (18000, 21599.9), (21600, 25199.9), (25200, 28799.9), 
                (28800, 32399.9), (32400, 35999.9)]

    # Thay thế giá trị time theo khoảng thời gian
    for item in vehicle_list:
        for start, end in time_ranges:
            if start <= float(item["time"]) < end:
                item["time"] = end
                break

    
    # Calculate distance, coin and hash coin average, compare hash
    time_init = 3599.9
    while(time_init <= 36000):
        total_distance = 0
        count_vehicle = 0
        for i in range(len(vehicle_list)):
            if (time_init == float(vehicle_list[i]["time"])):
                vehicle_list[i]["mining"] = False
                total_distance += int(vehicle_list[i]["distance"])
                count_vehicle += 1

        total_coin = 0
        for i in range(len(vehicle_list)):
            if (time_init == float(vehicle_list[i]["time"])):
                vehicle_list[i]["coin"] = int(int(vehicle_list[i]["distance"]) / int(2000))
                total_coin += vehicle_list[i]["coin"]
        average_coin = int(total_coin / count_vehicle)            

        for i in range(len(vehicle_list)):
            if (time_init == float(vehicle_list[i]["time"])):
                current_coin = int(vehicle_list[i]["coin"])
                hash_average = hashlib.sha256(str(average_coin).encode()).hexdigest()
                hash_vehicle = hashlib.sha256(str(current_coin).encode()).hexdigest()
                vehicle_list[i]["threshold"] = int(2000)
                vehicle_list[i]["distance"] = int(vehicle_list[i]['distance'])
                if (vehicle_list[i]["coin"] != 0):
                    if (hash_vehicle > hash_average):
                        vehicle_list[i]["mining"] = True
        time_init += 3600
    data = []
    for vehicle in vehicle_list:
        new_entry = {
            "time": vehicle["time"],
            "id": vehicle["id"],
            "distance": vehicle["distance"],
            "coin": vehicle["coin"],
            "mining": vehicle["mining"],
            "threshold": vehicle['threshold']
        }
        data.append(new_entry)
    
    json_file_path = 'v2.1.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

main(filename='v1.json')