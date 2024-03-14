import requests
from bs4 import BeautifulSoup as bs
website = requests.get('https://russiandrone.ru/publications/?show_by=100')
website_bs = bs('website', 'lxml')
inf = website_bs.find('selection', class_='priducts')
print(inf)