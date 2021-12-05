from typing import ItemsView

import mysql.connector
import requests
import pymysql
from bs4 import BeautifulSoup

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000',
                     db='project_pets', charset='utf8')
cursor = db.cursor()
response = requests.get('https://www.fuzeshop.com.tw/categories/%E7%8B%97%E7%8B%97%E7%94%A8%E5%93%81')
soup = BeautifulSoup(response.text, "html.parser")

container = soup.select(".boxify-image")


class shop_item:
    def __int__(self, title, price, url, produce_url):
        self.title = title
        self.price = price
        self.url = url
        self.produce_url = produce_url


list_url = []
for item in container:
    if item:
        value = item['style'].split("(")[1].split(")")[0]
        list_url.append(value)

title = soup.find_all("div", class_="title text-primary-color")
price = soup.find_all("div", class_="price-sale price sl-price primary-color-price")
produce_url = soup.find_all("a", class_="quick-cart-item js-quick-cart-item")


list_title = []
list_price = []
list_produce_url = []

for pro in produce_url:
    list_produce_url.append(pro['href'])

for tit in title:
    list_title.append(tit.getText())

for pri in price:
    list_price.append(pri.getText().strip())

for result in zip(list_title, list_price, list_url, list_produce_url):
    sql = f"INSERT INTO project_pets.pets_shop(shop_title, shop_price, shop_url, produce_url) VALUES (" + "'" + result[0] + "'" + ',' + "'" + result[1] + "'" + ',' + "'" + result[2] + "'" + "," + "'" + result[3] + "'" + ")"
    cursor.execute(sql)
db.commit()
# print(len(list_title))