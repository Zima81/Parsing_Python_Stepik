import requests
from bs4 import BeautifulSoup
import csv

def cook_soup(url):
    ans = requests.get(url)
    ans.encoding = 'utf-8'
    if ans.status_code != 200:
        print(ans.status_code, '\n\n', ans.text)
    return BeautifulSoup(ans.text, 'html.parser')

url = 'https://parsinger.ru/html/index1_page_1.html'
soup_index = cook_soup(url)
index = 1
page = 1

len_index = len(soup_index.find('div', class_='nav_menu').find_all('a'))

for _ in range(len_index):
    # Проход по индексам
    url_ = f'https://parsinger.ru/html/index{index}_page_{page}.html'
    soup_page = cook_soup(url_)
    len_page = len(soup_page.find('div', class_='pagen').find_all('a'))  # количество страниц с товаром в индексе
    for _ in range(len_page):
        # Проход по страницам
        soup_ = cook_soup(url_)
        for product in soup_.find_all('div', class_='item'):
            # Проход по карточке товара
            row = list()
            row.append(product.find('a', class_='name_item').text.strip())
            for li in product.find('div', class_='description').find_all('li'):
                # Проход по тэгам li
                row.append(li.text.split(':')[1].strip())
            row.append(product.find('p', class_="price").text.strip())
            # Запись в файл
            with open('data_all_cards.csv', 'a+', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f, delimiter=';')
                writer.writerow(row)
        page += 1
    page = 1
    index += 1