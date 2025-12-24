# 任务8：Python自动化脚本

## 🎯 任务目标

学会用Python编写自动化脚本，解决日常重复性工作。

---

## 📋 验收标准

| 序号 | 验收项目 | 具体要求 |
|------|----------|----------|
| 1 | 文件整理 | 自动按扩展名分类整理文件 |
| 2 | 批量重命名 | 批量给文件添加前缀或编号 |
| 3 | 文本处理 | 自动查找替换文件内容 |
| 4 | 定时提醒 | 创建简单的定时提醒工具 |
| 5 | 命令行工具 | 脚本能接收命令行参数 |

---

## 🛠️ 常用库

Python内置库，无需安装：

- `os` - 操作系统接口
- `shutil` - 高级文件操作
- `pathlib` - 路径处理
- `time` / `datetime` - 时间处理
- `argparse` - 命令行参数

---

## 📝 练习任务

### 练习1：文件自动整理

```python
# file_organizer.py
"""
自动整理下载文件夹
按文件类型分类到不同文件夹
"""
import os
import shutil
from pathlib import Path

# 文件类型分类规则
FILE_TYPES = {
    "图片": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "文档": [".doc", ".docx", ".pdf", ".txt", ".xlsx", ".pptx"],
    "视频": [".mp4", ".avi", ".mkv", ".mov", ".wmv"],
    "音乐": [".mp3", ".wav", ".flac", ".aac"],
    "压缩包": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "程序": [".exe", ".msi", ".dmg"],
}

def get_category(extension):
    """根据扩展名获取分类"""
    ext = extension.lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "其他"

def organize_folder(folder_path):
    """整理指定文件夹"""
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"文件夹不存在: {folder_path}")
        return
    
    moved_count = 0
    
    for file in folder.iterdir():
        # 跳过文件夹
        if file.is_dir():
            continue
        
        # 获取分类
        category = get_category(file.suffix)
        
        # 创建分类文件夹
        category_folder = folder / category
        category_folder.mkdir(exist_ok=True)
        
        # 移动文件
        dest = category_folder / file.name
        
        # 处理同名文件
        if dest.exists():
            base = file.stem
            ext = file.suffix
            counter = 1
            while dest.exists():
                dest = category_folder / f"{base}_{counter}{ext}"
                counter += 1
        
        shutil.move(str(file), str(dest))
        print(f"移动: {file.name} → {category}/")
        moved_count += 1
    
    print(f"\n完成！共整理 {moved_count} 个文件")

if __name__ == "__main__":
    # 整理下载文件夹（修改为你的路径）
    downloads = Path.home() / "Downloads"
    
    print(f"即将整理: {downloads}")
    confirm = input("确认执行？(y/n): ")
    
    if confirm.lower() == 'y':
        organize_folder(downloads)
    else:
        print("已取消")
```

### 练习2：批量重命名

```python
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
```

### 练习3：批量文本替换

```python
# text_replace.py
"""
批量查找替换文件内容
"""
from pathlib import Path
import re

def replace_in_file(file_path, old_text, new_text, use_regex=False):
    """替换单个文件中的文本"""
    file = Path(file_path)
    
    try:
        content = file.read_text(encoding='utf-8')
        
        if use_regex:
            new_content = re.sub(old_text, new_text, content)
        else:
            new_content = content.replace(old_text, new_text)
        
        if content != new_content:
            file.write_text(new_content, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"处理文件失败 {file_path}: {e}")
        return False

def batch_replace(folder_path, old_text, new_text, extensions=None):
    """批量替换文件夹中的文本"""
    folder = Path(folder_path)
    
    if extensions is None:
        extensions = ['.txt', '.py', '.js', '.html', '.css', '.md']
    
    modified_count = 0
    
    for file in folder.rglob('*'):  # 递归遍历
        if file.is_file() and file.suffix in extensions:
            if replace_in_file(file, old_text, new_text):
                print(f"已修改: {file}")
                modified_count += 1
    
    print(f"\n完成！共修改 {modified_count} 个文件")

# 使用示例
if __name__ == "__main__":
    # 示例：将所有 "TODO" 替换为 "DONE"
    # batch_replace("./my_project", "TODO", "DONE", ['.py'])
    
    # 示例：替换版本号
    # batch_replace("./", "v1.0.0", "v2.0.0", ['.py', '.md'])
    
    print("请修改代码中的参数后运行")
```

