import requests
from bs4 import BeautifulSoup


def soup_html(url):
    r = requests.get(url)
    r.encoding = 'urf-8'
    return BeautifulSoup(r.text, 'html.parser')

url = 'http://parsinger.ru/html/index1_page_1.html'
url_href = 'http://parsinger.ru/html/'

soup_url_index = soup_html(url)
col_indexs = len(soup_url_index.find('div', class_='nav_menu').find_all('a'))  # кол-во индексов (категорий)

index = 1
page = 1
col_price = 0
total_sum = 0
for index in range(1, col_indexs+1):
    """ Проход по категориям """
    url2 = f'http://parsinger.ru/html/index{index}_page_{page}.html'
    page_soup = soup_html(url)
    col_pages = len(page_soup.find('div', {'class': 'pagen'}).find_all('a'))  # кол. страниц (пагенаций)
    for page in range(1, col_pages+1):
        """Проход по страницам"""
        cart_soup = soup_html(url2)
        href_strs = cart_soup.find_all('a', {'class': 'name_item', 'href': True, 'name': True})
        href_list = [href.get('href') for href in href_strs]
        for href in href_list:
            """Проход по карточкам"""
            url_cards = url_href + href
            soup_card = soup_html(url_cards)
            card_price = int(soup_card.find('span', {'id': 'price'}).text.split(' ')[0])
            card_col = int(soup_card.find('span', {'id': 'in_stock'}).text.split(' ')[-1])
            col_price = card_price * card_col
            total_sum += col_price
