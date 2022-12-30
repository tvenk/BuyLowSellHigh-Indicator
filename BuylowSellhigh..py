from bs4 import BeautifulSoup
import requests

url = "https://www.macroaxis.com/valuation/FREQ"

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
print("FREQ Real value: $",realvalue)



url2 ="https://finance.yahoo.com/quote/FREQ/"

result = requests.get(url2)

doc2 = BeautifulSoup(result.text, "html.parser")

cprice = ""

tags = doc2.find_all("fin-streamer")

for tag in tags:
    if tag["data-symbol"] == "FREQ":
         cprice = tag["value"]
         break

print("Current FREQ price: $",cprice)

if float(cprice) < float(realvalue):
    print("Buy!")
else:
    print("Sell!")

