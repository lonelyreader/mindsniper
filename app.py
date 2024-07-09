from flask import Flask, request, send_file, jsonify, render_template
import os
import requests
from bs4 import BeautifulSoup
import time

app = Flask(__name__)

def get_articles(author_pinyin):
    base_url = "https://www.aisixiang.com"
    author_url = f"{base_url}/thinktank/{author_pinyin}.html"
    response = requests.get(author_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    article_links = []
    for div in soup.find_all('div', class_='thinktank-author-article-list'):
        for a in div.find_all('a', href=True):
            article_links.append(base_url + a['href'])

    articles = []
    for link in article_links:
        article_response = requests.get(link)
        article_soup = BeautifulSoup(article_response.content, 'html.parser')
        title = article_soup.find('h3').text.strip()
        content = article_soup.find('div', id='content').text.strip()
        articles.append({'title': title, 'content': content})
    
    return articles

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    author_pinyin = data.get('author')
    if not author_pinyin:
        return jsonify({'error': 'Invalid request'}), 400

    articles = get_articles(author_pinyin)
    if not articles:
        return jsonify({'error': 'No articles found'}), 404

    file_path = f"{author_pinyin}.md"
    with open(file_path, 'w', encoding='utf-8') as f:
        for article in articles:
            f.write(f"# {article['title']}\n\n")
            f.write(f"{article['content']}\n\n")
    
    return send_file(file_path, as_attachment=True, download_name=f"{author_pinyin}.md")

if __name__ == '__main__':
    app.run(debug=True)
