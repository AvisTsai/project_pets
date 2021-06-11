import urllib.request as req
def getData(url):
    reguest = req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
    })
    with req.urlopen(reguest) as response:
        data = response.read().decode("utf-8")
    #print(data)

    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div",class_="title")
    for title in titles:
        if title.a != None:
            print(title.a.string)
    nextlink = root.find("a",string="‹ 上頁")
    return nextlink["href"]

pageUrl = "https://www.ptt.cc/bbs/Gossiping/index.html"
count = 1 
while count < 3:
    pageUrl = "http://www.ptt.cc" + getData(pageUrl)
    count += 1
    