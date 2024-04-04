import os
import sys

# Set time running simulation, 0 - 2000s
begin = 0
end = int(sys.argv[1]) # Read parameter from command
insertionRate = int(sys.argv[2]) # Insertion rate is defined number of vehicles in SUMO

# Define path, in different setting variable environment, we need to set SUMO_HOME and PATH_RANDOMTRIP 
SUMO_HOME = "/root/sumo/"
PATH_RANDOMTRIP = "python3 "+ SUMO_HOME + "tools/randomTrips.py"


PATH_NET = "../sumo/net.net.xml"
PATH_ROUTE = "../sumo/route.rou.xml"

command1 = PATH_RANDOMTRIP + " -n" + PATH_NET + " -r " + PATH_ROUTE +" -b " + str(begin) +  " -e " + str(end) + " --insertion-rate " +  str(insertionRate) + " -l "

os.system(command1)

# Output latitude and longtitude
command2 = "sumo -c ../sumo/simulation" + str(insertionRate) + ".sumo.cfg --fcd-output ../sumo/vehicle" + str(insertionRate) +".sumo.xml --fcd-output.geo"

os.system(command2)

# Next time to begin += 2000s and end += 2000s
begin += int(sys.argv[1])
end += int(sys.argv[1])
print(f'DONE init_vehicle: vehicle[{insertionRate}].sumo.xml file')