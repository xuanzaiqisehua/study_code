import requests
proxy={'http':'http://116.62.215.123:8118'}
html=requests.get('http://icanhazip.com')
html_proxy=requests.get('http://icanhazip.com',proxies=proxy)
print('不使用代理的时候:{}'.format(html.text))
print('使用代理的时候:{}'.format(html_proxy.text))