import csv
import os

def check_number_of_lines(file_path, expected_lines):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        lines = sum(1 for row in reader)
        return lines == expected_lines

def check():
    num = 90
    file_paths = []
    for i in range(1, 6):
        for j in range(1, 22):
            file_path = f'../data/data_v1_{num}.csv'
            file_paths.append(file_path)
            num+=1
        num+= 79

    expected_lines = 111

    for file_path in file_paths:
        result = check_number_of_lines(file_path, expected_lines)
        print(f'{file_path}: {result}')

def merge_and_sort(file_path):
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        lines = list(csv.reader(file))

    # Sắp xếp theo cột "Begin" (cột thứ hai, index 1)
    lines[1:] = sorted(lines[1:], key=lambda x: float(x[1]))

    # Gộp dữ liệu với cùng giá trị của cột "Distance" (cột thứ tư, index 3)
    merged_lines = {}
    for line in lines[1:]:
        distance = float(line[3])
        if distance not in merged_lines:
            merged_lines[distance] = [line]
        else:
            merged_lines[distance].append(line)

    # Ghi lại vào tệp tin
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(lines[0])  # Ghi lại dòng tiêu đề
        for distance in sorted(merged_lines.keys()):
            writer.writerows(merged_lines[distance])

def sort(version, num):
    # num = 90
    # for i in range(1,6):
    #     for i in range(1,22):
    #         file_path = f'../data/data_v1_{num}.csv'
    #         merge_and_sort(file_path)
    #         print(f"Done data_v1_{num}.csv")
    #         num+=1
    #     num+=79
    file_path = f'../data/data_{version}_{num}.csv'
    merge_and_sort(file_path)
    print(f"Done data_{version}_{num}.csv")


# Thay đổi tên file từ "old_file.csv" thành "new_file.csv"
# rename_csv_file(f"..data/data_test_{number}.csv", f"../data/data_v2_{number}.csv")
def rename_csv_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Đã đổi tên file {old_name} thành {new_name} thành công.")
    except FileNotFoundError:
        print(f"File {old_name} không tồn tại.")
    except Exception as e:
        print(f"Lỗi khi đổi tên file: {e}")


if __name__ == '__main__':
    num = 20
    version = "v1"
    sort(version, num)
    version = "v2"
    sort(version, num)
    