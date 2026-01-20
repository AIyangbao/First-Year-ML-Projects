from sys import exception
from bs4 import BeautifulSoup
import requests
import json
def demo():
 url="https://www.thepaper.cn/newsDetail_forward_30426430"
 headers={'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'}
 data = requests.get(url,headers=headers)
 soup = BeautifulSoup(data.text,'html.parser')
 title=soup.find("title")
 body =soup.find_all("p")
 print(title.text)
 for i in body:
  print(i.text)
if __name__=="__main__":
    demo()
