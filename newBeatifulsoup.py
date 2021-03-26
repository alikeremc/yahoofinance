import requests
from bs4 import BeautifulSoup


response=requests.get("https://www.doviz.com/kripto-paralar/bitcoin")

soup=BeautifulSoup(response.content,"html.parser")

#print(soup.prettify())
coin=soup.find_all("div", class_="currency-card relative bg-blue-gray-9 rounded-md p-16")[0].find_all('div')

print(coin[1].get_text())
a=coin[2].get_text().strip().replace(" ","").split()

i=0
while i<10:
    print(a[i],end='     ')
    i += 2
    if i==2:
        i+=2

print()
i=1
while i<10:
    print(a[i],end='     ')
    i += 2
    if i==3:
        i+=2