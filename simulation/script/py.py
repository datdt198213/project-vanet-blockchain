import os

def rename_csv_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"Đã đổi tên file {old_name} thành {new_name} thành công.")
    except FileNotFoundError:
        print(f"File {old_name} không tồn tại.")
    except Exception as e:
        print(f"Lỗi khi đổi tên file: {e}")

# Thay đổi tên file từ "old_file.csv" thành "new_file.csv"
number = 90
rename_csv_file(f"..data/data_test_{number}.csv", f"../data/data_v2_{number}.csv")
