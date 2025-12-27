# export_data.py
import pandas as pd

df = pd.read_csv('students.csv')

# 添加计算列
df['总分'] = df['语文'] + df['数学'] + df['英语']
df['平均分'] = round(df['总分'] / 3, 1)

# 按总分排序
df = df.sort_values('总分', ascending=False)

# 添加排名
df['排名'] = range(1, len(df) + 1)

# 导出为新文件
df.to_csv('students_result.csv', index=False, encoding='utf-8-sig')
df.to_excel('students_result.xlsx', index=False)

print("结果已保存到 students_result.csv 和 students_result.xlsx")
