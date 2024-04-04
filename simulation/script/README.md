A. Running simulation and preprocessing data
1. Create simulation 

```
python3 py_init_simulation ending_time num_vehicle
```
ending_time: Thời gian kết thúc của mô phỏng <br>
num_vehicle: Số lượng xe trong mô phỏng

2. Init vehicle
```
python3 py_init_vehicle.py ending_time num_vehicle
```
ending_time: Thời gian kết thúc của mô phỏng <br>
num_vehicle: Số lượng xe trong mô phỏng

3. Convert data from XML to JSON
```
python3 py_convert_data.py ending_time num_vehicle
```
ending_time: Thời gian kết thúc của mô phỏng <br>
num_vehicle: Số lượng xe trong mô phỏng

B. Processing data
1. POD coin average algorithm
```
node JSAddHeader_v1.js num_vehicle
node JSMinerLargeFile_v1.js num_vehicle
```
num_vehicle: Số lượng xe trong mô phỏng

2. POD distance average algorithm
```
node JSAddHeader_v2.js num_vehicle
node JSMinerLargeFile_v2.js num_vehicle
```
num_vehicle: Số lượng xe trong mô phỏng

3. POD accumulate distance average algorithm
```
node JSAddHeader_v3.js num_vehicle
node JSMinerLargeFile_v3.js num_vehicle
```
num_vehicle: Số lượng xe trong mô phỏng

4. Calculate distance of vehicles in 1 hours
```
node JSCalculateDistance.js num_vehicle
```
num_vehicle: Số lượng xe trong mô phỏng

C. Statistic
1. Statistic the number of vehicles which satisfy conditions of algorithm v2 in 1 hours
Using function statistic_difference(num) in file py_draw_result_comparision.py
```
python3 py_draw_result_comparision.py
```
2. Statistic the fixed threshold of v1
Using function statistic_rate_difference(num) in file py_draw_result_comparision.py
```
python3 py_draw_result_comparision.py
```
3. Statistic the difference of fixed and dynamic threshold of v1 and v2 
Using function statistic_rate_difference_dynamic(num) in file py_draw_result_comparision.py
```
python3 py_draw_result_comparision.py
```
4. Statistic distance of vehicles
```
python3 py_draw_result_distance.py
```