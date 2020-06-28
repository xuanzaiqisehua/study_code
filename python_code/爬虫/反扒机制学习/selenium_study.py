from selenium import webdriver
browser=webdriver.Chrome()# 声明浏览器
url='https://www.baidu.com/'
browser.get(url) # 打开预设网址
print(browser.page_source)# 打印网页源代码
browser.close()# 关闭浏览器
