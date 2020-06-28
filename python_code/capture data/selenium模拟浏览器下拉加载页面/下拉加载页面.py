import requests,time
from bs4 import BeautifulSoup
from selenium import webdriver
# 参考https://www.cnblogs.com/sesshoumaru/p/python-selenium-webdriver.html
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
}
'''data=requests.get("https://tieba.baidu.com/index.html",headers=headers)
html=BeautifulSoup(data.text,'lxml')'''
browser=webdriver.Chrome()#使用谷歌浏览器
#模拟打开贴吧首页
browser.get('https://tieba.baidu.com/index.html')
for i in range(1,5):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(3)
# 最后再使用BeautifulSoup，解析图片标签：
html = BeautifulSoup(browser.page_source, "lxml")
imgs = html.select("#new_list li img")
print(imgs)





















