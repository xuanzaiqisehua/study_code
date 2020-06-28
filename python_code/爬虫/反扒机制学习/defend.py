import requests
import random
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
# 获取网页内容
def getHTMLText(url,proxies):
    try:
        r=requests.get(url,proxies=proxies,headers=headers)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return  r.text
    except:
        print('错误')
# # 获取所有代理IP的地址和端口号
def get_ip_list(url):
    web_data=requests.Session().get(url,headers=headers)# Seession 保持登录状态进行后续操作
    soup=BeautifulSoup(web_data.text,'html.parser')
    tr=soup.find_all('tr')
    ip_list=[]
    for i in range(1,len(tr)):
        ip_info=tr[i]
        tds=ip_info.find_all('td')
        ip_list.append(tds[1].text+':'+tds[2].text) # 提取所有的IP地址和端口
    for ip in ip_list:
       proxy_host='https://'+ip
       proxy_host1 = 'http://' + ip
       proxy_temp={'https':proxy_host,
                        'http': proxy_host1}
       print(proxy_temp)
    return proxy_temp
# 测试代理,建立代理IP池
def proxy_pool(headers):
    # 调用上面函数
    proxy_list = get_ip_list(url)
    # 可用代理IP列表
    useful_proxy = []
    # 测试代理是否可用
    for proxy in proxy_list:
        # proxy: {'http':'http://xxxx:xx'}
        try:
            res = requests.get(
                url='http://httpbin.org/get',
                headers=headers,
                proxies = proxy,
                timeout = 5
            )
            print(res.text)
            useful_proxy.append(proxy)
        except Exception as e:
            print('{}不能用'.format(proxy))
            continue
    return useful_proxy

if __name__ == '__main__':
    us=UserAgent()
    headers={'User-Agent':us.random}
    url='https://www.xicidaili.com/nn/'
    proxy_pool(headers)








