import requests
from bs4 import BeautifulSoup
import lxml

#User-agent tanımlıyorum.  Scraping yaparken beni browser sansın diye.

agent_header={'User Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36'}

sembol=input("Hisse Senedi Sembolünü Giriniz:")

hisse_url="https://finance.yahoo.com/quote/"+sembol+"?p="+sembol+"&.tsrc=fin-srch"

#hisse_url="https://finance.yahoo.com/quote/NFLX?p=NFLX&.tsrc=fin-srch"



print(hisse_url)

html_kod=requests.get(hisse_url, headers=agent_header)

#print(html_kod)

soup = BeautifulSoup(html_kod.content, 'lxml')

#sayfa Title'ını görelim

print(soup.title.text)

sayfa_title=soup.find("title").get_text()

# print(sayfa_title)

header = soup.find_all('div', id='quote-header-info')[0]

hisse_title = header.find('h1').get_text()

# print(hisse_title)

hisse_fiyat=header.find('div', class_='D(ib) Va(m) Maw(65%) Ov(h)').find('span').get_text()

print(hisse_title+" - "+hisse_fiyat)
print("---------------------------")


table_info = soup.find('div', class_="D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) "
                                     "smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY "
                                     "smartphone_Bdc($seperatorColor)")
for i in range(0,8):

    satirlar = table_info.find_all("tr")[i].find_all("td")
    #print(table_info)

    satir_baslik=satirlar[0].get_text()
    satir_deger=satirlar[1].get_text()

    print(satir_baslik+" : "+satir_deger)

