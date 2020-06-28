# 字典可以建立对象与对象之间的映射关系，pyhon内建的映射类型，key-value对，key可以为字符串、元组、序列等不可变类型，不能是可变列表
#常用函数len(dict),hash:判断某个元素是不是可哈希的（也就是不可变的）
#创建字典：（1）直接创建（2）利用dict函数
# ainfo={'Wangdachui':3000,'Niuyun':2000,'Linling':4500,'Tianqi':8000}
# info=[('Wangdachui',3000),('Niuyun',2000),('Linling',4500),('Tianqi',8000)]
# binfo=dict(info)
# cinfo=dict([['Wangdachui',3000],['Niuyun',2000],['Linling',4500],['Tianqi',8000]])#列表转为字典
# dinfo=dict(Wangdachui=3000,Niuyun=2000,Linling=4500,Tianqi=8000)
# finfo=dict((('Wangdachui',3000),('Niuyun',2000),('Linling',4500),('Tianqi',8000)))#元组转为字典
# #创建员工信息表将所有员工的工资默认值设置为3000
# ginfo={}.fromkeys(('Wangdachui','Niuyun','Linling'),3000)
# # 将已知姓名列表和工资列表，如何生成字典类型的员工信息表
# names=['Wangdachui','Niuyun','Linling','Tianqi']
# salaries=[3000,2000,4500,8000]
# # a = [1,2,3]  b = [4,5,6]  zipped = zip(a,b)  c = [4,5,6,7,8]
# #  打包为元组的列表 输出：[(1, 4), (2, 5), (3, 6)]   zip(a,c) #元素个数与最短的列表一致：[(1, 4), (2, 5), (3, 6)]
# # zip(*zipped) # *zipped 可理解为解压，返回二维矩阵式
# hinfo=dict(zip(names,salaries))#zip函数将其打包分组
# print()
#提取网页中获取数据列表中的数据并生成字典
'''lst=[('MMM', '3M', '158.66'), ('AXP', 'American Express', '129.87'), ('AAPL', 'Apple', '309.51'),
     ('BA', 'Boeing', '318.27'), ('CAT', 'Caterpillar', '131.35'), ('CVX', 'Chevron', '107.14'),
     ('CSCO', 'Cisco', '45.97'), ('KO', 'Coca-Cola', '58.40'), ('DIS', 'Disney', '138.31'),
     ('DOW', 'Dow Chemical', '46.07'), ('XOM', 'Exxon Mobil', '62.12'), ('GS', 'Goldman Sachs', '237.75'),
     ('HD', 'Home Depot', '228.10'), ('IBM', 'IBM', '143.73'), ('INTC', 'Intel', '63.93'),
     ('JNJ', 'Johnson & Johnson', '148.87'), ('JPM', 'JPMorgan Chase', '132.36'),
     ('MCD', "McDonald's", '213.97'), ('MRK', 'Merck', '85.44'), ('MSFT', 'Microsoft', '170.23'),
     ('NKE', 'Nike', '96.30'), ('PFE', 'Pfizer', '37.24'), ('PG', 'Procter & Gamble', '124.62'),
     ('TRV', 'Travelers Companies Inc', '131.62'), ('UTX', 'United Technologies', '150.20'),
     ('UNH', 'UnitedHealth', '272.45'), ('VZ', 'Verizon', '59.44'), ('V', 'Visa', '198.97'),
     ('WMT', 'Wal-Mart', '114.49'), ('WBA', 'Walgreen', '50.85')]
for element in lst:
    d={}
    d[element[0]]=element[2]'''

