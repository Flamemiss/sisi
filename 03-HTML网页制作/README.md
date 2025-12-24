# 任务3：HTML+CSS个人主页

## 🎯 任务目标

学会HTML和CSS基础，制作一个个人介绍网页。

---

## 📋 验收标准

| 序号 | 验收项目 | 具体要求 |
|------|----------|----------|
| 1 | 页面标题 | 浏览器标签显示自定义标题 |
| 2 | 标题文字 | 页面有大标题（h1）和小标题（h2） |
| 3 | 段落文字 | 至少2段自我介绍文字 |
| 4 | 图片展示 | 页面显示一张图片 |
| 5 | 超链接 | 至少1个可点击的链接 |
| 6 | 样式美化 | 使用CSS设置颜色、字体、背景 |
| 7 | 列表展示 | 用列表展示技能或爱好 |

---

## 🛠️ 开发工具

### 推荐编辑器

- **VS Code**（推荐）：https://code.visualstudio.com/
- 记事本（Windows自带，入门可用）

### 查看网页

直接双击 `.html` 文件，用浏览器打开即可。

---

## 📝 练习任务

### 练习1：第一个HTML页面

创建文件 `first.html`：

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>我的第一个网页</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>这是我的第一个网页！</p>
</body>
</html>
```

用浏览器打开查看效果。

### 练习2：完整个人主页

创建文件 `index.html`：

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>我的个人主页</title>
    <style>
        /* CSS样式写在这里 */
        body {
            font-family: "Microsoft YaHei", sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        
        .header {
            text-align: center;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            border-radius: 10px;
        }
        
        .avatar {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 4px solid white;
        }
        
        .section {
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        h2 {
            color: #667eea;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }
        
        ul {
            list-style-type: none;
            padding: 0;
        }
        
        li {
            padding: 8px 0;
            border-bottom: 1px dashed #eee;
        }
        
        li::before {
            content: "✓ ";
            color: #667eea;
        }
        
        a {
            color: #667eea;
            text-decoration: none;
        }
        
        a:hover {
            text-decoration: underline;
        }
        
        .footer {
            text-align: center;
            color: #888;
            padding: 20px;
        }
    </style>
</head>
<body>
    <!-- 头部区域 -->
    <div class="header">
        <img src="https://via.placeholder.com/150" alt="头像" class="avatar">
        <h1>你的名字</h1>
        <p>一句话介绍自己</p>
    </div>
    
    <!-- 关于我 -->
    <div class="section">
        <h2>关于我</h2>
        <p>你好！我是一名正在学习编程的新手。</p>
        <p>我对技术充满热情，希望通过学习能够创造出有趣的作品。</p>
    </div>
    
    <!-- 我的技能 -->
    <div class="section">
        <h2>正在学习的技能</h2>
        <ul>
            <li>Python 编程</li>
            <li>HTML/CSS 网页制作</li>
            <li>JavaScript 交互开发</li>
            <li>数据分析处理</li>
        </ul>
    </div>
    
    <!-- 我的爱好 -->
    <div class="section">
        <h2>我的爱好</h2>
        <ul>
            <li>阅读技术书籍</li>
            <li>看电影</li>
            <li>打游戏</li>
        </ul>
    </div>
    
    <!-- 联系方式 -->
    <div class="section">
        <h2>联系我</h2>
        <p>邮箱：<a href="mailto:example@email.com">example@email.com</a></p>
        <p>GitHub：<a href="https://github.com" target="_blank">github.com/yourname</a></p>
    </div>
    
    <!-- 页脚 -->
    <div class="footer">
        <p>© 2024 我的个人主页 | 用 ❤️ 制作</p>
    </div>
</body>
</html>
```

---

## 🎨 CSS常用属性速查

| 属性 | 作用 | 示例 |
|------|------|------|
| `color` | 文字颜色 | `color: red;` |
| `background-color` | 背景颜色 | `background-color: #f5f5f5;` |
| `font-size` | 字体大小 | `font-size: 16px;` |
| `padding` | 内边距 | `padding: 20px;` |
| `margin` | 外边距 | `margin: 10px;` |
| `border` | 边框 | `border: 1px solid black;` |
| `border-radius` | 圆角 | `border-radius: 10px;` |
| `text-align` | 文字对齐 | `text-align: center;` |

---

## ✅ 自测清单

- [ ] 知道 `<h1>` 到 `<h6>` 是标题标签吗？
- [ ] 知道 `<p>` 是段落、`<a>` 是链接、`<img>` 是图片吗？
- [ ] 知道CSS如何设置颜色和字体大小吗？
- [ ] 知道 `class` 和 `id` 的区别吗？
- [ ] 能用浏览器打开并查看自己的网页吗？

---

## 📚 推荐资源

- MDN Web文档：https://developer.mozilla.org/zh-CN/
- 菜鸟教程HTML：https://www.runoob.com/html/html-tutorial.html
- CSS颜色选择器：https://www.w3schools.com/colors/colors_picker.asp
