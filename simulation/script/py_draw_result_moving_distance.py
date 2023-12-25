import pandas as pd
import matplotlib.pyplot as plt


# Đọc dữ liệu từ tệp CSV
file_path = '../data/data_v3_10.csv'  # Điều chỉnh đường dẫn tệp CSV của bạn
df = pd.read_csv(file_path)

# Chọn các dòng có begin là 0 và end là 3599.9
selected_rows = df[(df['begin'] == 0) & (df['end'] == 3599.9)]

# Sắp xếp DataFrame theo cột 'id'
sorted_df = selected_rows.sort_values('id')

# In ra kết quả
# print(sorted_df[['Timslot', 'begin', 'end', 'id', 'distance']])

average_distance = sorted_df['distance'].mean()
print(average_distance)

plt.scatter(sorted_df['id'], sorted_df['distance'], alpha=0.5)
plt.title('Moving distance of 10 vehicles in 1 hours')
plt.xlabel('ID')
plt.ylabel('Distance (m)')
plt.show()