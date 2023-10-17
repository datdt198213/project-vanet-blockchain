import json
import csv
import datetime
import time

net_file = '../data/net.json'

times = 1

while times < 2: # number of files vehicle[i].json
    vehicle_file = '../data/vehicle' + str(times) + '.json'

    # Define class lane
    class lane:
        def __init__(self, _id, _type, _speed, _length, _shape):
            self.id = _id
            self.type = _type
            self.speed = _speed
            self.length = _length
            self.shape = _shape

        def display(self):
            print(f"ID: {self.id}, Type: {self.type}, Speed: {self.speed}, Length: {self.length}, Shape: {self.shape}")

    lanes = []

    # Load data from json file and create vehicle array
    with open(net_file) as json_file:
        data = json.load(json_file)
        
        edge = data['net']['edge']
        junction = data['net']['junction']
        connection = data['net']['connection']

        for i in edge:
            try:
                type_of_lane = i['type']
                if(type(i['lane']) == list):
                    for j in i['lane']:
                        lanes.append(lane(j['id'], type_of_lane, j['speed'], j['length'], j['shape']))
                elif(type(i['lane']) == dict):
                    j = i['lane']                    
                    lanes.append(lane(j['id'], type_of_lane, j['speed'], j['length'], j['shape']))

            except KeyError:
                if(type(i['lane']) == list):
                    for j in i['lane']:
                        lanes.append(lane(j['id'], 'highway.normal', j['speed'], j['length'], j['shape']))
                elif(type(i['lane']) == dict):
                    j = i['lane']                    
                    lanes.append(lane(j['id'], 'highway.normal', j['speed'], j['length'], j['shape']))
                print("Not have key type")

    # Define class vehicle
    class vehicle:
        def __init__(self, _time, _id, _x, _y, _angle, _speed, _pos, _lane, _duration, _condition, _event, _congestion):
            self.time = _time
            self.id = _id
            self.x = _x
            self.y = _y
            self.angle = _angle
            self.speed = _speed
            self.pos = _pos
            self.lane = _lane
            self.duration = _duration
            self.condition = _condition
            self.event = _event
            self.congestion = _congestion

        def display(self):
            print(f"Time: {self.time}, id: {self.id}, X: {self.x}, Y: {self.y}, Angle: {self.angle}, Speed: {self.speed}, Position: {self.pos}, Lane: {self.lane}, Duration: {self.duration}, Condition: {self.condition}, Event {self.event}, Congestion: {self.congestion}")

    vehicles = []

    with open(vehicle_file) as json_file:
        data = json.load(json_file)

        timestep = data['fcd-export']['timestep']

        for i in timestep:
            if (type(i['vehicle']) == list):
                for j in i['vehicle']:
                    vehicles.append(vehicle(i['time'], j['id'], j['x'], j['y'], 
                        j['angle'], j['speed'], j['pos'], 
                        j['lane'], 0.0, "Smooth", "Others", 0))
            elif (type(i['vehicle']) == dict):
                vehicles.append(vehicle(i['time'], i['vehicle']['id'], i['vehicle']['x'], i['vehicle']['y'], 
                        i['vehicle']['angle'], i['vehicle']['speed'], i['vehicle']['pos'], 
                        i['vehicle']['lane'], 0.0, "Smooth", "Others", 0))

        new_vehicles = []

        # Classify data
        check = []
        for i in range(0, len(vehicles)):
            check.append(False)

        for i in range(0, len(vehicles)):
            temps = []
            if (check[i] == False):
                temps.append(vehicles[i])
                check[i] = True

                for j in range(i+1, len(vehicles)):
                    if(vehicles[i].id == vehicles[j].id and check[j] == False):
                        temps.append(vehicles[j])
                        check[j] = True

                new_vehicles.append(temps)

        # Calculate duration and set congestion event
        current_day = 1

        for v in new_vehicles:
            duration = 0
            for i in range(1, len(v)):
                if v[i].pos == v[i-1].pos:
                    duration += 0.1
                    v[i].duration = duration
                    if duration > 5:
                        v[i].event = "Accident"
                        v[i].congestion = 1


    class export: 
        def __init__(self, _id, _timestamp, _X, _Y, _velocity, _duration, _road_type, _road_condition, _road_event, _congestion):
            self.id = _id
            self.timestamp = _timestamp
            self.latitudes = _X
            self.longtitudes = _Y
            self.velocity = _velocity
            self.duration = _duration
            self.road_type = _road_type
            self.road_condition = _road_condition
            self.road_event = _road_event
            self.congestion = _congestion

        def display(self):
            print(f"ID: {self.id} Timestamp: {self.timestamp}, Longtitudes: {self.longtitudes}, Latitudes: {self.latitudes}, velocity: {self.velocity}, duration: {self.duration}, road type: {self.road_type}, road condition: {self.road_condition}, road event: {self.road_event}, congestion: {self.congestion}")

        def get_row(self):
            return [self.id, self.timestamp, self.longtitudes, self.latitudes, self.velocity, self.duration, self.road_type, self.road_condition, self.road_event, self.congestion]

    exports = []

    def export_data():
        
        for v in vehicles:
            exports.append(export(v.id, v.time, v.x, v.y, v.speed, v.duration, v.lane, v.condition, v.event, v.congestion))

        # Mode overwrite
        # f = open('data.csv', 'w')
        # writer.writerow(["Node", "Timestamp", "X", "Y", "Velocity", "Duration", "Road Type", "Road Condition", "Road Event", "Congestion"])

        # Mode append 
        f = open('../data/data.csv', 'a')

        writer = csv.writer(f)


        for ve in exports:
            writer.writerow(ve.get_row())
        
        for e in exports:
            e.display()

    start = time.time()
    export_data()
    end = time.time()
    print("The time of execution of above program is :",
        (end-start) * 10**3, "ms")
    
    print(f'handle_data: times = {times}' )
    times += 1
