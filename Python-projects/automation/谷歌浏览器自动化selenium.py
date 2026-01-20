from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def demo():
 web=webdriver.Chrome()
 web.get("https://hao.360.com/2022.html?src=x")
 time.sleep(6)
 web.maximize_window()
 time.sleep(10)
 _input=web.find_element(by=By.XPATH,value='//*[@id="search-kw"]')
 _input.send_keys('王者荣耀')
 time.sleep(10)
 _input.send_keys(Keys.ENTER)
 time.sleep(10)
if __name__ =="__main__":
 demo()