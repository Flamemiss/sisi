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