#字典的基本操作;
# ainfo={'Wangdachui':3000,'Niuyun':2000,'Linling':4500,'Tianqi':8000}
'''# 键值查找;两种方法：如果字典中不存在第一种有返回值None，第二种程序会中断
print(ainfo.get('mayun'))
print(ainfo['mayun'])
# 更新;
ainfo['Niuyun']=4000
# 添加
ainfo['mayun']=4000
print(ainfo)
# 成员判断：
result='mayun' in ainfo
print(result)
# 删除字典中成员
del ainfo['mayun']
print(ainfo)'''
#清空字典中的值
# binfo=ainfo
# ainfo={}#此时ainfo指向一个空字典，但是binfo还是指向原来ainfo的值
# print(binfo,ainfo)
# binfo=ainfo
# ainfo.clear()# clear方法会将ainfo和binfo中的值都清空
# print(binfo,ainfo)
# 输出所有的key或者value值
# name=ainfo.keys()
# print(name)
# # ainfo.items()输出所有的key以及value值,返回一个列表，列表元素为key和value组合而成，然后循环访问
# for k,v in ainfo.items():
#     print(ainfo.items(),k,v)
# 人事部门有两份人员和工资表，一份为原有信息，一份为更改人员和新进人员的信息，如何较快的获得完整信息表
# ainfo={'Wangdachui':3000,'Niuyun':2000,'Linling':4500,'Tianqi':8000}
# binfo={'Wangdachui':4000,'Niuyun':9990,'Wangzi':6000}
# ainfo.update(binfo) # 改变原有字典
# print(ainfo)
'''
javascript object notation,JS对象标记，一种轻量级的数据交换格式，由一组名称和值对组成
'''
import json # 一般json编码格式都与字典类似，所以处理json文件时可以采用字
# x={"name":'Niuyun',"address":{"city":"beijing","stree":"Chaoyang Road"}}
# json_str=json.dumps(x)#使用json.dumps() 函数就可以将字典或者其他格式的数据转换为json格式
# print(json_str)
# dict=json.loads(json_str)# 如果想还原格式用json.load()函数
# print(dict)

# 假如处理数据时数据格式为json格式，可以将其进行解码
# with open('文件名') as f:
#     date=json.load(f)
'''** 字典相关使用小案例
搜索引擎关键词查询
百度：http://www.baiddu.com/s?wd=%s
Bing
中国：http://cn.bing.com/search?q=%us
美国：http://www.bing.com/search?q=%us  #其中问号后面的wd或者q代表特征词=%s或者=%us就是我们要查询的关键词
问号后面就像一个字典可以通过创建字典的方式查询
'''
# 假如要用Bing搜索引擎查询 python dict
# import requests
# kw={'q':'python dict'}
# r=requests.get('http://cn.bing.com/search',params=kw)
# # r.url
# print(r.text)
'''python 中函数的参数形式
（1）位置或关键字参数
（2）仅位置参数
（3）可变长位置参数：元组可充当 *argst
（4）可变长关键字参数：字典可充当 **argsd
'''
# def func(args1,*argst,**argsd):
#     print(args1)
#     print(argst)
#     print(argsd)
# func('hello','Wangdachui','Niuyun','Linglin','mayun',a1=1,a2=2,a3=3)
# 字典小练习
# （1）统计英文单词词频
'''poem_EN='Life can be good,life can be sad,life is mostly cheerful,Bit sometimes sad.'
poem_list=poem_EN.split()
p_dict={}
for item in poem_list:
    if item[-1] in ',.\'"':
        item=item[:-1]
    # if item not in p_dict:
    #     p_dict[item]=1
    # else:
    #     p_dict[item]+=1
    #方法2
    p_dict[item]=p_dict.get(item,0)+1# get()方法判断该单词是否在字典中，如果不在就是0，如果在就加1
print(p_dict)'''
# (2)运动会班级人数统计排序
'''def  func(data):
    dict_data={}
    for item in data:
        num_data = item.split('_')
        a, b = num_data[0], num_data[1].strip()
        if a not in dict_data:
            dict_data[a] = [b]
        else:
            dict_data[a] += [b]
    sorted(dict_data.items(), key=lambda dict_data: len(dict_data[1]), reverse=True)
    print(dict_data)
if __name__=='__main__':
    try:
        with open('file.txt') as f:
            people=f.readlines()
    except FileNotFoundError:
        print('the file does not exits')
    else:
         result=func(people)'''
# 集合例---生成符合要求的学号
'''要求：1 函数func()的功能是利用班级信息的字典数据随机选择班级并生成一个随机学号。
注意：学号共有六位，前四位为班级编号，后2位为某同学在班级中的序号，如A00101，序号从01开始顺序编号，
并且不能超过该班级学生总数
2 __main__模块中包含班级信息字典，调用func()生成10个不重复的学生学号并输出。
其中，班级信息字典键为班级编号，值为对应班级的学生总数。例如，当给定的班级信息为
data={'A001':32,'A002':47,'B001':39,'B002':42}时，表示A001班级共有32为同学，以此类推'''
import random
def func(data):
    cls_no=random.choice(list(data.keys()))
    stu_no=random.randint(1,data[cls_no])
    return '{}{:02}'.format(cls_no,stu_no)
if __name__=='__main__':
    data={'A001':32,'A002':47,'B001':39,'B002':42}
    result=set()
    while len(result)<10:
        result.add(func(data))
    print(result)





















