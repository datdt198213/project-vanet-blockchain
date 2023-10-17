import os
import sys

times = 1

# Set time running simulation, 0 - 2000s
begin = 0
end = int(sys.argv[1]) # Read parameter from command

# Set number of vehicle: numberOfVehice = (end - begin) / n
# n = (end - begin) / int(sys.argv[2])   # Read parameter from command
n = int(sys.argv[2])

# Define path to 
PATH_RANDOMTRIP = "python3 /home/parallel_user/sumo/tools/randomTrips.py"
PATH_NET = "../sumo/net.net.xml"
PATH_ROUTE = "../sumo/route.rou.xml"

times = 1
while times < 2:    #1h
# while times < 2:  #2h
# while times < 2:  #3h
  command1 = PATH_RANDOMTRIP + " -n" + PATH_NET + " -r " + PATH_ROUTE +" -b " + str(begin) +  " -e " + str(end) + " -p " + str(n) + " -l"

  os.system(command1)

  # Output latitude and longtitude
  command2 = "sumo -c ../sumo/simulation" + str(times) + ".sumo.cfg --fcd-output ../sumo/vehicle" + str(times) +".sumo.xml --fcd-output.geo"

  # Output X Y 
  # command2 = "sumo -c ../sumo/simulation" + str(times) + ".sumo.cfg --fcd-output ../sumo/vehicle" + str(times) +".sumo.xml"

  os.system(command2)

  # Next time to begin += 2000s and end += 2000s
  begin += int(sys.argv[1])
  end += int(sys.argv[1])
  print(f'DONE init_vehicle: vehicle[{times}].sumo.xml file')
  times += 1
