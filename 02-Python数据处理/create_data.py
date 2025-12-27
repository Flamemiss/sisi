# create_data.py - 创建测试数据
import pandas as pd

data = {
    '姓名': ['张三', '李四', '王五', '赵六', '钱七', '孙八'],
    '语文': [85, 92, 78, 95, 68, 88],
    '数学': [90, 85, 92, 88, 75, 95],
    '英语': [88, 90, 85, 92, 80, 78]
}

df = pd.DataFrame(data)
df.to_csv('students.csv', index=False, encoding='utf-8-sig')
df.to_excel('students.xlsx', index=False)
print("测试数据已创建！")
