import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu
categories = ['30p', '1h', '1h30', '2h', '2h30']
node_pod = [0, 0, 0, 4, 0] # Tọa độ x của hai điểm
total_node = [104, 111, 116, 111, 113]

node_non_pod = [0,0,0,0,0] # Tọa độ y của hai điểm
for i in range(0,5):
    node_non_pod[i] = total_node[i] - node_pod[i]

# Vẽ biểu đồ cột xếp chồng
plt.bar(categories, node_pod, label='POD')
plt.bar(categories, node_non_pod, bottom=node_pod, label='no-POD')

# Đặt tiêu đề cho biểu đồ và trục
plt.title('Number of vehicle received coin with time round = 30p')
plt.xlabel('Time')
plt.ylabel('Number of vehicles')
plt.legend()

# Hiển thị biểu đồ
plt.show()

# Dữ liệu
categories = ['1h', '2h', '3h', '4h', '5h']
node_pod = [3, 7, 0, 2, 2] # Tọa độ x của hai điểm
total_node = [209, 221, 219, 222, 220]

node_non_pod = [0,0,0,0,0] # Tọa độ y của hai điểm
for i in range(0,5):
    node_non_pod[i] = total_node[i] - node_pod[i]

# Vẽ biểu đồ cột xếp chồng
plt.bar(categories, node_pod, label='POD')
plt.bar(categories, node_non_pod, bottom=node_pod, label='no-POD')

# Đặt tiêu đề cho biểu đồ và trục
plt.title('Number of vehicle received coin with time round = 1h')
plt.xlabel('Time')
plt.ylabel('Number of vehicles')
plt.legend()

# Hiển thị biểu đồ
plt.show()


#Time round = 1h30p
# Dữ liệu
categories = ['1h30', '3h', '4h30', '6h', '7h30']
node_pod = [6, 0, 3, 4, 3]
total_node = [321, 323, 330, 321, 330]

node_non_pod = [0,0,0,0,0]
for i in range(0,5):
    node_non_pod[i] = total_node[i] - node_pod[i]

# Vẽ biểu đồ cột xếp chồng
plt.bar(categories, node_pod, label='POD')
plt.bar(categories, node_non_pod, bottom=node_pod, label='no-POD')

# Đặt tiêu đề cho biểu đồ và trục
plt.title('Number of vehicle received coin with time round = 1h30')
plt.xlabel('Time')
plt.ylabel('Number of vehicles')
plt.legend()

# Hiển thị biểu đồ
plt.show()