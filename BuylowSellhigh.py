from bs4 import BeautifulSoup
import requests

url = "https://www.macroaxis.com/valuation/SPY/SPDR-SP-500"

result = requests.get(url)
doc = BeautifulSoup(result.content, "html.parser")

divs = doc.find_all("div")
price = ""
for div in divs:
    if (str(div).startswith('<div style="margin-bottom:10px"')):
        div_text = str(div)
        index = div_text.index("$")
        index2 = div_text.find("per share")
        price = div_text[index:index2]
        break
price = price.rstrip()
realvalue = price.lstrip("$")
print("SPY Real value: ",realvalue)

url2 ="https://finance.yahoo.com/quote/SPY/"

result = requests.get(url2)

doc = BeautifulSoup(result.text, "html.parser")

currentprice = doc.find_all("fin-streamer")[18]

print("Current SPY price: ",currentprice.string)

if float(currentprice.string) < float(realvalue):
    print("Buy!")
else:
    print("Sell!")

