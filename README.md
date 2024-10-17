# BuyLowSellHigh

## 1. Standalone Python Version

This Python script provides a buy or sell rating on the ticker you enter by comparing the analyst real value price with the current market price. It helps investors to dollar cost average.

### Installation

To run the code, make sure to install these dependencies:

1. Open a terminal or command prompt
2. Install BeautifulSoup using pip:

pip install beautifulsoup4


3. Install requests:

pip install requests


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
