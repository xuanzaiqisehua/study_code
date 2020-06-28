''' 反扒机制 https://blog.csdn.net/qq_34109717/article/details/82953705
#******************************User-Agent*********************************
向访问网站提供你所使用的浏览器类型、操作系统及版本、CPU 类型、浏览器渲染引擎、
浏览器语言、浏览器插件等信息的标识:参考https://blog.csdn.net/rj042/article/details/6991441
# （1）将常见的User-Agent封装到一个.py文件中，命名为useragent.py
爬虫过程中导入useragent.py,随机选择ua_list中的user-agent
import random,requests
from useragent import ua_list
#随机获取User-Agent
headers = {'User-Agent':random.choice(ua_list)}
r= requests.get(url='https://www.baidu.com',headers=headers)
（2）Python中加载fake_useragent库，随机生成User-Agent添加到headers中
from fake_useragent import UserAgent
ua=UserAgent()
print(ua.IE)#chrome 浏览器
# 查看随机值
for i in range(3):
    print('')
    # print(ua.random)
# 爬虫应用
import requests
headers={'User-Agent':ua.random}
url='http://www.baidu.com'
r=requests.get(url,headers=headers)
print(r.content)
print(r.text)
'''
'''
#******************************基于IP反爬虫机制的反反爬虫方法，构建可用代理池*********************************
参考博客：
     http://icanhazip.com/ 这个网站来检测你的代理IP是否设定成功
（1）https://blog.csdn.net/a18612039484/article/details/99821226
（2）https://blog.csdn.net/weixin_40372371/article/details/80154707?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
主要思路
1.从代理ip网站爬取IP地址及端口号并储存
2.验证ip是否能用
3.格式化ip地址
4.在requests中使用代理ip爬取网站
# 国内高匿ip：https://www.xicidaili.com/nn/'''
import requests,random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
def _requestUrl(index):
    src_url = 'http://www.xicidaili.com/nt/'
    url = src_url + str(index)
    if index == 0:
        url = src_url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    }
    response = requests.get(url, headers=headers)
    return response.text
# 解析网页数据，获取ip和端口信息
def parseProxyIpList(content):
    list = []
    soup = BeautifulSoup(content, 'html.parser')
    ips = soup.findAll('tr')
    for x in range(1, len(ips)):
        tds = ips[x].findAll('td')
        ip_temp = 'http://' + tds[1].contents[0] + ':' + tds[2].contents[0]
        print('发现ip：%s' % ip_temp)
        list.append(ip_temp)
    return list
# 过滤有效的ip信息
def filterValidProxyIp(list):
    print('开始过滤可用ip')
    validList = []
    for ip in list:
        if validateIp(ip):
            print('%s 可用' % ip)
            validList.append(ip)
        else:
            print('%s 无效' % ip)
    return validList
# 验证ip是否有效
def validateIp(proxy):
    proxy_temp = {"http": proxy}
    url = "http://ip.chinaz.com/getip.aspx"
    try:
        response = requests.get(url, proxies=proxy_temp, timeout=5)
        return True
    except Exception as e:
        return False
# 获取可用的代理ip列表
def getProxyIp():
    allProxys = []
    startPage = 0
    endPage = 1
    for index in range(startPage, endPage):
        print('查找第 %s 页的ip信息' % index)
        # 请求url，获取网页数据
        content = _requestUrl(index)
        # 解析网页数据，获取ip和端口信息
        list = parseProxyIpList(content)
        # 过滤有效的ip信息
        list = filterValidProxyIp(list)
        # 添加到有效列表中
        allProxys.append(list)
        print('第 %s 页的有效ip有以下：' % index)
        print(list)
    print('总共找到有效ip有以下：')
    # 找到可用ip[['http://163.125.114.143:8118', 'http://120.78.79.150:8081', 'http://60.191.11.246:3128'], ['http://122.224.65.198:3128',
    # 'http://120.78.79.150:8081'], ['http://220.168.86.37:3128', 'http://116.62.215.123:8118']]
    print(allProxys)
    return allProxys
def getHTML(url):
    headers = {'User-Agent': us.random}
    ip_list = getProxyIp()
    ip=random.choice(ip_list)
    proxy = {"http": ip}
    # proxy='http://163.125.114.143:8118'
    try:
        r=requests.get(url,headers,proxies=proxy,timeout=5, retry=2) # timeout: 超时, retry：重试
        r1 = requests.get(url)
        print('不使用代理的时候:{}'.format(r.text))
        print('使用代理的时候:{}'.format(r1.text))
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('产生异常')
url='http://icanhazip.com/'
us=UserAgent()
html=getHTML(url)
print('使用代理的时候：{}'.format(html))
'''#******************selenium最初是一个自动化测试工具，而爬虫中使用它主要是为了解决requests无法执行javaScript代码的问题***********
selenium:https://www.cnblogs.com/lweiser/p/11045023.html,我们一般用它来做登录验证'''






















