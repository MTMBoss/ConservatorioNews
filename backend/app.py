from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

@app.route('/updates', methods=['GET'])
def get_updates():
    url = 'https://conts.it/it/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news = []
    for item in soup.select('body > main > div:nth-child(2) > div.row.g-0'):
        title = item.get_text()
        news.append({'title': title})

    return jsonify(news)

if __name__ == '__main__':
    app.run(debug=True)
