#coding=utf-8
#@Time:2020/1/10 19:47
#@Author:金波
#@Email:1258804025@qq.com
#@File:人民网.py
#@Software:PyCharm
import requests
from lxml import html
import datetime
n=100000
today= datetime.date.today() # 获取今天的时间
for i in range(n): #循环获取数据十万次链接中的数据
    data = today + datetime.timedelta(days=-i)#timedelta()函数我先用date()函数输入三个参数（2016，8，5），today的值便是2016-8-5，那如果我要第二天的日期，也就是2016-8-6，即5+1，这时的+1便是+timedelta(days=1)，里面参数days决定每一次加多少。
    # print(datetime.timedelta(days=-i))
    rule_data = data.strftime("%Y-%m/%d")# 将获得的日期进行格式化
    print(rule_data)
    root_url='http://kazakh.ts.cn/system/'
    'http://kazakh.ts.cn/system/2020/05/09/036255958.shtml'
    last_url="/nbs.D110000renmrb_01.htm"
    # url='http://paper.people.com.cn/rmrb/html/2020-01/04/nbs.D110000renmrb_01.htm' #需要爬数据的网址
    url=root_url+str(rule_data)+last_url
    # print(url)
    page=requests.Session().get(url)#说的明白点就是session相当于一个虚拟的浏览器，在这个浏览器上处于一种保持登录的状态。
    print(page.content)
    tree=html.fromstring(page.content)#解析为字节
    # print(tree)
    # category = tree.xpath('.//div[@id="pageList"]//a//text()')
    # for c in category:
    #     print(c.split("：")[1].strip("'"))
    # exit(1)
    # result=tree.xpath('.//div[@id="pageList"]//a[contains(text(),"要闻")]//@href') #获取需要的数据
    # result = tree.xpath('.//div[@id="pageList"]//a[@id="pageLink"]//@href')  # 获取需要的数据
    result = tree.xpath('.//div[@id="pageList"]//a[@id="pageLink"]//@href')
    print('result',result)
    for r in result:
        if r.startswith("./"):
            now_url=root_url+str(rule_data)+r[1:]
        else:
            now_url = root_url + str(rule_data)+"/"+r
        # print(now_url)
        page1 = requests.Session().get(now_url)
        tree1 = html.fromstring(page1.text)
        result1 = tree1.xpath('.//div[@id="titleList"]//@href')  # 获取需要的数据
        for txt_page in result1:
            txt_page_url=root_url + str(rule_data)+"/"+txt_page
            # print(txt_page_url)
            txt_page_response = requests.Session().get(txt_page_url)
            txt_tree = html.fromstring(txt_page_response.content)
            txt = txt_tree.xpath('.//div[@class="c_c"]//p//text()')  # 获取需要的数据
            with open("./txt/"+str(txt_page).split(".")[1]+".txt","w",encoding="utf-8") as writef:
                for t in txt:
                    writef.write(t+"\n")
