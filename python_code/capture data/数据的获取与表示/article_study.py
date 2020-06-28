# 文件article.txt 中存放了一篇文章，假设文章中标点仅包含","、"!"、"?"和"..."、，编程找出其中最长的单词并输出
'''
f.read:通常读取整个文件以字符串的内容读出，f.readline:通常读取一行，f.readlines：通常读取全部文件内容并以每行一个列表的方式返回
lst1=' '.join(lst)#连接字符串''.join(str)引号里面可用空格，逗号等连接
lst2=lst1.replace('\n','.')#后边的内容替换掉前边的
list.sort()和Python内建函数sorted()用法差不多，区别在于list.sort()改变原来列表，而sorted返回一个新列表list，
如果想逆序reverse设置为True即可：sorted(序列，reverse=True)
sorted高级用法，如果处理的数据元素为多维，sorted函数中的key参数可传入一个自定义函数
l=[('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
sorted(l, key=lambda x:x[0]) 输出：[('a', 1), ('b', 2), ('c', 6), ('d', 4), ('e', 3)]
sorted(l, key=lambda x:x[1])输出： [('a', 1), ('b', 2), ('e', 3), ('d', 4), ('c', 6)]
sorted(l, key=lambda x:x[1], reverse=True) 输出：[('c', 6), ('d', 4), ('e', 3), ('b', 2), ('a', 1)]
'''
import re
with open('article.txt',encoding='utf-8') as f:
    lst=f.read()
words=lst.split()#将字符串分割为一个一个单词存放在列表中返回
lst=[]
for word in words:
    if word[-3:]=='...':
        word=word[:-3]
        lst.append(word)
    if word[-1] in ',.?!':
        word=word[:-1]
    lst.append(word)
result=sorted(lst,key=len,reverse=True)# 按长度逆序排列
maxlen=len(result[0])
# print(maxlen)
#寻找长度最长的单词，如果最长的单词有多个去掉相同
for word in set(words):
    n=len(word)
    if n==maxlen:
        print(word)