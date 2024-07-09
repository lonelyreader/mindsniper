from flask import Flask, request, send_file, render_template, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

base_url = "https://www.aisixiang.com"

# 定义一个函数来抓取文章内容
def get_article_content(url):
    article_response = requests.get(url)
    article_response.encoding = 'utf-8'
    article_soup = BeautifulSoup(article_response.text, 'html.parser')
    title = article_soup.find('h3').text.strip()
    content_div = article_soup.find('div', id='content')
    paragraphs = content_div.find_all('p')
    content = "\n".join([p.text.strip() for p in paragraphs])
    return title, content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    author_pinyin = data['author']
    author_url = f"{base_url}/thinktank/{author_pinyin}.html"
    
    # 发送请求并获取网页内容
    response = requests.get(author_url)
    response.encoding = 'utf-8'
    if response.status_code != 200:
        return jsonify({"error": "Author not found"}), 404

    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有文章的链接
    article_sections = soup.find_all('div', class_='thinktank-author-article-list')
    article_links = []

    for section in article_sections:
        links = section.find_all('a')
        for link in links:
            article_links.append(base_url + link['href'])

    # 创建Markdown文件
    filename = f"{author_pinyin}.md"
    with open(filename, 'w', encoding='utf-8') as file:
        for link in article_links:
            try:
                title, content = get_article_content(link)
                file.write(f"# {title}\n")
                file.write(f"[Source]({link})\n\n")
                file.write(f"{content}\n\n")
                file.write("---\n\n")
            except Exception as e:
                print(f"Failed to process {link}: {e}")

    return send_file(filename, as_attachment=True, download_name=filename, mimetype='text/markdown')

if __name__ == '__main__':
    app.run(debug=True)
