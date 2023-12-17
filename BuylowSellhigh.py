from bs4 import BeautifulSoup
import requests


ticker =""

while ticker != 0 or ticker != 1:
    ticker = input("Type the ticker symbol you want to check. Do you want to close? 1 = Yes 0 = No: ").upper()
    if ticker == 1:
        exit()


    url = "https://www.macroaxis.com/valuation/{0}".format(ticker) 

    result = requests.get(url)
    doc = BeautifulSoup(result.content, "html.parser")

    divs = doc.find_all("div")
    price = ""
    for div in divs:
        if (str(div).startswith('<div class="ui large green button"')):
            div_text = str(div)
            price = div.text
            break
            

    realvalue = price
    realvalue = realvalue.replace(',','')
    print("{0} Real value: $".format(ticker),realvalue) 


    url2 ="https://finance.yahoo.com/quote/{0}/".format(ticker) 

    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'} 
    result = requests.get(url2, headers=headers)

    doc2 = BeautifulSoup(result.text, "html.parser")

    cprice = ""

    tags = doc2.find_all("fin-streamer")

    for tag in tags:
        if tag["data-symbol"] == ticker: 

             cprice = tag["value"]
             break

    print("Current {0} price: $".format(ticker),cprice)


    if float(cprice) < float(realvalue):
        print("Buy!")
    else:
        print("Sell!")

    print("\n")




