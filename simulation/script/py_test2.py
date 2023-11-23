# import xml.etree.ElementTree as ET

# # Đọc tệp XML
# tree = ET.parse('trips.trips.xml')
# root = tree.getroot()

# # Lấy danh sách các trip
# trips = root.findall('trip')

# # Tạo một từ điển để lưu 'to' của mỗi trip
# to_dict = {}

# for trip in trips:
#     trip_id = trip.get('id')
#     trip_to = trip.get('to')
#     to_dict[trip_id] = trip_to

# # Tìm bắt đầu ('from') của mỗi trip là 'to' của trip khác
# start_of_trip = {}

# for trip in trips:
#     trip_id = trip.get('id')
#     trip_from = trip.get('from')

#     # Kiểm tra xem 'to' của trip này có là 'from' của trip khác hay không
#     matching_trip_id = next((tid for tid, tto in to_dict.items() if tto == trip_from), None)

#     if matching_trip_id:
#         start_of_trip[trip_id] = matching_trip_id
#         trip.set('id', matching_trip_id)

# # In kết quả
# for trip_id, start_trip_id in start_of_trip.items():
#     print(f"Trip {trip_id}: Start from trip {start_trip_id}")

# # Lưu tệp XML mới
# tree.write('new_routes1.rou.xml')

# import xml.etree.ElementTree as ET

# # Đọc tệp XML
# tree = ET.parse('new_routes1.rou.xml')
# root = tree.getroot()

# # Lấy danh sách các trip và sắp xếp chúng theo trip id
# trips = sorted(root.findall('trip'), key=lambda trip: int(trip.get('id')))

# # Xóa tất cả các trip từ root
# for trip in root.findall('trip'):
#     root.remove(trip)

# # Thêm lại các trip đã sắp xếp vào root
# for trip in trips:
#     root.append(trip)

# # Lưu tệp XML mới
# tree.write('new_routes_sorted.rou.xml')

# import xml.etree.ElementTree as ET

# # Đọc tệp XML
# tree = ET.parse('new_routes_random_ids.rou.xml')
# root = tree.getroot()

# # Lấy danh sách các trip
# trips = root.findall('trip')

# # Tạo một tập hợp để lưu trữ các ID duy nhất
# unique_ids = set()

# # Lặp qua các trip và thêm ID vào tập hợp
# for trip in trips:
#     unique_ids.add(trip.get('id'))

# # Đếm số lượng ID duy nhất
# num_unique_ids = len(unique_ids)

# print(f"Số lượng ID còn lại: {num_unique_ids}")

# import xml.etree.ElementTree as ET
# import random

# # Đọc tệp XML
# tree = ET.parse('new_routes1.rou.xml')
# root = tree.getroot()

# # Lấy danh sách các trip
# trips = root.findall('trip')

# # Chọn ngẫu nhiên 100 ID
# selected_ids = random.sample([trip.get('id') for trip in trips], 100)

# # Lặp qua các trip và giữ lại chỉ các trip có ID thuộc danh sách đã chọn
# new_trips = [trip for trip in trips if trip.get('id') in selected_ids]

# # Xóa tất cả các trip từ root
# for trip in root.findall('trip'):
#     root.remove(trip)

# # Thêm lại các trip mới vào root
# for trip in new_trips:
#     root.append(trip)

# # Lưu tệp XML mới
# tree.write('new_routes_100_ids.rou.xml')

# import xml.etree.ElementTree as ET
# import random

# Đọc tệp XML
# tree = ET.parse('new_routes1.rou.xml')
# root = tree.getroot()

# # Lấy danh sách các trip
# trips = root.findall('trip')

# # Tạo một danh sách chứa các ID mới từ 1 đến 100
# new_ids = list(range(1, 101))

# # Lặp qua các trip và gán ID mới ngẫu nhiên
# for trip in trips:
#     new_id = random.choice(new_ids)
#     trip.set('id', str(new_id))
#     # new_ids.remove(new_id)  # Đảm bảo ID không được tái sử dụng

# # Lưu tệp XML mới
# tree.write('new_routes_random_ids.rou.xml')

import xml.etree.ElementTree as ET

# Đọc tệp .rou.xml
tree = ET.parse('trip.rou.xml')
root = tree.getroot()

# Tạo một tệp .add.xml mới
add_xml = ET.Element('routes')

# Thêm định nghĩa loại xe 'car'
v_type = ET.SubElement(add_xml, 'vType', id='car', accel='2.6', decel='4.5', sigma='0.5', length='4.5', minGap='2.5', maxSpeed='50')

# Lặp qua từng trip và thêm vào tệp .add.xml
for trip in root.findall('trip'):
    vehicle_id = trip.get('id')
    depart_time = trip.get('depart')
    from_edge = trip.get('from')
    to_edge = trip.get('to')

    # Tạo phần tử vehicle trong tệp .add.xml
    vehicle = ET.SubElement(add_xml, 'vehicle', id=f'{vehicle_id}', type='car', depart=depart_time, color='1,0,0')
    route = ET.SubElement(vehicle, 'route', edges=f'{from_edge} {to_edge}')

# Lưu tệp .add.xml
add_tree = ET.ElementTree(add_xml)
add_tree.write('my_routes.add.xml')