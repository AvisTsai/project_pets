from typing import ItemsView

import mysql.connector
import requests
import pymysql
from bs4 import BeautifulSoup

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='0000',
                     db='project_pets', charset='utf8')
cursor = db.cursor()
response = requests.get(
    "https://www.fuzeshop.com.tw/categories/%E5%B0%BF%E5%B8%83%E5%A2%8A%E7%84%A1%E6%B3%95%E8%88%87%E4%BB%96%E5%8D%80%E5%85%B1%E5%90%8C%E7%B5%90%E5%B8%B3"
)
soup = BeautifulSoup(response.text, "html.parser")

container = soup.select(".boxify-image")


class shop_item:
    def __int__(self, title, price, url):
        self.title = title
        self.price = price
        self.url = url


list_url = []
for item in container:
    if item:
        value = item['style'].split("(")[1].split(")")[0]
        list_url.append(value)

title = soup.find_all("div", class_="title text-primary-color")
price = soup.find_all(
    "div", class_="price-sale price sl-price primary-color-price")

list_title = []
list_price = []

for tit in title:
    list_title.append(tit.getText())

for pri in price:
    list_price.append(pri.getText().strip())

for result in zip(list_title, list_price, list_url):
    sql = f"INSERT INTO project_pets.pets_shop(shop_title, shop_price, shop_url) VALUES (" + "'" + result[0] + "'" + ',' + "'" + result[1] + "'" + ',' + "'" + result[2] + "'" + ")"
    cursor.execute(sql)
db.commit()
# print(len(list_title))