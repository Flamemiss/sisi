# filter_data.py
import pandas as pd

df = pd.read_csv('students.csv')

# 筛选语文成绩大于80的学生
print("=== 语文成绩 > 80 ===")
high_chinese = df[df['语文'] > 80]
print(high_chinese)

# 筛选数学成绩大于90的学生
print("\n=== 数学成绩 > 90 ===")
high_math = df[df['数学'] > 90]
print(high_math)

# 多条件筛选：语文和数学都大于85
print("\n=== 语文和数学都 > 85 ===")
excellent = df[(df['语文'] > 85) & (df['数学'] > 85)]
print(excellent)
