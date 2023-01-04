from bs4 import BeautifulSoup
import requests

#IMPORTANT: TO RUN CODE ON DIFFERENT TICKERS IT IS BEST ADVISED TO CHANGE ALL THE TICKERS TO THE SAME ONE AS INDICATED BY THE COMMENTS.

url = "https://www.macroaxis.com/valuation/SPY" #Change to any stock ticker symbol at end of link to one you want where it says ticker symbol SPY

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
print("SPY Real value: $",realvalue) #Change to any stock ticker symbol you want at beginning of string where it says ticker symbol SPY



url2 ="https://finance.yahoo.com/quote/SPY/" #Change to any stock ticker symbol at end of link to one you want


result = requests.get(url2)

doc2 = BeautifulSoup(result.text, "html.parser")

cprice = ""

tags = doc2.find_all("fin-streamer")

for tag in tags:
    if tag["data-symbol"] == "SPY": #Change to any stock ticker symbol at end of == to the one you want

         cprice = tag["value"]
         break

print("Current SPY price: $",cprice) #Change to any stock ticker symbol to one you want


if float(cprice) < float(realvalue):
    print("Buy!")
else:
    print("Sell!")

