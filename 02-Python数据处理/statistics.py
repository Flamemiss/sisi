# statistics.py
import pandas as pd

df = pd.read_csv('students.csv')

# 计算总分
df['总分'] = df['语文'] + df['数学'] + df['英语']

# 计算平均分
df['平均分'] = df['总分'] / 3

print("=== 添加计算列后的数据 ===")
print(df)

# 统计信息
print("\n=== 各科统计 ===")
print(f"语文 - 平均:{df['语文'].mean():.1f}, 最高:{df['语文'].max()}, 最低:{df['语文'].min()}")
print(f"数学 - 平均:{df['数学'].mean():.1f}, 最高:{df['数学'].max()}, 最低:{df['数学'].min()}")
print(f"英语 - 平均:{df['英语'].mean():.1f}, 最高:{df['英语'].max()}, 最低:{df['英语'].min()}")

# 按总分排序
print("\n=== 按总分排名 ===")
df_sorted = df.sort_values('总分', ascending=False)
print(df_sorted[['姓名', '总分', '平均分']])
