import requests
from bs4 import BeautifulSoup

# url = 'https://akipress.org/'
# response = requests.get(url=url)
# # print(response.text)
# soup = BeautifulSoup(response.text, 'lxml')
# print(soup)
# all_news = soup.find_all('a', class_='newslink')
# # print(all_news)
# n = 0
# for news in all_news:
#     n += 1
#     with open('news.txt', 'a+', encoding='utf-8') as news_file:
#         news_file.write(f"{n}) {news.text}\n")
#     print(f"{n}", news.text)

def parsing_sulpak():
    n = 0
    for i in range(1, 21):
        url = f'https://www.sulpak.kg/f/smartfoniy?page={i}'
        response = requests.get(url=url)
        soup = BeautifulSoup(response.text, 'lxml')
        # print(response)
        smartfoniy = soup.find_all('div', class_='product__item-name')
        prices = soup.find_all('div', class_='product__item-price')
        # print(smartfoniy)
        for name, price in zip(smartfoniy, prices):
            n += 1
            current_price = "".join(price.text.split())
            print(n, name.text, current_price)
parsing_sulpak()