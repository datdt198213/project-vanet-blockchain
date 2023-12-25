import os
import sys

# Set time running simulation, 0 - 2000s
begin = 0
end = int(sys.argv[1]) # Read parameter from command

# Insertion rate is defined number of vehicles in SUMO
insertionRate = int(sys.argv[2])

# Define path to 
# SUMO_HOME = "/home/parallel_user/sumo/"
SUMO_HOME = "/root/sumo/"
PATH_RANDOMTRIP = "python3 "+ SUMO_HOME + "tools/randomTrips.py"
PATH_NET = "../sumo/net.net.xml"
PATH_ROUTE = "../sumo/route.rou.xml"

# command1 = PATH_RANDOMTRIP + " -n" + PATH_NET + " -r " + PATH_ROUTE +" -b " + str(begin) +  " -e " + str(end) + " -p " + str(period) + " -l " 

command1 = PATH_RANDOMTRIP + " -n" + PATH_NET + " -r " + PATH_ROUTE +" -b " + str(begin) +  " -e " + str(end) + " --insertion-rate " +  str(insertionRate) + " -l "
# command1 = PATH_RANDOMTRIP + " -n" + PATH_NET + " -r " + PATH_ROUTE +" -b " + str(begin) +  " -e " + str(end) + " --insertion-rate " +  str(insertionRate) + " -l -s 20" 

# python3 /root/sumo/tools/randomTrips.py -n ../sumo/net.net.xml -r ../sumo/route.rou.xml -b 0 -e 36000 --insertion-rate 208 -l -s 40
# python3 my_random_trips.py -n net.net.xml -r route.rou.xml -b 0 -e 10 --insertion-rate 2 > my_random_trips.txt
os.system(command1)

# Output latitude and longtitude
command2 = "sumo -c ../sumo/simulation" + str(insertionRate) + ".sumo.cfg --fcd-output ../sumo/vehicle" + str(insertionRate) +".sumo.xml --fcd-output.geo"

# Output X Y 
# command2 = "sumo -c ../sumo/simulation208.sumo.cfg --fcd-output ../sumo/vehicle208.sumo.xml

os.system(command2)

# Next time to begin += 2000s and end += 2000s
begin += int(sys.argv[1])
end += int(sys.argv[1])
print(f'DONE init_vehicle: vehicle[{insertionRate}].sumo.xml file')