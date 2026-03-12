# BuyLowSellHigh

## 1. Standalone Python Version

This Python script provides a buy or sell rating on any ticker by comparing
the intrinsic (real) value from Macroaxis against the current market price
from Yahoo Finance. After the signal, enter your intended entry price to
receive ATR-based stop loss levels tailored for day trading, swing trading,
and trend following.

### Installation

#### Windows
```
pip install beautifulsoup4 requests
```

#### Linux (Debian/Ubuntu/MX Linux)
```
sudo apt install python3-bs4 python3-requests
```
Or via virtual environment (recommended):
```
python3 -m venv .venv
source .venv/bin/activate
pip install beautifulsoup4 requests
```

---

### Running the Script

#### Windows
```
python BuylowSellhigh.py
```

#### Linux
```
python3 BuylowSellhigh.py
```

---

### Usage
1. Type a ticker symbol (e.g. `AAPL`, `TSLA`, `SPY`)
2. View the intrinsic value vs current price and **Buy/Sell** signal
3. Enter your intended entry price
4. Receive stop loss levels for three trading styles:

| Style        | Multiplier | Description               |
|--------------|------------|---------------------------|
| Day Trading  | 1x ATR     | Tight stop, short-term    |
| Swing        | 2x ATR     | Medium-term holds         |
| Trend Follow | 3x ATR     | Wide stop, long-term      |

5. Type `1` to exit, `0` to quit the loop

---

## 2. Upgraded WebApp Version


This version provides a backend with Flask and Python (`app.py`), while the frontend is displayed via JavaScript (`index.html`).

### Setup and Running

1. Place the `index.html` into a folder named "templates".
2. Place `app.py` into the same directory as the "templates" folder (next to it).
3. Open terminal or command prompt and navigate to your current directory containing the "templates" folder and `app.py`.
Example (if the "templates" folder and app.py is in your Desktop) run this command without quotes "cd Desktop".
4. Run the Flask server via command prompt running the code below:

python app.py

5. Open a web browser and go to http://127.0.0.1:5000 or http://localhost:5000 to use the application.
