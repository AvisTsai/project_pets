#import urllib.request as req
import requests
url = "https://www.momoshop.com.tw/category/LgrpCategory.jsp?l_code=4700200000&mdiv=1099700000-bt_0_997_18-bt_0_997_18_P104_2_e1&ctype=B"
headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}
res =requests.get(url,headers=headers )

import bs4
soup = bs4.BeautifulSoup(res.text, 'html.parser')

for good in soup.select('input[name=".sys_url:e2_img:e3_prdName:e4_gds:p1"]'): 
    title = good.select_one('.prdName').get('title')
    price = good.select_one('.prdPrice').text
    print(title,price)
