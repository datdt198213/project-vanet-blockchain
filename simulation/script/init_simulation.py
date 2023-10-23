import sys

input = "../sumo/simulation.sumo.cfg"

with open(input) as file:
    
    lines = file.readlines()

    # Set time running simulation, 0 - 2000s 
    begin = 0
    end = int(sys.argv[1]) # Read parameter from command
    n = int(sys.argv[2])
    times = str(end) + "_" + str(int(end/n))

    for i in range(len(lines)):
      if '<begin value="' in lines[i]:
        temp = lines[i].split('"')
        temp[1] = str(begin)
        str_temp = '"'.join(temp)
        lines[i] = str_temp
        begin += int(sys.argv[1])
        
      elif '<end value="' in lines[i]:
        temp = lines[i].split('"')
        temp[1] = str(end)
        str_temp = '"'.join(temp)
        lines[i] = str_temp
        end += int(sys.argv[1])

    name_file = "../sumo/simulation" + str(times) + ".sumo.cfg"
    new_file = open(name_file, "w")
    new_file.writelines(lines)
    print(f"DONE init_simulation: simulation[{times}].sumo.cfg file")

    # times = 1
    # while times < 2:    # 1h
    # while times < 3:  # 2h
    # while times < 4:  # 3h

      # for i in range(len(lines)):
      #   if '<begin value="' in lines[i]:
      #     temp = lines[i].split('"')
      #     temp[1] = str(begin)
      #     str_temp = '"'.join(temp)
      #     lines[i] = str_temp
      #     begin += int(sys.argv[1])
          
      #   elif '<end value="' in lines[i]:
      #     temp = lines[i].split('"')
      #     temp[1] = str(end)
      #     str_temp = '"'.join(temp)
      #     lines[i] = str_temp
      #     end += int(sys.argv[1])

      # name_file = "../sumo/simulation" + str(times) + ".sumo.cfg"
      # new_file = open(name_file, "w")
      # new_file.writelines(lines)
      # print(f"DONE init_simulation: simulation[{times}].sumo.cfg file")
      # times += 1

