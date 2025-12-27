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
