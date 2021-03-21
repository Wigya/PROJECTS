import random
from bs4 import BeautifulSoup
import requests
from PIL import Image


CHARS = 'abcdefghijklmnouprstvxyz1234567890'


def getImageSrc():
    petla = True
    while petla:
        header = {'User-Agent': 'Mozilla/5.0'}
        x = ''
        for i in range(1, 6):
            x += random.choice(CHARS)
        url = 'https://prnt.sc/{}'.format(x)
        req = requests.get(url, headers=header).text
        bs = BeautifulSoup(req, 'html.parser')
        imageSrc = bs.find('img')
        if imageSrc['src'] == '//st.prntscr.com/2021/02/09/0221/img/footer-logo.png' or imageSrc['src'] == '//st.prntscr.com/2021/02/09/0221/img/0_173a7b_211be8ff.png':
            petla = True
        else:
            petla = False
    return bs.find('img')['src']


def saveImage():
    image_url = getImageSrc()
    img = Image.open(requests.get(image_url, stream=True).raw)
    toRGB = img.convert('RGB')
    x = ''
    for i in range(1, 6):
        x += random.choice(CHARS)
    return toRGB.save('image-{}.jpg'.format(x))


a = 0
while a < 30:
    getImageSrc()
    saveImage()
    a += 1
