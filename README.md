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

This version provides a backend with Flask and Python (`app.py`), while
the frontend is displayed via HTML/JavaScript (`index.html`). It supports
ticker analysis with buy/sell signals and ATR-based stop loss calculations
directly in the browser.

### Installation

#### Windows
```
pip install flask beautifulsoup4 requests
```

#### Linux (Debian/Ubuntu/MX Linux)
```
sudo apt install python3-flask python3-bs4 python3-requests
```
Or via virtual environment (recommended):
```
python3 -m venv .venv
source .venv/bin/activate
pip install flask beautifulsoup4 requests
```

---

### Setup and Running

1. Place `index.html` into a folder named `templates`
2. Place `app.py` in the same directory **next to** the `templates` folder:
```
your-folder/
├── app.py
└── templates/
    └── index.html
```
3. Open a terminal or command prompt and navigate to your project folder:
```
cd your-folder
```
4. Run the Flask server:

**Windows:**
```
python app.py
```
**Linux:**
```
python3 app.py
```
5. Open a browser and go to:
```
http://127.0.0.1:5000
```
or
```
http://localhost:5000
```

---

### Usage
1. Enter a ticker symbol (e.g. `AAPL`, `TSLA`, `SPY`) and click **Analyze**
2. View the intrinsic value, current market price, and **Buy/Sell** signal
3. Enter your intended entry price in the stop loss section that appears
4. View ATR-based stop loss levels for all three trading styles:

| Style        | Multiplier | Description            |
|--------------|------------|------------------------|
| Day Trading  | 1x ATR     | Tight stop, short-term |
| Swing        | 2x ATR     | Medium-term holds      |
| Trend Follow | 3x ATR     | Wide stop, long-term   |

5. Open a web browser and go to http://127.0.0.1:5000 or http://localhost:5000 to use the application.
