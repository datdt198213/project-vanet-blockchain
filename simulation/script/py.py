# import csv

# def check_number_of_lines(file_path, expected_lines):
#     with open(file_path, 'r', newline='', encoding='utf-8') as file:
#         reader = csv.reader(file)
#         lines = sum(1 for row in reader)
#         return lines == expected_lines

# def main():
#     num = 90
#     file_paths = []
#     # Danh sách các tệp tin CSV cần kiểm tra
#     for i in range(1, 6):
#         for j in range(1, 22):
#             file_path = f'../data/data_test_{num}.csv'
#             file_paths.append(file_path)
#             num+=1
#         num+= 79
#     # file_paths = ['file1.csv', 'file2.csv', 'file3.csv', ...]  # Thêm tên các tệp tin của bạn vào đây

#     expected_lines = 111

#     for file_path in file_paths:
#         result = check_number_of_lines(file_path, expected_lines)
#         print(f'{file_path}: {result}')

# if __name__ == '__main__':
#     main()


# import csv

# def reverse_second_row(file_path):
#     with open(file_path, 'r', newline='', encoding='utf-8') as file:
#         lines = list(csv.reader(file))

#     # Nếu có ít nhất 3 dòng trong tệp tin
#     if len(lines) >= 3:
#         # Đảo ngược dòng thứ hai
#         lines[1], lines[-1] = lines[-1], lines[1]

#         # Ghi lại vào tệp tin
#         with open(file_path, 'w', newline='', encoding='utf-8') as file:
#             writer = csv.writer(file)
#             writer.writerows(lines)

# # Thay đổi tên tệp tin thành tên thực tế của tệp tin CSV bạn đang sử dụng
# file_path = '../data/data_test_190.csv'
# reverse_second_row(file_path)

import csv

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

num = 90
for i in range(1,6):
    for i in range(1,22):
        file_path = f'../data/data_test_{num}.csv'
        merge_and_sort(file_path)
        print(f"Done data_test_{num}.csv")
        num+=1
    num+=79

