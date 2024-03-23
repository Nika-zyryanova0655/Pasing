import requests
from bs4 import BeautifulSoup as bs
website = requests.get('https://russiandrone.ru/publications/?show_by=100')
website_bs = bs(website.text, 'lxml')
#print(website_bs) #чтение html кода верно
#inf = website_bs.select("div.name.a")
#inf = website_bs.find("section",class_="content right")
pars = website_bs.find('div', class_ = 'left-menu-bl').find('div', class_='cats left-menu-block')
print(pars)
for item in pars:
    print(item.text)