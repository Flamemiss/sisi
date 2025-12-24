# 任务2：Python数据处理（Excel/CSV）

## 🎯 任务目标

学会用Python读写Excel和CSV文件，进行数据筛选、统计和分析。

---

## 📋 验收标准

| 序号 | 验收项目 | 具体要求 |
|------|----------|----------|
| 1 | 库安装 | 成功安装 pandas 和 openpyxl |
| 2 | 读取CSV | 读取CSV文件并打印前5行 |
| 3 | 读取Excel | 读取Excel文件内容 |
| 4 | 数据筛选 | 按条件筛选数据（如：成绩>80） |
| 5 | 数据统计 | 计算平均值、最大值、最小值 |
| 6 | 导出文件 | 将处理结果保存为新文件 |

---

## 🛠️ 环境准备

### 安装所需库

打开命令提示符，运行：

```
pip install pandas openpyxl -i https://pypi.tuna.tsinghua.edu.cn/simple
```

> 💡 使用清华镜像加速下载

---

## 📝 练习任务

### 准备测试数据

首先创建测试数据文件 `students.csv`：

```python
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
```

### 练习1：读取CSV文件

```python
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
```

### 练习2：读取Excel文件

```python
# read_excel.py
import pandas as pd

# 读取Excel
df = pd.read_excel('students.xlsx')

print("=== Excel数据 ===")
print(df)
```

### 练习3：数据筛选

```python
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
```

### 练习4：数据统计

```python
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
```

### 练习5：导出处理结果

```python
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
```

---

## ✅ 自测清单

- [ ] 能用 `pd.read_csv()` 读取CSV文件吗？
- [ ] 能用 `pd.read_excel()` 读取Excel文件吗？
- [ ] 知道如何用 `df[条件]` 筛选数据吗？
- [ ] 知道 `mean()`, `max()`, `min()` 等统计函数吗？
- [ ] 能用 `to_csv()` 和 `to_excel()` 导出文件吗？

---

## 📚 推荐资源

- Pandas官方文档：https://pandas.pydata.org/docs/
- Pandas中文教程：https://www.pypandas.cn/
