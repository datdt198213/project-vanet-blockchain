# import module
import fileinput
import time
import math
import hashlib
import json

# Thống kê quãng đường đi được, tích lũy quãng đường với ngưỡng là quãng đường trung bình, thuật toán hash distance trung bình
def v4_5_statistic_hash_distance_average (filename):
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

    # Đặt Id cho các xe lớn hơn 20 để thực hiện tích lũy và đặt lại các giá trị mining của các xe là False
    time_init = 3599.9
    count = 1
    while(time_init <= 36000):
        count_tmp = 20
        for i in range(len(vehicle_list)):
            vehicle_list[i]["mining"] = False
            if(vehicle_list[i]["time"] == time_init):
                if(int(vehicle_list[i]["id"]) >= 20):
                    vehicle_list[i]["id"] = count_tmp
                    count_tmp += 1
                    
        # print(count_tmp)
        count += 1
        time_init += 3600
 
    # Calculate distance, coin and hash coin average, compare hash
    time_init = 3599.9
    distance_tmp_list = []
    while(time_init <= 36000):
        # Khởi tạo tổng quãng đường cho round hiện tại và biến đếm số lượng xe trong round hiện tại
        total_distance = 0
        count_vehicle = 0
        
        # Tích lũy bắt đầu từ round 2, (đã test và kiểm tra dữ liệu)
        if(time_init != 3599.9):
            tmp_idx = [] # mảng chứa các vị trí các phần tử có quãng đường của round trước đã được cập nhật cho round hiện tại
            for i in range(len(vehicle_list)):
                if (time_init == float(vehicle_list[i]["time"])):
                    for idx in range(len(distance_tmp_list)):
                        if (vehicle_list[i]["id"] == distance_tmp_list[idx]['id']):
                            vehicle_list[i]["distance"] += distance_tmp_list[idx]['distance']
                            tmp_idx.append(idx)
                
                # Cập nhật lại giá trị quãng đường của round trước là 0 nếu đã được cập nhật tại round hiện tại
                for idx in range(len(distance_tmp_list)):
                    if (float(distance_tmp_list[idx]["time"]) == float(vehicle_list[i]["time"])):
                        if(distance_tmp_list[idx]["id"] == vehicle_list[i]["id"]):
                            vehicle_list[i]["distance"] = 0
                            break


            # Xóa các phần tử đã được tăng quãng đường trong mảng distance_tmp_list
            error = 0
            try:
                if (len(tmp_idx) != 0):
                    tmp_idx.sort(reverse=True)
                    for idx in tmp_idx: 
                        error = idx
                        del distance_tmp_list[idx]

            except:
                print("Idx error:", error)
                print(tmp_idx)
                print('Len current of array', len(distance_tmp_list))

        # Tính tổng quãng đường và quãng đường trung bình của round hiện tại 
        for i in range(len(vehicle_list)):
            if (time_init == float(vehicle_list[i]["time"])):
                total_distance += int(vehicle_list[i]["distance"])
                count_vehicle += 1
        average_distance = int(total_distance/count_vehicle)

        # Tính số lượng xe đạt được PoD trong round hiện tại
        for i in range(len(vehicle_list)):
            if (time_init == float(vehicle_list[i]["time"])):
                current_distance = int(vehicle_list[i]["distance"])
                hash_average = hashlib.sha256(str(average_distance).encode()).hexdigest()
                hash_vehicle = hashlib.sha256(str(current_distance).encode()).hexdigest()
                vehicle_list[i]["threshold"] = average_distance
                vehicle_list[i]["coin"] = 0
                
                # Nếu quãng đường của xe hiện tại lớn hơn quãng đường trung bình thì thực hiện so sánh
                if(current_distance > average_distance):
                    if (hash_vehicle > hash_average):
                        vehicle_list[i]["mining"] = True
                        vehicle_list[i]["coin"] = int(current_distance / average_distance)
                else:
                    distance_tmp_list.append({"time": vehicle_list[i]['time'], "id": vehicle_list[i]["id"], "distance": int(vehicle_list[i]["distance"])})
                
                if (vehicle_list[i]["distance"] > average_distance and vehicle_list[i]["mining"] == False):
                    distance_tmp_list.append({"time": vehicle_list[i]['time'], "id": vehicle_list[i]["id"], "distance": int(vehicle_list[i]["distance"])})

        time_init += 3600
    data = []
    for vehicle in vehicle_list:
        # print(vehicle)
        new_entry = {
            "time": vehicle["time"],
            "id": vehicle["id"],
            "distance": int(vehicle["distance"]),
            "coin": int(vehicle["coin"]),
            "mining": vehicle["mining"],
            "threshold": vehicle["threshold"]
        }
        data.append(new_entry)
    
    json_file_path = 'v4.5_statistic_hash_distance_average.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


