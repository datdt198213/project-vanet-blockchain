import xml.etree.ElementTree as ET

# Tạo dữ liệu 1 chuyến đi dài 
def merge_routes(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    vehicles = root.findall('vehicle')
    routes = [vehicle.find('route').get('edges').split() for vehicle in vehicles]
    count = 0 
    
    while (len(routes[1]) < 3000):
        merged_route = routes[1]
        for i in range(1, len(routes)):
            if count == 10:  # Dừng nếu đã nối đủ 10 phần tử
                break

            last_edge_of_first_route = merged_route[-1]

            if last_edge_of_first_route in routes[i]:
                # Tìm vị trí nối
                merge_index = routes[i].index(last_edge_of_first_route)
                
                # Nối các route
                merged_route += routes[i][merge_index + 1:]
                count += 1
            
        # Replace route 0 in XML
        vehicles[1].find('route').set('edges', " ".join(merged_route))
        tree.write(file_path, encoding='utf-8', xml_declaration=True)
    
my_str = merge_routes("./day2_route100.rou.xml")
print(my_str)