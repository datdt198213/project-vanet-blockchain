import matplotlib.pyplot as plt
import statistics
import csv

file_path = f'../data/final_result_2.csv'

try:
    with open(file_path, 'w', newline='') as file:
        file.truncate(0)
    print(f"All data in {file_path} has been cleared.")
except Exception as e:
    print(f"An error occurred: {e}")

# Store all data and compute to result file
d = 1000
for i in range(1,12):
    num = 100
    for j in range(1,6):
        csv_file_path = f"../data/v_{num}_d_{d}_2.csv"

        averages = []
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                averages.append(float(row[1]))

        std_dev1 = statistics.stdev(averages)
        mean = statistics.mean(averages)

        file_name = f'../data/final_result_2.csv'
        f = open(file_name, 'a', newline='')
        writer = csv.writer(f)
        writer.writerow([mean, std_dev1, num, d])
        f.close()
        num+=100    
    d+= 100

# Draw graph
csv_file_path = f"../data/final_result_2.csv"

tmp_data = []
tmp_error = []
v = []
d= []
with open(csv_file_path, 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        tmp_data.append(float(row[0]))
        tmp_error.append(float(row[1]))
        v.append(row[2])
        d.append(int(row[3]))


# if distance == 1000:
#     begin = 0
#     end = 5
# elif distance == 1500:
#     begin = 5
#     end = 10  
# elif distance == 2000:
#     begin = 10
#     end = 15

distance = 1000
for temp in range(1000, 2100):
    data = [] 
    error_d = []
    # print(tmp_data)
    for i in range(len(tmp_data)):
        if d[i] == distance:
            data.append(float(tmp_data[i]))
            error_d.append(float(tmp_error[i]))

    x_values = [100, 200, 300, 400, 500]
    m = statistics.mean(data)
    sd = statistics.stdev(data)

    plt.errorbar(x_values, data, yerr=error_d, fmt='o', color='orange', ecolor='red', capsize=5, capthick=2, label='Error Bar')
    # plt.axhline(m, color='k', linestyle='dashed', label='Mean')
    # plt.axhline(m + sd, color='blue', linestyle='dashed', label='Mean + stdev')
    # plt.axhline(m - sd, color='blue', linestyle='dashed', label='Mean - stdev')

    plt.xlabel("Vehicles")
    plt.ylabel("Value")
    plt.title(f"Distance = {distance}, Timeslot = 1h")
    # plt.xticks(x_values, range(100,300))

    plt.legend()
    plt.show()

    result = 0
    for i in tmp_data:
        result += abs(i-m)

    print(result)
    temp+=100
    distance+=100