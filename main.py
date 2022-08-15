import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL_TEMPLATE = 'https://vuzopedia.ru/region/city/59/poege/egemat;egerus;egeinform;?page=1'
r = requests.get(URL_TEMPLATE)
soup = bs(r.text, 'html.parser')
unis = soup.find_all('div', class_="vuzesfullnorm")
for uni in unis:
        name_info = uni.img['alt'][8:]
        print(f"Название: {name_info}")

        link_info = uni.a['href']
        print(f"Ссылка: {link_info}")

        budget_info = [i for i in uni.find_all('div', class_='col-md-4 info')][1].find_all('a', class_='tooltipq')
        if budget_info != []:
            budget_info = [budget_info[0].text[budget_info[0].text.find('от')+3:budget_info[0].text.find('минимальный')],
                           budget_info[-1].text[:budget_info[-1].text.find('мест')-1]]
            print(f"Бюджет: {budget_info}\n")
        else:
            print(f"Бюджет: нет\n")
