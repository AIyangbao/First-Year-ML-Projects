import requests
from bs4 import BeautifulSoup

# 获取壁纸网站首页数据
def demo():
    url = "https://haowallpaper.com/homeView?isSel=false&page=1"
    head = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
    resp1 = requests.get(url, headers=head)
    # 获取壁纸的url
    soup = BeautifulSoup(resp1.text, "html.parser")
    div_tag = soup.find_all("div", class_="resource-container img-or-video")
    for resourcecontainer in div_tag:

        if resourcecontainer.find("img"):
            img_url = resourcecontainer.find("img")["src"]
            name = resourcecontainer.find("img")["title"]
            resp2 = requests.get(img_url, headers=head)
            with open(f"D:\编程教程\Python编程项目\IMG/{name}.png", "wb") as f:
                f.write(resp2.content)
        else:
            img_url = resourcecontainer.find("video")["src"]
            name = resourcecontainer.find("video")["title"]
            resp2 = requests.get(img_url, headers=head)
            with open(f"D:\编程教程\Python编程项目\IMG/{name}.mp4", "wb") as f:
                f.write(resp2.content)
            # 将向壁纸url发送请求，下载保存

demo()
