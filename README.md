```markdown
# 学者文章提取器

这是一个简单的Flask Web应用，用于从`爱思想`网站上抓取特定学者的所有文章，并将其保存为Markdown文件。

## 功能

- 输入学者姓名拼音，从`爱思想`网站上抓取该学者的所有文章。
- 将抓取到的文章保存为Markdown文件。
- 支持下载生成的Markdown文件。

## 前提条件

在运行此应用之前，请确保你的系统已安装以下软件：

- Python 3.x
- pip

## 安装

1. 克隆此仓库到你的本地计算机：

```bash
git clone https://github.com/yourusername/scholar-article-scraper.git
cd scholar-article-scraper
```

2. 创建并激活虚拟环境（可选但推荐）：

```bash
python -m venv venv
source venv/bin/activate   # 在Windows上使用: venv\Scripts\activate
```

3. 安装依赖项：

```bash
pip install -r requirements.txt
```

## 运行应用

1. 启动Flask应用：

```bash
python app.py
```

2. 在浏览器中打开以下链接：

```
http://127.0.0.1:5000/
```

3. 输入学者姓名拼音并提交，即可抓取该学者的所有文章，并生成Markdown文件供下载。

## 项目结构

```plaintext
scholar-article-scraper/
│
├── app.py                 # Flask应用的主文件
├── requirements.txt       # Python依赖包
├── templates/
│   └── index.html         # 前端HTML模板
└── README.md              # 项目说明文件
```

## 依赖项

- Flask
- requests
- beautifulsoup4

## 如何贡献

如果你想为此项目做出贡献，请遵循以下步骤：

1. Fork此仓库
2. 创建一个新的分支 (`git checkout -b feature-branch`)
3. 提交你的更改 (`git commit -am 'Add new feature'`)
4. 推送到分支 (`git push origin feature-branch`)
5. 创建一个新的Pull Request

## 许可证

此项目使用MIT许可证。详情请参阅LICENSE文件。
```

### requirements.txt

确保在项目根目录下创建一个`requirements.txt`文件，内容如下：

```
Flask
requests
beautifulsoup4
```

### 完整项目结构

```
scholar-article-scraper/
│
├── app.py                 # Flask应用的主文件
├── requirements.txt       # Python依赖包
├── templates/
│   └── index.html         # 前端HTML模板
└── README.md              # 项目说明文件
```

把这些文件和目录放在一起并提交到你的GitHub仓库中。
