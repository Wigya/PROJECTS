from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import re

class Olx():

    def __init__(self, url):
        self.url = url

    def getTitle(self):
        html = urlopen(self.url)
        bs = BeautifulSoup(html, 'html.parser')
        content = bs.find('div', class_='content')
        title = content.find_all('a', {'class':['marginright5 link linkWithHash detailsLinkPromoted linkWithHashPromoted','marginright5 link linkWithHash detailsLink','marginright5 link linkWithHash detailsLinkPromoted']})
        return title


    def getPrice(self):
        """Get prices from olx"""
        html = urlopen(self.url)
        bs = BeautifulSoup(html, 'html.parser')
        price = bs.findAll('p', class_='price')
        return price

    def nextPage(self):
        """Go to the next page"""
        html = urlopen(self.url)
        bs = BeautifulSoup(html, 'html.parser')
        pageButton = bs.findAll('a', {'class': 'block br3 brc8 large tdnone lheight24'})
        try:
            return pageButton
        except AttributeError:
            None
        else:
            return pageButton


def saveOutput():
    """Function which saves output into file"""
    filenamePrices = 'prices.txt'
    with open(filenamePrices, 'w', encoding='utf-8') as obj:
        json.dump(Prices, obj, indent='\t', ensure_ascii=False)
    
    filenameTitles = 'titles.txt'
    with open(filenameTitles, 'w', encoding='utf-8') as obj:
        json.dump(Titles, obj, indent='\t', ensure_ascii=False)

# Instances of class
olxprices = Olx('https://www.olx.pl/nieruchomosci/mieszkania/wynajem/olsztyn/').getPrice()
nextpage = Olx('https://www.olx.pl/nieruchomosci/mieszkania/wynajem/olsztyn/').nextPage()
title = Olx('https://www.olx.pl/nieruchomosci/mieszkania/wynajem/olsztyn/').getTitle()


# This part of code saves all prices
Prices = []
for page in nextpage:
    for price in olxprices:
        Prices.append(price.get_text().strip().replace('ł', '').replace('z', '').replace(' ',''))
    newUrl = page['href']
    olxprices = Olx(newUrl).getPrice()

# This part of code saves all titles
Titles = []
for page in nextpage:
    for titles in title:
        Titles.append(titles.get_text().replace('\n', '').replace('n\'', '').replace(',',''))
    newUrl = page['href']   
    olxprices = Olx(newUrl).getPrice()
print(Prices)
print(Titles)

saveOutput()