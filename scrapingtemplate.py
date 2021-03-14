#hurriyet.com.tr den dolar çekilecek


import requests
from bs4 import BeautifulSoup

hisse_url = "https://hurriyet.com.tr"

html_kod = requests.get(hisse_url)


soup = BeautifulSoup(html_kod.content, 'lxml')