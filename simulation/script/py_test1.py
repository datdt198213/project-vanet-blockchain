import pandas as pd
import numpy as np

# Đọc dữ liệu từ tệp CSV
distance = 1000
num = 200
for i in range(1, 4):
    time = 1
    for j in range(1, 5):
        file_name = f'../data/vehicle_{num}_{distance}_{time}h.csv'
        df = pd.read_csv(file_name, header=None, names=['timeslot', 'distance_total', 'distance'])

        # Tính trung bình và độ lệch chuẩn của cột 'distance_total'
        average_distance = df['distance_total'].mean()
        std_dev_distance = df['distance_total'].std()

        # In kết quả
        print(f'\nAverage {file_name}: {average_distance}')
        print(f'Standard Deviation {file_name}: {std_dev_distance}')
        time += 1
    distance += 500
