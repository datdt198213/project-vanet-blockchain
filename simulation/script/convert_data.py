import json
import xmltodict
import os


# input_file = '../sumo/net.net.xml'
# input_file = '../sumo/road-side.poly.xml'
# input_file = '../sumo/route.rou.xml'

# output_file = 'data/net.json'
# output_file = 'data/road_side.json'
# output_file = 'data/route.json'

times = 1
while times < 2: # number of files xml to json
# while times < 3:
# while times < 4:
    input_file = '../sumo/vehicle'+ str(times) +'.sumo.xml'

    output_file = '../data/vehicle' + str(times) + '.json'

    temp = "Temp.json"
    with open(input_file) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        # xml_file.close()
        
        # generate the object using json.dumps()
        # corresponding to json data
            
        json_data = json.dumps(data_dict)
            
        # Write the json data to output
        # json file
        with open(temp, "w") as json_file:
            json_file.write(json_data)

    # Delete @ character in file
    fin = open(temp, "rt")
    fout = open(output_file, "wt")
    for line in fin:
        fout.write(line.replace('@', ''))
    fin.close()
    fout.close()

    # Delete file Temp.json
    os.remove(temp)
    # Delete file trips.trips.xml
    os.remove("trips.trips.xml")
    print(f"DONE convert_data: vehicle[{times}].sumo.xml => vehicle[{times}].json")
    times += 1