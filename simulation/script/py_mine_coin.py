import math
import hashlib
import json
import fs
import sys
import time

start = time.time()
class Driver:
    def __init__(self, id, distance, time, coin):
        self.id = id
        self.distance = float(distance)
        self.time = float(time)
        self.coin = float(coin)

    def display(self):
        print(f"id: {self.id}, Distance: {self.distance}, Time: {self.time}, Coin: {self.coin}")

class Vehicle:
    def __init__(self, vehicle, time):
        self.id = vehicle['id']
        self.x = vehicle['x']
        self.y = vehicle['y']
        self.angle = vehicle['angle']
        self.type = vehicle['type']
        self.speed = vehicle['speed']
        self.pos = vehicle['pos']
        self.lane = vehicle['lane']
        self.slope = vehicle['slope']
        self.time = float(time)


# Calculate distance by Haversine formula (miles)
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)

    a = math.sin(dLat / 2) * math.sin(dLat / 2) + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dLon / 2) * math.sin(dLon / 2)

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c  # The distance in kilometers
    distance *= 1000  # Convert distance to meters
    return distance

def sha512(input_string):
    hashed = hashlib.sha512(input_string.encode()).hexdigest()
    return hashed

def get_data_from_json(begin, end):
    with open('your_json_file.json', 'r') as file:
        data_json = json.load(file)

    data = data_json['fcd-export']['timestep']

    data_list = []

    for element in data:
        time = float(element['time'])
        if begin <= time <= end:
            # Having an object
            if 'vehicle' in element:
                vehicles = element['vehicle']
                if not isinstance(vehicles, list):
                    # Push data to list
                    data_list.append(Vehicle(vehicles, element['time']))
                else:
                    # Having object list
                    for v in vehicles:
                        data_list.append(Vehicle(v, element['time']))

    return data_list

def classify_list(drivers):
    new_drivers = []
    check = [False] * len(drivers)

    for i in range(len(drivers)):
        current_list = []
        if not check[i]:
            current_list.append(drivers[i])
            check[i] = True
            for j in range(i + 1, len(drivers)):
                if drivers[i].id == drivers[j].id and not check[j]:
                    current_list.append(drivers[j])
                    check[j] = True
            new_drivers.extend(current_list)

    # for v in new_drivers:
    #     print(v)
    # print("DONE Classify list: Length =", len(new_drivers))
    return new_drivers

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

        if idx < len(vehicles) - 1:
            if vehicles[idx - 1].id != vehicles[idx].id:
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

def rule(drivers):
    node_pod = []
    w = 0

    for d in drivers:
        w += d.coin

    w = w / len(drivers)
    hash_w = sha512(str(w))

    for driver in drivers:
        if driver.coin != 0:
            hash_current = sha512(str(driver.coin))

            if hash_current <= hash_w:
                node_pod.append(driver)

    # print("DONE rule: Number of node POD =", len(node_pod))
    for v in node_pod:
        print(v)

    return node_pod

def main():
    global beginTime, endTime, distance, timeslot, totalTime, numVehicles  # Đảm bảo rằng các biến đã được định nghĩa trước đó
    begin = beginTime
    end = endTime

    if not begin or not end or not distance:
        print("Warning: Please enter valid parameters in the running command.")
        sys.exit()

    input_data = get_data_from_json(begin, end)

    t = input_data[len(input_data) - 1].time - input_data[0].time
    print(f"t = {t} timeslot = {timeslot}")
    
    if round(t) == timeslot:
        print(f"Time begin = {begin} Time end = {end}")
        class_list = classify_list(input_data)
        distance_list = calculate_distance_list(class_list, distance, end)
        n_pod = rule(distance_list)

        # Statistic
        data_arrays = [[timeslot, begin, end - 0.1, distance, len(distance_list), len(n_pod), totalTime, numVehicles]]

        file_name = f"../data/data_statistic_{numVehicles}.csv"
        try:
            with open(file_name, 'a') as stream:
                stream.write(",".join(map(str, data_arrays[0])) + "\r\n")
            print("Filename:", file_name)
        except FileNotFoundError:
            print("Error: File not found.")

main()
end = time.time()
print(f"Execution time: {end - start} ms")