### 练习4：定时提醒工具

```python
# reminder.py
"""
简单的定时提醒工具
"""
import time
from datetime import datetime, timedelta

def countdown_timer(seconds, message="时间到！"):
    """倒计时提醒"""
    print(f"倒计时开始: {seconds} 秒")
    print(f"提醒内容: {message}\n")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r剩余时间: {timer}", end="", flush=True)
        time.sleep(1)
        seconds -= 1
    
    print(f"\n\n{'='*30}")
    print(f"⏰ {message}")
    print(f"{'='*30}")
    
    # Windows系统蜂鸣声
    try:
        import winsound
        winsound.Beep(1000, 500)  # 频率1000Hz，持续500ms
    except:
        print('\a')  # 通用蜂鸣

def time_reminder(target_time, message="时间到！"):
    """定时提醒（指定时间）"""
    # 解析目标时间
    if isinstance(target_time, str):
        target = datetime.strptime(target_time, "%H:%M")
        target = target.replace(
            year=datetime.now().year,
            month=datetime.now().month,
            day=datetime.now().day
        )
    else:
        target = target_time
    
    now = datetime.now()
    
    if target < now:
        print("目标时间已过！")
        return
    
    wait_seconds = (target - now).total_seconds()
    print(f"将在 {target.strftime('%H:%M:%S')} 提醒你")
    print(f"还需等待 {int(wait_seconds)} 秒")
    
    countdown_timer(int(wait_seconds), message)

# 使用示例
if __name__ == "__main__":
    print("=== 定时提醒工具 ===")
    print("1. 倒计时（分钟）")
    print("2. 指定时间")
    
    choice = input("\n选择模式 (1/2): ")
    
    if choice == "1":
        minutes = int(input("倒计时分钟数: "))
        message = input("提醒内容: ") or "时间到！"
        countdown_timer(minutes * 60, message)
    
    elif choice == "2":
        time_str = input("目标时间 (格式 HH:MM): ")
        message = input("提醒内容: ") or "时间到！"
        time_reminder(time_str, message)
```

### 练习5：命令行工具

```python
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
```

---

## 🔧 常用技巧

### 路径处理

```python
from pathlib import Path

# 当前目录
current = Path.cwd()

# 用户目录
home = Path.home()

# 拼接路径
downloads = home / "Downloads"

# 遍历文件
for file in downloads.iterdir():
    print(file.name)

# 递归遍历
for file in downloads.rglob("*.txt"):
    print(file)
```

### 文件操作

```python
import shutil

# 复制文件
shutil.copy("src.txt", "dst.txt")

# 移动文件
shutil.move("old.txt", "new/old.txt")

# 删除文件夹（包含内容）
shutil.rmtree("folder_to_delete")
```

---

## ✅ 自测清单

- [ ] 知道 `Path` 和 `os` 的基本用法吗？
- [ ] 能遍历文件夹中的所有文件吗？
- [ ] 能用 `shutil` 复制和移动文件吗？
- [ ] 知道 `argparse` 如何添加命令行参数吗？
- [ ] 能编写自己的自动化脚本吗？

---

## 📚 推荐资源

- Python pathlib文档：https://docs.python.org/zh-cn/3/library/pathlib.html
- Python shutil文档：https://docs.python.org/zh-cn/3/library/shutil.html
- argparse教程：https://docs.python.org/zh-cn/3/howto/argparse.html
