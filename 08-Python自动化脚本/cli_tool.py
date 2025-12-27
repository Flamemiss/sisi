# cli_tool.py
"""
命令行工具示例
使用 argparse 处理参数
"""
import argparse
from pathlib import Path

def count_lines(file_path):
    """统计文件行数"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except Exception as e:
        return f"错误: {e}"

def count_folder(folder_path, extension=None):
    """统计文件夹中的代码行数"""
    folder = Path(folder_path)
    total_lines = 0
    file_count = 0
    
    for file in folder.rglob('*'):
        if file.is_file():
            if extension and file.suffix != extension:
                continue
            
            lines = count_lines(file)
            if isinstance(lines, int):
                total_lines += lines
                file_count += 1
                print(f"{file.name}: {lines} 行")
    
    return total_lines, file_count

def main():
    parser = argparse.ArgumentParser(description='代码统计工具')
    
    # 添加参数
    parser.add_argument('path', help='文件或文件夹路径')
    parser.add_argument('-e', '--ext', help='只统计指定扩展名（如 .py）')
    parser.add_argument('-v', '--verbose', action='store_true', help='显示详细信息')
    
    args = parser.parse_args()
    
    path = Path(args.path)
    
    if path.is_file():
        lines = count_lines(path)
        print(f"文件: {path.name}")
        print(f"行数: {lines}")
    
    elif path.is_dir():
        if args.verbose:
            print(f"统计文件夹: {path}\n")
        
        total, count = count_folder(path, args.ext)
        
        print(f"\n{'='*30}")
        print(f"文件数: {count}")
        print(f"总行数: {total}")
    
    else:
        print(f"路径不存在: {path}")

if __name__ == "__main__":
    main()

# 使用方法：
# python cli_tool.py ./my_project
# python cli_tool.py ./my_project -e .py
# python cli_tool.py ./my_project -e .py -v
