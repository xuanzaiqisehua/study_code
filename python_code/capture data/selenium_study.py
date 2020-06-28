'''
参考：https://zhuanlan.zhihu.com/p/76904806
selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。'''
from selenium import webdriver
browser=webdriver.Chrome()#声明浏览器
browser.get('http://www.pythontab.com')
print(browser.page_source)
browser.close()

