def v4_6_hash_distance_average(filename):
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

    # Đặt Id cho các xe lớn hơn 20 để thực hiện tích lũy và đặt lại các giá trị mining của các xe là False
    time_init = 3599.9
    count = 1
    while(time_init <= 36000):
        count_tmp = 20
        for i in range(len(vehicle_list)):
            vehicle_list[i]["mining"] = False
            if(float(vehicle_list[i]["time"]) == time_init):
                if(int(vehicle_list[i]["id"]) >= 20):
                    vehicle_list[i]["id"] = count_tmp
                    count_tmp += 1
                    
        # print(count_tmp)
        count += 1
        time_init += 3600
 
    # Calculate distance, coin and hash coin average, compare hash
    time_init = 3599.9
    distance_tmp_list = []
    while(time_init <= 36000):
        # Khởi tạo tổng quãng đường cho round hiện tại và biến đếm số lượng xe trong round hiện tại
        total_distance = 0
        count_vehicle = 0
        
        # Tích lũy bắt đầu từ round 2, (đã test và kiểm tra dữ liệu)
        if(time_init != 3599.9):
            tmp_idx = [] # mảng chứa các vị trí các phần tử có quãng đường của round trước đã được cập nhật cho round hiện tại
            for i in range(len(vehicle_list)):
                if (time_init == float(vehicle_list[i]["time"])):
                    for idx in range(len(distance_tmp_list)):
                        if (int(vehicle_list[i]["id"]) == distance_tmp_list[idx]['id']):
                            vehicle_list[i]["distance"] += distance_tmp_list[idx]['distance']
                            tmp_idx.append(idx)
                
                # Cập nhật lại giá trị quãng đường của round trước là 0 nếu đã được cập nhật tại round hiện tại
                # for idx in range(len(distance_tmp_list)):
                #     if (distance_tmp_list[idx]["time"] == vehicle_list[i]["time"]):
                #         if(distance_tmp_list[idx]["id"] == vehicle_list[i]["id"]):
                #             vehicle_list[i]["distance"] = 0
                #             break


            # Xóa các phần tử đã được tăng quãng đường trong mảng distance_tmp_list
            error = 0
            try:
                if (len(tmp_idx) != 0):
                    tmp_idx.sort(reverse=True)
                    for idx in tmp_idx: 
                        error = idx
                        del distance_tmp_list[idx]

            except:
                print("Idx error:", error)
                print(tmp_idx)
                print('Len current of array', len(distance_tmp_list))

        # Tính tổng quãng đường và quãng đường trung bình của round hiện tại 
        for i in range(len(vehicle_list)):
            if (time_init == float(vehicle_list[i]["time"])):
                total_distance += int(vehicle_list[i]["distance"])
                count_vehicle += 1
        average_distance = int(total_distance/count_vehicle)

        # Tính số lượng xe đạt được PoD trong round hiện tại
        for i in range(len(vehicle_list)):
            if (time_init == float(vehicle_list[i]["time"])):
                current_distance = int(vehicle_list[i]["distance"])
                hash_average = hashlib.sha256(str(average_distance).encode()).hexdigest()
                hash_vehicle = hashlib.sha256(str(current_distance).encode()).hexdigest()
                vehicle_list[i]["threshold"] = average_distance
                vehicle_list[i]["coin"] = 0
                
                # Nếu quãng đường của xe hiện tại lớn hơn quãng đường trung bình thì thực hiện so sánh
                if(current_distance > average_distance):
                    if (hash_vehicle > hash_average):
                        vehicle_list[i]["mining"] = True
                        vehicle_list[i]["coin"] = int(current_distance / average_distance)
                else:
                    distance_tmp_list.append({"time": vehicle_list[i]['time'], "id": vehicle_list[i]["id"], "distance": int(vehicle_list[i]["distance"])})
                
                if (vehicle_list[i]["distance"] > average_distance and vehicle_list[i]["mining"] == False):
                    distance_tmp_list.append({"time": vehicle_list[i]['time'], "id": vehicle_list[i]["id"], "distance": int(vehicle_list[i]["distance"])})

        time_init += 3600

    data = []
    for vehicle in vehicle_list:
        new_entry = {
            "time": vehicle["time"],
            "id": vehicle["id"],
            "distance": int(vehicle["distance"]),
            "coin": int(vehicle["coin"]),
            "mining": vehicle["mining"],
            "threshold": int(vehicle["threshold"])
        }
        data.append(new_entry)
    
    json_file_path = 'v4.6_hash_distance_average.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Tích lũy quãng đường với ngưỡng là quãng đường trung bình, thuật toán hash distance không filter
