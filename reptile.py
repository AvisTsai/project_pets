import requests
from bs4 import BeautifulSoup
import urllib.request as req
import os


url = "https://www.fuzeshop.com.tw/products"
request = req.Request(url, headers={
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36'
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    soup = BeautifulSoup(data, "html.parser")
    all_img = soup.select(".boxify-image js-boxify-image center-contain sl-lazy-image")
    return all_img
5fy-image js-boxify-image center-contain sl-lazy-image
