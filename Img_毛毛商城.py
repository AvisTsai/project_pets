import requests
url = "https://shopping.etipets.com/product-list/110"
headers={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}
res =requests.get(url,headers=headers )

import bs4
soup = bs4.BeautifulSoup(res.text, 'html.parser')

path = ("output4.txt")
f = open(path, 'w')

pngs = soup.find_all("div",{"class":"pic"})
pngs2 = soup.find_all("a")
print(len(pngs))
print(pngs2)

for each in pngs2:
    png_tag = each.find("img", {"class": " lazyloaded"})
    if not png_tag:
        png_url = ""
    else:
        png_url = png_tag.get("src")
        print(png_url)