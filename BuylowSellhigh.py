from bs4 import BeautifulSoup
import requests
import re
import json
from datetime import datetime, timedelta

while True:
    ticker = input("Type the ticker symbol. Close? 1=Yes 0=No: ").strip().upper()
    
    if ticker == "1":
        exit()
    if ticker == "0":
        break

    # Macroaxis real/intrinsic value
    url = f"https://www.macroaxis.com/valuation/{ticker}"
    result = requests.get(url)
    doc = BeautifulSoup(result.content, "html.parser")

    realvalue = ""
    for div in doc.find_all("div"):
        if str(div).startswith('<div class="symbolDescriptionNoMargin"'):
            match = re.search(r"\$\d+(?:\.\d{2})?", str(div))
            if match:
                realvalue = match.group()[1:]  # strip "$"
            break

    print(f"{ticker} Real value: ${realvalue}")

    # Yahoo Finance current price
    url2 = f"https://finance.yahoo.com/quote/{ticker}/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    result2 = requests.get(url2, headers=headers)
    doc2 = BeautifulSoup(result2.text, "html.parser")

    cprice = ""
    tags = doc2.find_all("fin-streamer")
    if tags:
        cprice = tags[0].get_text()

    print(f"Current {ticker} price: ${cprice}")

    if realvalue and cprice:
        signal = "Buy!" if float(cprice) < float(realvalue) else "Sell!"
        print(signal)
        
        # ALWAYS prompt for entry price + calculate stop losses
        try:
            entry_price = float(input(f"Enter your entry price for {ticker}: $"))
            
            # Fetch historical data for ATR (14 periods, daily)
            end_date = datetime.now()
            start_date = end_date - timedelta(days=30)
            params = {
                "period1": int(start_date.timestamp()),
                "period2": int(end_date.timestamp()),
                "interval": "1d",
                "events": "history"
            }
            hist_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}"
            hist_result = requests.get(hist_url, params=params, headers=headers)
            hist_data = hist_result.json()
            
            quotes = hist_data["chart"]["result"][0]["indicators"]["quote"][0]
            highs = quotes["high"][:15]
            lows = quotes["low"][:15]
            closes = quotes["close"][:15]
            
            # Calculate True Ranges
            trs = []
            for i in range(1, 15):
                hl = highs[i] - lows[i]
                hc = abs(highs[i] - closes[i-1])
                lc = abs(lows[i] - closes[i-1])
                tr = max(hl, hc, lc)
                trs.append(tr)
            
            # ATR = average of TRs (14-period)
            atr = sum(trs) / len(trs)
            
            print("\nStop Loss Levels (Entry - ATR * Multiplier):")
            print("| Style        | Multiplier | Stop Loss   |")
            print("|--------------|------------|-------------|")
            print(f"| Day Trading  | 1          | ${entry_price - atr*1:.2f} |")
            print(f"| Swing        | 2          | ${entry_price - atr*2:.2f} |")
            print(f"| Trend Follow | 3          | ${entry_price - atr*3:.2f} |")
            print(f"\n(ATR 14-day: ${atr:.2f})")
            
        except (ValueError, KeyError, IndexError, json.JSONDecodeError):
            print("Could not calculate ATR/stop loss (data unavailable).")
    else:
        print("Could not retrieve prices for comparison.")

    print("\n")
