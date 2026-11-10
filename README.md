# 大一学习小项目合集

我大一期间完成的机器学习与深度学习、Python 编程、Web 开发入门项目合集。

这是我建立的第一个 GitHub 仓库，目的不是展示作品，而是**记录一个初学者从零开始的路线**——从高考后第一次写代码，到接触机器学习算法原理。内容不深，但每一步都是真实的。

## 📍 学习路线

```
2025.07  高考结束，开始学编程
   └─ Python 基础语法 → 爬虫 → 数据分析 → Web 前后端入门 demo
2026.01  开始学机器学习与深度学习
   └─ 调库实现 → 逐步理解原理（前向/反向传播、梯度下降、CNN 卷积与池化）
```

## 📂 目录结构

```
First-Year-ML-Projects
├── Python-projects/            # Python 编程：基础、爬虫、数据分析
│   ├── basic-practice/         #   语法基础实验
│   ├── web-crawler/            #   爬虫（壁纸/百度图片/招聘数据/天气查询）
│   └── data-analysis/          #   数据分析（pandas/numpy/matplotlib/pyecharts）
├── web-development/            # Web 开发入门
│   ├── backend-practice/       #   Flask + MySQL 后端 demo
│   └── front-learning/         #   HTML/CSS 前端页面与组件
└── 机器学习与深度学习/           # 机器学习与深度学习
    ├── machine-learning/       #   经典机器学习算法
    └── deep-learning/          #   神经网络与 CNN
```

## 1️⃣ Python 编程（[Python-projects/](./Python-projects/)）

**技术栈**：requests、BeautifulSoup、jieba、pandas、numpy、Matplotlib、Pyecharts、jupyter

| 类别 | 内容 |
|---|---|
| 爬虫 | 爬取新闻、壁纸、招聘数据并导出 Excel；百度引擎关键字图片爬取系统 |
| 自动化 | Selenium 浏览器自动化、Excel 表格生成 |
| 数据分析 | 电商客户分析、天气预报查询、奶茶店经营分析、酒店数据与情感可视化、抖音热门商品分析 |

> **2025.07 ~ 2025.12 的记录**：这是我高考结束后开始学习编程的起点。作为初学者，简单的爬虫和数据分析带来的正向反馈很多。资料都是网上找的，从文件存放处理上并不算好——也算是新手时期真实的样子。

## 2️⃣ Web 开发入门（[web-development/](./web-development/)）

**技术栈**：MySQL、Flask、pymysql、HTML、CSS

| 类别 | 内容 |
|---|---|
| 后端 | Flask 搭建接口服务，pymysql 封装 MySQL 增删改查 |
| 前端实战 | 企业网站登录页与样式开发 |
| 前端基础 | 作业提交检查功能、密码框 UI 组件、创客企业网站页面 |

> **2025.07 ~ 2025.12 的记录**：前后端入门 demo，用 pymysql 大致写了增删改查并简单封装，配 HTML/CSS 静态页面和 Flask 简单接口。对前后端有了基本概念，但还没做前后端交互——这是后续要补的方向。

## 3️⃣ 机器学习与深度学习（[机器学习与深度学习/](./机器学习与深度学习/)）

**技术栈**：Python、Pandas、numpy、Scikit-learn、Matplotlib、seaborn、TensorFlow、jupyter

| 类别 | 内容 |
|---|---|
| 回归 | 线性回归、多元线性回归预测销售额、随机森林预测共享单车 |
| 分类 | 逻辑回归（泰坦尼克/乳腺癌）、决策树（贷款/糖尿病/鸢尾花）、随机森林（天气/心血管疾病） |
| 探索性分析 | 鸢尾花数据集探索 |
| 神经网络 | 手写数字识别、鸢尾花分类 |
| CNN | CIFAR-10 分类、时尚单品识别、猫狗分类（含 MobileNetV2 迁移学习 + tkinter 可视化窗口） |

> **2026.01 开始的记录**：刚开始基本是调 TensorFlow 现成的库去用，后面逐步了解其中的原理。印象最深刻的是神经网络的前向传播、反向传播、梯度下降，以及 CNN 的卷积、池化机制——从"会调库"到"知道库在做什么"。

## 🧭 后续方向

- [ ] 前后端交互（axios / fetch + Flask 接口联调）
- [ ] 深度学习项目工程化（数据处理管道、模型保存与评估）
- [ ] 当前专业方向：人工智能（详见我的[个人博客](https://blog.fireflyai.site)）
