import json
import requests
def demo1():
 while True:
  url="http://gfeljm.tianqiapi.com/api?unescape=1&version=v63&appid=77994331&appsecret=wWr4HCI5&city="
  city=input("请输入你想要查找天气情况的城市(输入q退出系统):")
  if city=="q":
   print('天气灾害查询系统已退出')
   break
  else:
    url=url+city
    resp=(requests.get(url))
    list=resp.json()
    for key, value in list.items():
      print(f"{key}:{value}")
if __name__ == '__main__':
 demo1()


