from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
class Olx():

    def __init__(self, url):
        self.url = url

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

olxprices = Olx('https://www.olx.pl/nieruchomosci/mieszkania/wynajem/olsztyn/').getPrice()
nextpage = Olx('https://www.olx.pl/nieruchomosci/mieszkania/wynajem/olsztyn/').nextPage()

counter = 0

while len(nextpage) > 0:
    for price in olxprices:
        print(price.get_text().strip())
    newUrl = nextpage[counter]['href']
    olxprices = Olx(newUrl).getPrice()
    counter += 1
