# read_csv.py
import pandas as pd

# 读取CSV
df = pd.read_csv('students.csv')

# 查看前5行
print("=== 数据预览 ===")
print(df.head())

# 查看数据信息
print("\n=== 数据信息 ===")
print(f"行数: {len(df)}")
print(f"列名: {list(df.columns)}")
