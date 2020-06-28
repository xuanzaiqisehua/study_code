from lxml import etree
# 参考：  https://www.cnblogs.com/zhangxinqi/p/9210211.html#_label2
'''XPath常用规则
nodename :选取此节点的所有子节点
/:从当前节点选取直接子节点
//:从当前节点选取子孙节点
.:选取当前节点
..:选取当前节点的父节点
@:选取属性
*:通配符，选择所有元素节点与元素名
@*:选取所有属性
[@attrib]:选取具有给定属性的所有元素
[@attrib='value']:选取给定属性具有给定值的所有元素
[tag]:选取所有具有指定元素的直接子节点
[tag='text']:选取所有具有指定元素并且文本内容是text节点'''
text='''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">第一个</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0"><a href="link5.html">a属性</a>
     </ul>
 </div>
'''
#************************读取文本解析节点
'''html=etree.HTML(text)# 初始化生成一个Xpath解析对象
result=etree.tostring(html,encoding='utf-8')#解析对象输出代码
# print(result)   #etree会修复HTML文本节点
# print(type(html))
# print(type(result))
print(result.decode('utf-8'))'''
#*************************读取HTML文件进行解析
'''html=etree.parse('text.html',etree.HTMLParser())##指定解析器HTMLParser会根据文件修复HTML文件中缺失的如声明信息
result=etree.tostring(html)   #解析成字节
#result=etree.tostringlist(html) #解析成列表
print(type(html))
print(type(result))
print(result)'''
#*************************获取所有节点
html=etree.parse('text.html',etree.HTMLParser())##指定解析器HTMLParser会根据文件修复HTML文件中缺失的如声明信息
'''result=html.xpath('// *')   #//代表获取子孙节点，*代表所有
print(type(html))
print(type(result))
print(result)
result1=html.xpath('//li/a') #通过追加/a选择所有li节点的所有直接a节点，因为//li用于选中所有li节点，/a用于选中li节点的所有直接子节点a
print(result1)'''
import datetime
today= datetime.date.today()
print(today)
for i in range(5):
    data = today + datetime.timedelta(days=-i)  # timedelta()函数我先用date()函数输入三个参数（2016，8，5），today的值便是2016-8-5，那如果我要第二天的日期，也就是2016-8-6，即5+1，这时的+1便是+timedelta(days=1)，里面参数days决定每一次加多少。
    # print(datetime.timedelta(days=-i))
    rule_data = data.strftime("%Y-%m/%d")
    print('111 ',rule_data)














