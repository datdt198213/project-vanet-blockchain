import json
import xmltodict
import os
import sys

# Read parameter from command
end = int(sys.argv[1]) 
numVehicles = int(sys.argv[2])
times = int(sys.argv[3])

# Define path file
input_file = '../sumo/vehicle'+ str(times) +'.sumo.xml'
output_file = '../sumo/vehicle' + str(times) + '.json'

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
print("CONVERT DATA excuting ...")
fin = open(temp, "rt")
fout = open(output_file, "wt")
for line in fin:
    fout.write(line.replace('@', ''))
fin.close()
fout.close()

# Delete file Temp.json
os.remove("Temp.json")
# Delete file trips.trips.xml
os.remove("trips.trips.xml")
print(f"DONE convert_data: vehicle[{times}].sumo.xml => vehicle[{times}].json")