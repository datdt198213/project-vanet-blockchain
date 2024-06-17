import os
import sys
import json
import os
import sys


# Define path, in different setting variable environment, we need to set SUMO_HOME and PATH_RANDOMTRIP 


# Generate dữ liệu xe đi bằng công cụ của sumo

def generate_by_sumo():
    # SUMO_HOME = "/root/sumo/"
    # PATH_RANDOMTRIP = "python3 "+ SUMO_HOME + "tools/randomTrips.py"
    # PATH_NET = "../sumo /net.net.xml"
    # PATH_ROUTE = "../sumo/route3.rou.xml"

    # command1 = PATH_RANDOMTRIP + " -n" + PATH_NET + " -r " + PATH_ROUTE +" -b " + str(0) +  " -e " + str(3600) + " --insertion-rate " +  str(100) + " -l "
    # os.system(command1)

    command2 = "sumo -c ../sumo/simulation" + str(100) + ".sumo.cfg --fcd-output ../sumo/vehicle" + str(100) +".sumo.xml --fcd-output.geo"

    os.system(command2)
    print(f'DONE init_vehicle: vehicle100.sumo.xml')

def main ():

    # Initialize file vehicle 
    command = f"sumo -c {config_file} --fcd-output {output_file} --fcd-output.geo"
    os.system(command)

    print(f'DONE init_vehicle: {config_file} => {output_file} file')

config_file = "../sumo/simulation.sumo.cfg"

output_file = "../sumo/vehicle.sumo.xml"
main()