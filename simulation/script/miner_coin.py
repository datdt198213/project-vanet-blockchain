import hashlib
import json
import time
from math import radians, sin, cos, sqrt, atan2

# Full time run simulation 
# begin_time = float(input("Enter beginning time parameter in running command: "))
# end_time = float(input("Enter ending time parameter in running command: "))
begin_time  = 0
end_time = 3600

# Define driver class
class Driver:
    def __init__(self, id, distance, time, coin):
        self.id = id
        self.distance = float(distance)
        self.time = float(time)
        self.coin = int(coin)

    def display(self):
        print(f"id: {self.id}, Distance: {self.distance}, Time: {self.time}, Coin: {self.coin}")

# Define vehicle class
class Vehicle:
    def __init__(self, vehicle, time):
        self.id = vehicle["id"]
        self.x = vehicle["x"]
        self.y = vehicle["y"]
        self.angle = vehicle["angle"]
        self.type = vehicle["type"]
        self.speed = vehicle["speed"]
        self.pos = vehicle["pos"]
        self.lane = vehicle["lane"]
        self.slope = vehicle["slope"]
        self.time = float(time)

# Hash string by sha512
def sha512(input_string):
    return hashlib.sha512(input_string.encode()).hexdigest()

# Get data from json and return a list of vehicle in a period of time
def get_data_from_json(begin, end):
    data = data_json["fcd-export"]["timestep"]

    data_list = []

    for element in data:
        time = float(element["time"])
        if begin <= time <= end:
            # Having an object
            if not isinstance(element["vehicle"], list):
                # Push data to the list
                data_list.append(Vehicle(element["vehicle"], element["time"]))
            # Having an object list
            else:
                # Push data to the list
                for v in element["vehicle"]:
                    data_list.append(Vehicle(v, element["time"]))

    return data_list

# Classify data of a node, return a new array that is classified
def classify_list(drivers):
    new_drivers = []
    check = [False] * len(drivers)

    for i in range(len(drivers)):
        lst = []
        if not check[i]:
            lst.append(drivers[i])
            check[i] = True
            for j in range(i + 1, len(drivers)):
                if drivers[i].id == drivers[j].id and not check[j]:
                    lst.append(drivers[j])
                    check[j] = True
            new_drivers.extend(lst)

    return new_drivers

# Calculate distance by haversine formula (meters)
def haversine(lat1, lon1, lat2, lon2):
    # Bán kính của Trái Đất (đơn vị: km)
    r = 6371.0
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)

    # Chuyển đổi độ sang radian
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    # Sự chênh lệch giữa vĩ độ và kinh độ
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Sử dụng công thức Haversine
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = r * c * 1000  # The distance in meters

    return distance

# Calculate distance of a vehicle list, return a driver list
def calculate_distance_list(vehicles, distance, end):
    drivers = []
    d = 0
    c = 0
    for idx in range(1, len(vehicles)):
        if vehicles[idx].id == vehicles[idx - 1].id:
            timestep = vehicles[idx].time - vehicles[idx - 1].time
            round_time = round(timestep, 1)

            if round_time == 0.1:
                d += haversine(vehicles[idx].x, vehicles[idx].y, vehicles[idx - 1].x, vehicles[idx - 1].y)
                if d >= distance:
                    c += int(d / distance)
                    d %= distance

        if idx < len(vehicles) - 1 and vehicles[idx - 1].id != vehicles[idx].id:
            dr = Driver(vehicles[idx - 1].id, d, end, c)
            drivers.append(dr)
            d = 0
            c = 0
        elif idx == len(vehicles) - 1:
            dr = Driver(vehicles[idx - 1].id, d, end, c)
            drivers.append(dr)
            d = 0
            c = 0

    return drivers

# Return satisfying node proof of driving
def rule(drivers):
    node_pod = []

    w = sum(d.coin for d in drivers) / len(drivers)
    hash_w = sha512(str(w))

    for driver in drivers:
        if driver.coin != 0:
            hash_current = sha512(str(driver.coin))
            if hash_current <= hash_w:
                node_pod.append(driver)

    return node_pod

def count_number_of_vehicle(list_vehicle):
    count = 0
    if list_vehicle:
        count = 1
        for i in range(len(list_vehicle) - 1):
            if list_vehicle[i].id != list_vehicle[i + 1].id:
                count += 1
    return count

def main():
    begin = begin_time
    end = end_time
    timeslot = end - begin
    distance = 2000
    count = int(end_time / timeslot)
    output = []

    input_data = get_data_from_json(begin, end)
    class_list = classify_list(input_data)
    distance_list = calculate_distance_list(class_list, distance, end)
    n_pod = rule(distance_list)

    print(f"\nTime begin = {begin}, Time end = {end}")
    print(f"Number of node POD = {len(n_pod)}")

    # Statistics
    all_data_json = get_data_from_json(0, end_time)
    classify_all_data = classify_list(all_data_json)
    number_of_vehicle = count_number_of_vehicle(classify_all_data)
    print(f"Number of vehicle: {number_of_vehicle}")

if __name__ == "__main__":
    begin = time.time()
    with open("../data/vehicle1.json") as json_file:
        data_json = json.load(json_file)
    main()
    end = time.time()
    print("The time of execution of above program is :",
      (end-begin) * 10**3, "ms")
