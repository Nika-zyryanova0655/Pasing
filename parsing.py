import requests
from bs4 import BeautifulSoup as bs
website = requests.get('https://russiandrone.ru/publications/?show_by=100').text
website_bs = bs('website', 'lxml')
inf = website_bs.find("section", class_="products").find("div", class_="desc")
print(inf)

#как-то использовать product.name
#почитать документацию