def v4_7_hash_distance_average_not_filter (filename):
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

    # Đặt Id cho các xe lớn hơn 20 để thực hiện tích lũy và đặt lại các giá trị mining của các xe là False
    time_init = 3599.9
    count = 1
    while(time_init <= 36000):
        count_tmp = 20
        for i in range(len(vehicle_list)):
            vehicle_list[i]["mining"] = False
            if(vehicle_list[i]["time"] == time_init):
                if(int(vehicle_list[i]["id"]) >= 20):
                    vehicle_list[i]["id"] = count_tmp
                    count_tmp += 1
                    
        # print(count_tmp)
        count += 1
        time_init += 3600
 
    # Calculate distance, coin and hash coin average, compare hash
    time_init = 3599.9
    distance_tmp_list = []
    while(time_init <= 36000):
        # Khởi tạo tổng quãng đường cho round hiện tại và biến đếm số lượng xe trong round hiện tại
        total_distance = 0
        count_vehicle = 0
        
        # Tích lũy bắt đầu từ round 2, (đã test và kiểm tra dữ liệu)
        if(time_init != 3599.9):
            tmp_idx = [] # mảng chứa các vị trí các phần tử có quãng đường của round trước đã được cập nhật cho round hiện tại
            for i in range(len(vehicle_list)):
                if (time_init == vehicle_list[i]["time"]):
                    for idx in range(len(distance_tmp_list)):
                        if (int(vehicle_list[i]["id"]) == distance_tmp_list[idx]['id']):
                            vehicle_list[i]["distance"] += distance_tmp_list[idx]['distance']
                            tmp_idx.append(idx)
                
                # Cập nhật lại giá trị quãng đường của round trước là 0 nếu đã được cập nhật tại round hiện tại
                # for idx in range(len(distance_tmp_list)):
                #     if (distance_tmp_list[idx]["time"] == vehicle_list[i]["time"]):
                #         if(distance_tmp_list[idx]["id"] == vehicle_list[i]["id"]):
                #             vehicle_list[i]["distance"] = 0
                #             break


            # Xóa các phần tử đã được tăng quãng đường trong mảng distance_tmp_list
            error = 0
            try:
                if (len(tmp_idx) != 0):
                    tmp_idx.sort(reverse=True)
                    for idx in tmp_idx: 
                        error = idx
                        del distance_tmp_list[idx]

            except:
                print("Idx error:", error)
                print(tmp_idx)
                print('Len current of array', len(distance_tmp_list))

        # Tính tổng quãng đường và quãng đường trung bình của round hiện tại 
        for i in range(len(vehicle_list)):
            if (time_init == float(vehicle_list[i]["time"])):
                total_distance += int(vehicle_list[i]["distance"])
                count_vehicle += 1
        average_distance = int(total_distance/count_vehicle)

        # Tính số lượng xe đạt được PoD trong round hiện tại
        for i in range(len(vehicle_list)):
            if (time_init == float(vehicle_list[i]["time"])):
                current_distance = int(vehicle_list[i]["distance"])
                hash_average = hashlib.sha256(str(average_distance).encode()).hexdigest()
                hash_vehicle = hashlib.sha256(str(current_distance).encode()).hexdigest()
                vehicle_list[i]["threshold"] = average_distance
                vehicle_list[i]["coin"] = 0
                
                # Thực hiện bước so sánh hash
                if (hash_vehicle > hash_average):
                    vehicle_list[i]["mining"] = True
                    vehicle_list[i]["coin"] = int(current_distance / average_distance)
                else:
                    distance_tmp_list.append({"time": vehicle_list[i]['time'], "id": vehicle_list[i]["id"], "distance": int(vehicle_list[i]["distance"])})

        time_init += 3600

    data = []
    for vehicle in vehicle_list:
        new_entry = {
            "time": vehicle["time"],
            "id": vehicle["id"],
            "distance": int(vehicle["distance"]),
            "coin": int(vehicle["coin"]),
            "mining": vehicle["mining"],
            "threshold": int(vehicle["threshold"])
        }
        data.append(new_entry)
    
    json_file_path = 'v4.7_hash_distance_average_not_filter.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)


# v4_5_statistic_hash_distance_average(filename="v1.1.json")
# v4_6_hash_distance_average(filename="v1.1.json")
# v4_7_hash_distance_average_not_filter(filename="v1.1.json")
