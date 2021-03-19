# Döviz.com'dan en çok kazandıran 6 hisse senedini çektim. hisse senedi listesi excel dosyasına çekilecek.


import requests
from bs4 import BeautifulSoup

hisse_url = "https://borsa.doviz.com/"

html_kod = requests.get(hisse_url)


soup = BeautifulSoup(html_kod.content, 'lxml')

baslik=soup.find_all('h3', class_='left')

bilgi_bar = soup.find_all('div', class_='table')[0].find_all('th')

print(baslik[0].get_text())

for i in range(1,7):
    bilgi_bar2 = soup.find_all('div', class_='table')[0].find_all('tr')[i].find_all('td')

    for j in range(0,4):
        print(bilgi_bar[j].get_text()+":"+bilgi_bar2[j].get_text().strip())
    print("----------------------------------------------")


