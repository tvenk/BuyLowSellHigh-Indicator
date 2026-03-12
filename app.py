from flask import Flask, jsonify, render_template
from bs4 import BeautifulSoup
import requests
import re
import json
from datetime import datetime, timedelta

app = Flask(__name__)

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze/<ticker>')
def analyze_ticker(ticker):
    try:
        ticker = ticker.upper().strip()
        real_value = get_real_value(ticker)
        current_price = get_current_price(ticker)
        signal = "Buy!" if float(current_price) < float(real_value) else "Sell!"

        return jsonify({
            'ticker': ticker,
            'realValue': real_value,
            'currentPrice': current_price,
            'signal': signal
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/stoploss/<ticker>/<entry_price>')
def stop_loss(ticker, entry_price):
    try:
        ticker = ticker.upper().strip()
        entry = float(entry_price)
        atr = get_atr(ticker)

        return jsonify({
            'ticker': ticker,
            'entryPrice': entry,
            'atr': round(atr, 2),
            'stopLoss': {
                'dayTrading':    round(entry - atr * 1, 2),
                'swingTrading':  round(entry - atr * 2, 2),
                'trendFollowing': round(entry - atr * 3, 2)
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


def get_real_value(ticker):
    url = f"https://www.macroaxis.com/valuation/{ticker}"
    result = requests.get(url, headers=HEADERS)
    doc = BeautifulSoup(result.content, "html.parser")

    for div in doc.find_all("div"):
        if str(div).startswith('<div class="symbolDescriptionNoMargin"'):
            # Fixed regex: single backslash escapes inside raw string
            match = re.search(r"\$\d+(?:\.\d{2})?", str(div))
            if match:
                return match.group()[1:]  # strip "$"
    raise Exception(f"Real value not found for {ticker}")


def get_current_price(ticker):
    url = f"https://finance.yahoo.com/quote/{ticker}/"
    result = requests.get(url, headers=HEADERS)
    doc = BeautifulSoup(result.text, "html.parser")
    tags = doc.find_all("fin-streamer")
    if tags:
        return tags[0].get_text()
    raise Exception(f"Current price not found for {ticker}")


def get_atr(ticker):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    params = {
        "period1": int(start_date.timestamp()),
        "period2": int(end_date.timestamp()),
        "interval": "1d",
        "events": "history"
    }
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
    result = requests.get(url, params=params, headers=HEADERS)
    data = result.json()

    quotes = data["chart"]["result"][0]["indicators"]["quote"][0]
    highs  = quotes["high"][:15]
    lows   = quotes["low"][:15]
    closes = quotes["close"][:15]

    # Calculate 14-period True Range
    trs = []
    for i in range(1, 15):
        hl = highs[i] - lows[i]
        hc = abs(highs[i] - closes[i - 1])
        lc = abs(lows[i] - closes[i - 1])
        trs.append(max(hl, hc, lc))

    return sum(trs) / len(trs)


if __name__ == '__main__':
    app.run(debug=True)

