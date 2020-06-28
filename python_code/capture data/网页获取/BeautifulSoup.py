# (1)
import requests
url='http://www.baidu.com'
# print('第一种方法')
# response1=requests.get(url)
# print(response1.status_code)
# print(len(response1.text))
print('第二种方法 ')
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}
response2=requests.get(url,headers=headers).text
print(response2)
# print('第三种方法')
#(2)
# BeautifulSoup解析器使用
# from bs4 import BeautifulSoup
# import  re
# html = """
# <html>
#     <head>
#         <title>The Dormouse's story</title>
#     </head>
#     <body>
#         <p class="story">
#             Once upon a time there were three little sisters; and their names were
#             <a href="http://example.com/elsie" class="sister" id="link1">
#                 <span>Elsie</span>
#             </a>
#             <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
#             and
#             <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
#             and they lived at the bottom of a well.
#         </p>
#         <p class="story">...</p>
# """
# soup=BeautifulSoup(html,'lxml')
# print(soup.prettify())#输出HTML页面所有内容
# print(soup.title)#输出<title>The Dormouse's story</title>
# print(soup.title.string)#输出title的文本内容：
# print(soup.title.name) #输出title标签
# print(soup.title.parent.name)#输出title的父级标签
# print(soup.p['class'])#输出p的类别
# print(soup.p.contents)#输出标签P包含的内容
# print(soup.p.children)#soup.p.children是一个迭代对象，而不是列表，只能通过循环的方式获取素有的信息
# for i,child in enumerate(soup.p.children):
#     print(i,child)
# print(soup.a)
# print(soup.find_all('a'))
# print(soup.find(id='link3'))
# for link in soup.find_all('a'):
#     print(link.get('href'))
#     print(soup.get_text)
# soup.a.next_siblings #获取后面的兄弟节点
# soup.a.previous_siblings #获取前面的兄弟节点
# soup.a.next_sibling #获取下一个兄弟标签
# soup.a.previous_sinbling #获取上一个兄弟标签
#(4)find_all(name,attrs,recursive,text,**kwargs) 可以根据标签名，属性，内容查找文档
# html='''
# <div class="panel">
#     <div class="panel-heading">
#         <h4>Hello</h4>
#     </div>
#     <div class="panel-body">
#         <ul class="list" id="list-1" name="elements">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#             <li class="element">Jay</li>
#         </ul>
#         <ul class="list list-small" id="list-2">
#             <li class="element">Foo</li>
#             <li class="element">Bar</li>
#         </ul>
#     </div>
# </div>
# '''
# find_all(name)
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all('ul'))
# print(type(soup.find_all('ul')[0]))
#find_all(attrs)
# attrs可以传入字典的方式来查找标签，但是这里有个特殊的就是class,因为class在python中是特殊的字段，
# 所以如果想要查找class相关的可以更改attrs={'class_':'element'}或者soup.find_all('',{"class":"element})，
# 特殊的标签属性可以不写attrs
# print(soup.find_all(attrs={'id':'list-1'}))
# print(soup.find_all(attrs={'name':'elements'}))
# print(soup.find_all(text='Foo'))
#find返回的匹配结果的第一个元素
# 其他一些类似的用法：
# find_parents()返回所有祖先节点，find_parent()返回直接父节点。
# find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
# find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。
# find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
# find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点
#通过select()直接传入CSS选择器就可以完成选择
# 熟悉前端的人对CSS可能更加了解，其实用法也是一样的
# .表示class #表示id
# 标签1，标签2 找到所有的标签1和标签2
# 标签1 标签2 找到标签1内部的所有的标签2
# [attr] 可以通过这种方法找到具有某个属性的所有标签
# [atrr=value] 例子[target=_blank]表示查找所有target=_blank的标签
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
# print(soup.select('.panel .panel-heading'))
# print(soup.select('ul li'))
# print(soup.select('#list-2 .element'))
# print(type(soup.select('ul')[0]))
# for li in soup.select('li'):#通过get_text()就可以获取文本内容
#     print(li.get_text())
# for ul in soup.select('ul'):
#     print(ul['id'])
    # print(ul.attrs['id'])
#(3)正则表达式
# a='aa+10+20'
# regex1=re.compile(r'a.*?b')
# regex2=re.compile(r'a.*b')
# print(regex1.findall(a),regex2.findall(a))
# regex3=re.compile(r'\+')
# regex4=re.compile(r'(\d+)([+])(\d+)')
# print(regex3.split(a))
# print(re.sub(r'\+','*',a))
# print(regex4.search(a).group())