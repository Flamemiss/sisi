# batch_rename.py
"""
批量重命名文件
"""
import os
from pathlib import Path

def add_prefix(folder_path, prefix):
    """给所有文件添加前缀"""
    folder = Path(folder_path)
    
    for file in folder.iterdir():
        if file.is_file():
            new_name = f"{prefix}{file.name}"
            file.rename(folder / new_name)
            print(f"重命名: {file.name} → {new_name}")

def add_number(folder_path, start=1, digits=3):
    """给文件添加编号"""
    folder = Path(folder_path)
    files = sorted([f for f in folder.iterdir() if f.is_file()])
    
    for i, file in enumerate(files, start=start):
        number = str(i).zfill(digits)  # 补零
        new_name = f"{number}_{file.name}"
        file.rename(folder / new_name)
        print(f"重命名: {file.name} → {new_name}")

def replace_in_name(folder_path, old_str, new_str):
    """替换文件名中的字符串"""
    folder = Path(folder_path)
    
    for file in folder.iterdir():
        if file.is_file() and old_str in file.name:
            new_name = file.name.replace(old_str, new_str)
            file.rename(folder / new_name)
            print(f"重命名: {file.name} → {new_name}")

# 使用示例
if __name__ == "__main__":
    # 测试文件夹
    test_folder = "./test_rename"
    
    # 创建测试文件夹和文件
    os.makedirs(test_folder, exist_ok=True)
    for i in range(5):
        Path(f"{test_folder}/photo_{i}.jpg").touch()
    
    print("=== 添加前缀 ===")
    add_prefix(test_folder, "2024_")
    
    # 或者添加编号
    # add_number(test_folder)
