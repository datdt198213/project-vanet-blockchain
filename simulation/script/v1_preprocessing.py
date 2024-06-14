# import module
import fileinput
import time
import math
import hashlib
import json

def main ():
    #time at the start of program is noted
    start = time.time()

    #keeps a track of number of lines in the file
    is_exist = []

    for i in range(0, 1000):
        is_exist.append(False)

    vehicle_list = []
    vehicle_list_storage = []
    vehicle_time = None
    vehicle_id = None
    vehicle_x = None
    vehicle_y = None

    average_coin = 0
    total_coin = 0
        
    for lines in fileinput.input(['../sumo/vehicle100.sumo.xml']):
        if ("<timestep time" in lines):
            lines_split = lines.split('"')
            vehicle_time = lines_split[1]
            # if (vehicle_time != None):
                # print(vehicle_time)
        if ("<vehicle id" in lines):
            lines_split = lines.split('"')
            vehicle_id = lines_split[1]
            vehicle_x = lines_split[3]
            vehicle_y = lines_split[5]
            # print(f"{int(vehicle_id)} {vehicle_x} {vehicle_y}")

        if (vehicle_time != None and vehicle_id != None and vehicle_x != None and vehicle_y != None):

            # Trường hợp khởi tạo 
            # vehicle_list.append({"time": vehicle_time, "id": vehicle_id, "x": vehicle_x, "y": vehicle_y})
            if (is_exist[int(vehicle_id)] == False):
                vehicle_list.append({"time": vehicle_time, "id": vehicle_id, "x": vehicle_x, "y": vehicle_y, "distance": 0})
                is_exist[int(vehicle_id)] = True
            else:
                for i in range(0, len(vehicle_list)):
                    if (vehicle_id == vehicle_list[i]["id"]):
                        # calculate distance by Haversine formula
                        lat1 = float(vehicle_list[i]["x"])
                        lon1 = float(vehicle_list[i]['y'])
                        lat2 = float(vehicle_x)
                        lon2 = float(vehicle_y)
                        # print(lat1, lon1, lat2, lon2)
                        # Công thức Haversine
                        R = 6371000  # Bán kính trung bình của Trái Đất (đơn vị mét)
                        dLat = (lat2 - lat1) * (math.pi / 180)
                        dLon = (lon2 - lon1) * (math.pi / 180)
                        a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(lat1 * (math.pi / 180)) * math.cos(lat2 * (math.pi / 180)) * math.sin(dLon / 2) * math.sin(dLon / 2)
                        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
                        distance = R * c
                        vehicle_list[i]["time"] = vehicle_time
                        vehicle_list[i]["x"] = vehicle_x
                        vehicle_list[i]["y"] = vehicle_y
                        vehicle_list[i]["distance"] = float(vehicle_list[i]["distance"]) + distance
                        # print(distance)
            
            # reset value
            # vehicle_time = None
            vehicle_id = None
            vehicle_x = None
            vehicle_y = None
        
        # End of round 
        if vehicle_time == "3600.00" or vehicle_time == "7200.00" or vehicle_time == "10800.00" or vehicle_time == "14400.00" or vehicle_time == "18000.00" or vehicle_time == "21600.00" or vehicle_time == "25200.00" or vehicle_time == "28800.00" or vehicle_time == "32400.00" or vehicle_time == "36000.00": 

                # for i in range(0, len(vehicle_list)):
                #     if (vehicle_list[i]["distance"] != 0):
                #         total_coin += float(vehicle_list[i]["distance"]) / 2000
                #     is_exist[int(vehicle_list[i]["id"])] = False
                # if (len(vehicle_list) != 0 and vehicle_list[i]["distance"] != 0):
                #     average_coin = total_coin / len(vehicle_list)
                #     hash_average_coin = hashlib.sha256(str(average_coin).encode()).hexdigest()
                #     for i in range(0, len(vehicle_list)):
                #         coin = float(vehicle_list[i]["distance"]) / 2000
                #         vehicle_list[i]["coin"] = coin
                #         hash_coin = hashlib.sha256(str(coin).encode()).hexdigest()
                #         if (hash_coin > hash_average_coin):
                #             vehicle_list[i]["mining"] = True
                #         else: 
                #             vehicle_list[i]["mining"] = False
                
                for i in range(0, len(vehicle_list)):
                    is_exist[int(vehicle_list[i]["id"])] = False
                if (len(vehicle_list) != 0 and vehicle_list[i]["distance"] != 0):
                    for i in range(0, len(vehicle_list)):
                        vehicle_list[i]["coin"] = 0
                        vehicle_list[i]["mining"] = False

                for i in range(0, len(vehicle_list)):
                    vehicle_list_storage.append(vehicle_list[i])
                    # break;  

                vehicle_list.clear()
                # total_coin = 0

                # break
    
    data = []
    for vehicle in vehicle_list_storage:
        new_entry = {
            "time": float(vehicle["time"]),
            "id": vehicle["id"],
            "distance": int(vehicle["distance"]),
            "coin": int(vehicle["coin"]),
            "mining": vehicle["mining"]
        }
        data.append(new_entry)
    
    json_file_path = 'v1.1.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    end = time.time() #time at the end of program execution is noted
    
    #total time taken to print the file
    print("Execution time in seconds: ",(end - start))
    print("No. of lines printed: ",len(vehicle_list))


main()