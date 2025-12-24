# 任务9：Markdown文档写作

## 🎯 任务目标

学会使用Markdown语法编写规范的技术文档和笔记。

---

## 📋 验收标准

| 序号 | 验收项目 | 具体要求 |
|------|----------|----------|
| 1 | 标题层级 | 正确使用 1-6 级标题 |
| 2 | 文本格式 | 使用粗体、斜体、删除线 |
| 3 | 列表使用 | 有序列表和无序列表 |
| 4 | 代码展示 | 行内代码和代码块 |
| 5 | 链接图片 | 插入链接和图片 |
| 6 | 表格制作 | 创建简单表格 |
| 7 | 完整文档 | 编写一份完整的项目README |

---

## 🛠️ 编辑工具

### 推荐编辑器

- **VS Code**：安装 Markdown Preview 插件
- **Typora**：所见即所得编辑器
- **Mark Text**：开源免费
- **在线工具**：https://markdownlivepreview.com/

---

## 📝 语法教程

### 1. 标题

```markdown
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

### 2. 文本格式

```markdown
**粗体文字**

*斜体文字*

***粗斜体***

~~删除线~~

`行内代码`
```

效果：**粗体**、*斜体*、***粗斜体***、~~删除线~~、`行内代码`

### 3. 列表

**无序列表**：

```markdown
- 项目1
- 项目2
  - 子项目2.1
  - 子项目2.2
- 项目3
```

**有序列表**：

```markdown
1. 第一步
2. 第二步
3. 第三步
```

**任务列表**：

```markdown
- [x] 已完成任务
- [ ] 未完成任务
- [ ] 待办事项
```

### 4. 链接和图片

```markdown
[链接文字](https://www.example.com)

[带标题的链接](https://www.example.com "鼠标悬停显示")

![图片描述](image.jpg)

![网络图片](https://example.com/image.png)
```

### 5. 代码

**行内代码**：

```markdown
使用 `print()` 函数输出内容
```

**代码块**：

````markdown
```python
def hello():
    print("Hello, World!")
```
````

**支持的语言标识**：python, javascript, html, css, json, bash, sql 等

### 6. 表格

```markdown
| 姓名 | 年龄 | 城市 |
|------|------|------|
| 张三 | 25   | 北京 |
| 李四 | 30   | 上海 |
| 王五 | 28   | 广州 |
```

**对齐方式**：

```markdown
| 左对齐 | 居中 | 右对齐 |
|:-------|:----:|-------:|
| 左     | 中   |     右 |
```

### 7. 引用

```markdown
> 这是一段引用文字
> 
> 可以多行

> 引用可以嵌套
>> 二级引用
>>> 三级引用
```

### 8. 分割线

```markdown
---
或
***
或
___
```

### 9. 转义字符

如果要显示 Markdown 语法字符本身，使用反斜杠：

```markdown
\*这不是斜体\*
\# 这不是标题
```

---

## 📝 练习任务

### 练习1：个人简介

创建 `about-me.md`：

```markdown
# 关于我

## 基本信息

- **姓名**：你的名字
- **职业**：学生/程序员
- **城市**：你的城市

## 技能清单

### 正在学习

- [ ] Python
- [ ] HTML/CSS
- [x] Markdown

### 已掌握

- Microsoft Office
- 基本电脑操作

## 座右铭

> 学无止境，每天进步一点点！

---

*最后更新：2024年*
```

### 练习2：学习笔记

创建 `notes.md`：

```markdown
# Python学习笔记

## 第一章：基础语法

### 1.1 变量

Python中定义变量不需要声明类型：

```python
name = "张三"
age = 25
is_student = True
```

### 1.2 数据类型

| 类型 | 说明 | 示例 |
|------|------|------|
| int | 整数 | `10` |
| float | 浮点数 | `3.14` |
| str | 字符串 | `"hello"` |
| bool | 布尔值 | `True` |
| list | 列表 | `[1, 2, 3]` |

### 1.3 常用函数

- `print()` - 输出内容
- `input()` - 获取输入
- `len()` - 获取长度
- `type()` - 获取类型

## 参考链接

- [Python官方文档](https://docs.python.org/zh-cn/3/)
- [菜鸟教程](https://www.runoob.com/python3/)
```

### 练习3：项目README

创建 `project-readme.md`：

```markdown
# 项目名称

简短描述这个项目是做什么的。

## 功能特性

- ✅ 功能1
- ✅ 功能2
- 🚧 功能3（开发中）

## 快速开始

### 环境要求

- Python 3.8+
- Windows 10/11

### 安装步骤

1. 克隆项目

```bash
git clone https://github.com/username/project.git
```

2. 安装依赖

```bash
pip install -r requirements.txt
```

3. 运行程序

```bash
python main.py
```

## 使用示例

```python
from myproject import hello

hello("世界")
# 输出: 你好，世界！
```

## 项目结构

```
project/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   └── test_main.py
├── README.md
└── requirements.txt
```

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 联系方式

- 邮箱：example@email.com
- GitHub：[@username](https://github.com/username)
```

---

## 💡 写作技巧

### 好的文档应该

1. **结构清晰**：使用标题层级组织内容
2. **重点突出**：使用粗体、列表强调关键信息
3. **代码规范**：代码块标注语言，便于阅读
4. **图文并茂**：适当使用图片和表格
5. **保持简洁**：避免冗长，直奔主题

### 常见文档类型

- **README**：项目介绍和使用说明
- **CHANGELOG**：版本更新记录
- **API文档**：接口说明
- **教程**：步骤式指导
- **笔记**：知识点整理

---

## ✅ 自测清单

- [ ] 能创建多级标题吗？
- [ ] 知道粗体、斜体、删除线怎么写吗？
- [ ] 能创建有序和无序列表吗？
- [ ] 能插入带语法高亮的代码块吗？
- [ ] 能创建表格吗？
- [ ] 能写一份完整的项目README吗？

---

## 📚 推荐资源

- Markdown官方教程：https://markdown.com.cn/
- GitHub Markdown指南：https://docs.github.com/cn/get-started/writing-on-github
- Typora下载：https://typora.io/
