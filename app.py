from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import requests
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze/<ticker>')
def analyze_ticker(ticker):
    try:
        real_value = get_real_value(ticker)
        current_price = get_current_price(ticker)
        
        return jsonify({
            'ticker': ticker,
            'realValue': real_value,
            'currentPrice': current_price
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def get_real_value(ticker):
    url = f"https://www.macroaxis.com/valuation/{ticker}"
    result = requests.get(url)
    doc = BeautifulSoup(result.content, "html.parser")

    divs = doc.find_all("div")
    for div in divs:
        if str(div).startswith('<div class="symbolDescriptionNoMargin"'):
            div_text = str(div)
            money_pattern = r"\$\d+(?:\.\d{2})?"
            match = re.search(money_pattern, div_text)
            if match:
                return match.group()[1:]
    raise Exception("Real value not found")

def get_current_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    result = requests.get(url, headers=headers)
    doc = BeautifulSoup(result.text, "html.parser")
    tags = doc.find_all("fin-streamer")
    if len(tags) > 2:
        return tags[2].text
    raise Exception("Current price not found")

if __name__ == '__main__':
    app.run(debug=True)
