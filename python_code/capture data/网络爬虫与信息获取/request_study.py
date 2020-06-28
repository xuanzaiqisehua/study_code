'''Response 对象的属性：
（1） r.status_code :HTTP 请求的返回状态，200表示成功，404表示失败
（2） r.text :HTTP 响应内容的字符串形式，即url对应的页面内容
（3） r.encoding :从HTTP header中猜测出的响应内容编码方式,如果header中有charset字段，说明访问的服务器对其资源的编码是有要求的，
这样的编码将会存储在header中被获得，并不是所有的服务器对其资源都有编码要求，如果hearder中没有charset字段，那么将会返回ISO-8859-1
（4） r.apparent_encoding : 根据页面内容中分析出的响应内容编码方式（备选编码方式）
（5）r.content : HTTP 响应内容的二进制形式
网页爬取通用代码框架：准确的可靠的爬取网页内容，网页连接有风险，异常处理很重要，request的异常
（1）requests.ConnectionError :网络连接错误异常，如 DNS 查询失败、拒绝连接等，DNS----- 域名系统（服务）协议（DNS），域名解析
（2）requests.HTTPError: HTTP错误异常，HTTP协议层出现异常
（3）requests.URLRequired : URL 缺失异常
（4）requests.TooManyRedirects : 超过最大重定向次数，产生重定向异常，重定向数超过request库设置的最大重定向数，对复杂连接进行访问时可能产生
（5）requests.ConnectTimeout : 连接远程服务器超时异常
（6）requests.Timeout : 请求URL超时，产生超时异常
r.raise_for_status() :如果是200，返回正常，如果不是200，产生异常requests.HTTPError
'''
'''import requests
r=requests.get('http://www.baidu.com')
# ********************通用框架*****************
def getHTMLText(url):
   try:
       r=requests.get(url,timeout=30) #（3,7） 第一个是连接时间，第二个是读取时间 如果只写一个的话，就是连接和读取的timeout总和
       r.raise_for_status()# 如果返回不是200，则引发异常
       r.encoding=r.apparent_encoding # 改变页面内容编码格式，将分析出的页面编码格式赋值解析页面
       return  r.text
   except:
       return  '产生异常'
if __name__=='__main__':
    url='http://www.baidu.com'
    print(getHTMLText(url))'''
# print(r.status_code) # 返回状态码为200，说明请求成功
# print(r.headers)# 返回get()请求获得页面的头部信息
# print(r.text)
# print(r.encoding)
# print(r.apparent_encoding) # 输出utf-8，此时可用utf-8替换它的编码方式在输出页面内容
# r.encoding='utf-8' # 将编码格式改为'utf-8'后页面内容正常显示
# print(r.text)
# print(r.raise_for_status)
# ********************HTTP协议及requests库方法*****************
'''
Requests 库的7个主要的方法
1、requests.request(method，url，**kwargs): 构造一个请求，支撑以下各方法的基础方法
method：请求方式(7种：get/head/put/post/patch/delete/options)options:指获取服务器与客户端打交道的参数；使用是可以直接使用requests.request('GET',url,**kwargs),也可以使用以下的方法获取
**kwargs:控制访问的参数，均为可选项
（1）params：
kv={'key1':'value1','key2':'value2'}
r=requests.request('GET','http://python124.io/ws',params=kv)
print(r.url)
data:用于向服务器提交，提交的内容提交到URL链接对应位置作为数据存储
kv={'key1':'value1','key2':'value2'}
r=requests.request('GET','http://python124.io/ws',data=kv)
（2）body='主体内容'
r=requests.request('GET','http://python124.io/ws',data=body)
print(r.url)
（3）json:JSON格式的数据（类似字典），作为Request的内容
kv={'key1':'value1'}
r=requests.request('POST','http://python123.io/ws',json=kv)
（4）headers：字典，定制访问某个HTTP的协议头
hd={'user-agent':'Chrome/10'} # Chrome浏览器第10个版本
r=requests.request('POST','http://python123.io./ws',headers=hd)# 模拟任何一个想要模拟的浏览器向服务器发起访问
（5）cookies：字典或CookieJar，从http中解析cookie
     auth :元组，支持HTTP认证功能
    cookies 和 auth都是request库的高级字段
（6）files: 字典类型，向服务器传输文件时使用
fs={'file':open('data.xls','rb')}
r=requests.request('POST','http://python123.io./ws',files=fs)
（7）timeout : 设定超时时间，秒为单位
（8）proxies：字典类型，设定访问代理服务器，可以增加登录认证；使用代理服务器爬取可以有效隐藏爬取用户真实的IP地址
pxs={'http':'http://user:pass@10.10.10.1:1234'
      'https':'http://user:pass@10.10.10.1:4321'}
r.requests.request('GET','http://www.baidu.com',proxies=pxs)
2、requests.get(): 获取HTML网页的主要方法，对应于HTTP的GET------请求获取URL位置的资源
3、requests.head(): 获取HTML网页头信息的方法，对应于HTTP的HEAD------获取该资源的头部信息
4、requests.post(): 向HTML网页提交post请求的方法，对应于HTTP的POST------请求URL位置资源后附加新的数据
5、requests.put(): 向HTML网页提交put请求的方法，对应于HTTP的PUT------请求向URL位置存储一个资源，覆盖原URL位置的资源
6、requests.patch(): 向HTML网页提交局部修改请求，对应于HTTP的PATCH------改变该处资源的部分内容
7、requests.delete(): 向HTML网页提交局部删除请求，对应于HTTP的DELETE------请求删除URL位置存储的资源
HTTP协议：
（1）采用URL作为定位网络资源的表示，URL格式：http://host[:port][path];host:合法的Internet主机域名或IP地址；port：端口号，缺省端口为80；path：请求资源的路径；例如：http：//www.bit.edu.cn---北京理工大学网址；http://220.181.111.188/duty:主机地址为：
220.181.111.188的duty文件夹中的资源
'''
import requests
url='http://item.jd.com/2967929.html'
try:
    r=requests.get(url)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
except:
    print('爬取失败')
r.request.headers # 查看请求的页面的header










