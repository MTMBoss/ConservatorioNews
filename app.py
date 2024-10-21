from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/updates', methods=['GET'])
def get_updates():
    url = 'URL_DEL_SITO_DEL_CONSERVATORIO'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news = []
    for item in soup.select('CSS_SELECTOR_PER_LA_NEWS'):
        title = item.get_text()
        news.append({'title': title})

    return jsonify(news)

if __name__ == '__main__':
    app.run(debug=True)
