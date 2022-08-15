import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL_TEMPLATE = 'https://vuzopedia.ru/region/city/59/poege/egemat;egerus;egeinform;?page=1'
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, 'html.parser')
unis = soup.find_all('div', class_="vuzesfullnorm")
for uni in unis:
    try:
        scores, places = [i.text for i in uni.find_all('div', class_='col-md-4 info')[1].find_all('a', class_='tooltipq')[::2]]
        print(f"Название: {uni.img['alt'][8:]}")
        print(f"Ссылка: {uni.a['href']}")
        print(f"Бюджет: {[scores[3:6], places[:-38]]}\n")
    except:
        pass
