# 在经过以timeout参数设定的秒数时间之后停止响应。基本上所有的生产代码都应该使用，如果不使用，程序将可能永远失去响应
# 1 requests连接超时:requests.exceptions.ConnectTimeout
import requests
'''try:
    r=requests.get('http://www.baidu.com',timeout=20)
    r.encoding=r.apparent_encoding
except requests.exceptions.ConnectionError:
    print('连接超时')
print(r.text)'''
#  2. 连接、读取超时，代理服务器没响应
'''若分别指定连接和读取的超时时间，服务器在指定时间没有应答，抛出 requests.exceptions.ConnectTimeout 
- timeout=([连接超时时间], [读取超时时间]) 
- 连接：客户端连接服务器并并发送http请求服务器 
- 读取：客户端等待服务器发送第一个字节之前的时间'''
'''try:
    r=requests.get('http://www.baidu.com',timeout=(20,10))
except requests.exceptions.ConnectionError:
    print('连接超时')
print(r.text)'''
# 3 代理连接不上
# try:
#     r=requests.get('http://www.baidu.com',timeout=(20,10))
# except requests.exceptions.ProxyErroy:
#     print('代理连接不上')
# print(r.text)