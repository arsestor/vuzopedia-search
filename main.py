import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

MAIN_URL = 'https://vuzopedia.ru'

page = 0
while True:
    page += 1
    URL_TEMPLATE = f'https://vuzopedia.ru/region/city/59/poege/egemat;egerus;egeinform;?page={page}'

    r = requests.get(URL_TEMPLATE)
    soup = bs(r.text, 'html.parser')

    if 'По данной комбинации ЕГЭ вариантов не найдено.' in soup.find('p').text:
        break

    unis = soup.find_all('div', class_="vuzesfullnorm")
    for uni in unis:
        name_info = uni.img['alt'][8:]
        link_info = uni.a['href']
        budget_info = [i for i in uni.find_all('div', class_='col-md-4 info')][1].find_all('a', class_='tooltipq')

        if budget_info != []:
            budget_info = {'min': budget_info[0].text[budget_info[0].text.find('от')+3:budget_info[0].text.find('минимальный')],
                           'places': budget_info[-1].text[:budget_info[-1].text.find('мест')-1]}
            if budget_info['min'] == '-':
                continue

            print(f"Название: {name_info}")
            print(f"Ссылка: {link_info}")
            print(f"Бюджет (общий): {budget_info}")

            r = requests.get(MAIN_URL + link_info)
            soup = bs(r.text, 'html.parser')

            print('Специальности:')
            for i in soup.find_all('a', class_='spectittle'):
                print(f'   - {i.text}')
            print('\n')

        else:
            pass
