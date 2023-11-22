import json
import math 
import time

start = time.time()
f = open('../sumo/vehicle10.json')
data = json.load(f)

class MyVehicle(object):
    def __init__(self, id, x, y, angle, pos, lane, d):
    # def __init__(self, id, d):
        self.id = id
        self.x = x
        self.y = y
        self.angle = angle
        self.pos = pos
        self.lane = lane
        self.d = d
v = []
# for i in data['fcd-export']['timestep']:
# for i in range(50):
for i in range(len(data['fcd-export']['timestep'])):
    varr = data['fcd-export']['timestep'][i]['vehicle']
    if type(varr).__name__ == 'dict':
        d = 0
        if len(v)>0:
            eV = True
            for idx, vi in enumerate(v):
                if vi.id == varr['id']:
                    d = math.sqrt(pow(float(varr['x']) - float(vi.x), 2) + pow(float(varr['y'])-float(vi.y), 2))
                    v[idx].x = varr['x']
                    v[idx].y = varr['y']
                    v[idx].angle = varr['angle']
                    v[idx].pos = varr['pos']
                    v[idx].lane = varr['lane']
                    v[idx].d += d
                    eV = False
                    break
            if eV:
                v.append(MyVehicle(varr['id'], varr['x'], varr['y'], varr['angle'], varr['pos'], varr['lane'], d))  
        else:
            v.append(MyVehicle(varr['id'], varr['x'], varr['y'], varr['angle'], varr['pos'], varr['lane'], d))  
            
    if type(varr).__name__ == 'list':
        numcar = len(varr)
        for j in range(numcar):
            d = 0
            if len(v)>0:
                eV = True
                for idx, vi in enumerate(v):
                    if vi.id == varr[j]['id']:
                        d = math.sqrt(pow(float(varr[j]['x']) - float(vi.x), 2) + pow(float(varr[j]['y'])-float(vi.y), 2))
                        v[idx].x = varr[j]['x']
                        v[idx].y = varr[j]['y']
                        v[idx].angle = varr[j]['angle']
                        v[idx].pos = varr[j]['pos']
                        v[idx].lane = varr[j]['lane']
                        v[idx].d += d
                        eV = False
                        break
                if eV:
                    v.append(MyVehicle(varr[j]['id'], varr[j]['x'], varr[j]['y'], varr[j]['angle'], varr[j]['pos'], varr[j]['lane'], d))
            else:
                v.append(MyVehicle(varr[j]['id'], varr[j]['x'], varr[j]['y'], varr[j]['angle'], varr[j]['pos'], varr[j]['lane'], d))

for lv in range(len(v)):
    print("xe id " + v[lv].id + "d " + str(v[lv].d))
# Closing file
f.close()
end = time.time()
print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")

