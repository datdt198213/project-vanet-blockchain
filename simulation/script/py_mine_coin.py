import math
import hashlib
import json
import sys
import time

start = time.time()

try:
    timeslot = int(sys.argv[1])
    begin_time = int(sys.argv[2])
    end_time = int(sys.argv[3])
    distance = int(sys.argv[4])
    num_vehicles = int(sys.argv[5])
    total_time = int(sys.argv[6])
except IndexError:
    print("Error: Please provide valid command line arguments.")
    sys.exit()

filename = f"../sumo/vehicle{int(num_vehicles)}.json"
try:
    with open(filename, 'r') as file:
        dataJson = json.load(file)
except FileNotFoundError:
    print("Error: File not found.")
    sys.exit()

total_distance = 0
total_coin = 0
total_c = 0

def main():
    begin = begin_time
    end = end_time

    input_data = get_data_from_json(begin, end)
    print(f"{begin}, {timeslot}, {end}, {distance}, {num_vehicles} {total_time}")
    t = input_data[len(input_data) - 1].time - input_data[0].time
    print(f"input timeslot = {t} timeslot = {timeslot}")
    
    if round(t) == timeslot:
        print(f"Time begin = {begin} Time end = {end}")
        class_list = classify_list(input_data)
        distance_list = calculate_coin(class_list, distance, end)
        n_pod = rule(distance_list)

        for v in n_pod:
            v.display()

        # Statistic
        data_arrays = [[timeslot, begin, end - 0.1, distance, len(distance_list), len(n_pod), total_time, num_vehicles, total_distance/1000, total_coin, total_c]]
        print(f'Total distance {total_distance}\t total coin: {total_coin} total coin adding: {total_c}')

        # file_name = f"../data/data_statistic_{num_vehicles}.csv"
        file_name = f"../data/test{num_vehicles}.csv"
        try:
            with open(file_name, 'a', newline="") as stream:
                stream.write(",".join(map(str, data_arrays[0])) + "\r\n")
            print("Filename:", file_name)
        except FileNotFoundError:
            print("Error: File not found.")

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
    lat1 = float(lat1)
    lat2 = float(lat2)
    lon1 = float(lon1)
    lon2 = float(lon2)
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
    try:
        with open(filename, 'r') as file:
            data_json = json.load(file)
            data = data_json['fcd-export']['timestep']
            data_list = []
            for element in data:
                time = float(element['time'])
                if begin <= time and time <= end:
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
    except FileNotFoundError:
        print("Error: File not found.")
        sys.exit()
    
    
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

def calculate_coin(vehicles, distance, end):
    global total_distance, total_coin
    drivers = []
    d = 0

    for idx in range(1, len(vehicles)):
        if vehicles[idx].id == vehicles[idx - 1].id:
            timestep = vehicles[idx].time - vehicles[idx - 1].time
            round_time = round(timestep, 1)

            if round_time == 0.1:
                d += haversine(vehicles[idx].x, vehicles[idx].y, vehicles[idx - 1].x, vehicles[idx - 1].y)
                # if d >= distance:
                #     c += int(d / distance)
                #     total_coin += c
                #     tmp_coin += c
                #     d %= distance

        if idx < len(vehicles) - 1:
            if vehicles[idx - 1].id != vehicles[idx].id:
                total_distance += d
                coin = d / distance
                total_coin += coin
                dr = Driver(vehicles[idx - 1].id, d, end, coin)
                drivers.append(dr)
                d = 0
        elif idx == len(vehicles) - 1:
            total_distance += d
            coin = d / distance
            total_coin += coin
            dr = Driver(vehicles[idx - 1].id, d, end, coin)
            drivers.append(dr)
            d = 0

    return drivers

def rule(drivers):
    global total_c
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
        total_c += v.coin

    return node_pod


main()
end = time.time()
print(f"Execution time: {end - start} ms")