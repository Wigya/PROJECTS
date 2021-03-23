from bs4 import BeautifulSoup
import requests
import smtplib
import time

url = 'https://www.amazon.com/Acer-Display-Graphics-Keyboard-A515-43-R19L/dp/B07RF1XD36/ref=sr_1_3?dchild=1&keywords=laptop&qid=1616507455&sr=8-3'
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0', 'Accept-Language': 'en-US,en;q=0.5'}
html = requests.get(url, headers=header).text
soup = BeautifulSoup(html, 'html.parser')


def getTitle():
    title = soup.find('span', id='productTitle')
    return title.get_text().strip()


def getPrice():
    try:
        price = soup.find('span', id='priceblock_ourprice').get_text()
        price = float(price[1:])
    except AttributeError:
        price = 'Currently unavailable'
    return price


def sendEmail():
    with smtplib.SMTP_SSL('smtp.wp.pl', '465') as smtp:
        # Here type YOUR login and password for in this case wp.pl mailbox
        smtp.login('', '')

        msg = f'{getTitle()} price is {getPrice()}'
        # Here type YOUR email and target email
        return smtp.sendemail('', '', msg)


while True:
    time.sleep(3600)
    if getPrice() == 'Currently unavailable':
        print('Currently unavailable')
    elif getPrice() > 100:
        sendEmail()
