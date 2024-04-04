import pandas as pd
import matplotlib.pyplot as plt


# Đọc dữ liệu từ tệp CSV
file_path = '../data/Result_statistic_distance/data_distance_20.csv'  # Điều chỉnh đường dẫn tệp CSV của bạn
df = pd.read_csv(file_path)

# Chọn các dòng có begin là 0 và end là 3599.9
# Chọn các dòng có begin là 25200 và end là 28799.9
selected_rows = df[(df['Begin'] == 25200) & (df['End'] == 28799.9)]

# Sắp xếp DataFrame theo cột 'id'
sorted_df = selected_rows.sort_values('ID')

# In ra kết quả
# print(sorted_df[['Timslot', 'begin', 'end', 'id', 'distance']])

average_distance = sorted_df['Distance'].mean()
print(average_distance)

yticks = [20000, 25000, 30000, 35000]
plt.scatter(sorted_df['ID'], sorted_df['Distance'])
# plt.title('Accumulated distance of 20 vehicles in 1 hours')
plt.xlabel('ID')
plt.yticks(yticks)
plt.xticks(sorted_df['ID'])
plt.ylabel('Distance (m)')
plt.show()