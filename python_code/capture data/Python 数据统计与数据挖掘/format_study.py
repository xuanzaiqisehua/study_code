''' 函数参数：位置参数，默认参数，可变参数，关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装成一个dict，使用**表示关键字参数；针对位置参数少传一个参数报错的问题，是否可以设置一个默认的值呢？这样在函数调用时不用传入该参数时也不会报错。这就是“默认参数”。
（1）为位置参数和 默认参数
# def default_fun(a,b,c = 2019):# a,b为位置参数，c=2019 默认参数
print("a = {0},b = {1},c = {2}".format(a,b,c))
（2）# 命名参数：
采用指定形参的具体实参值是可以增加函数调用的灵活性。
比如：postion_fun(a,b,c)
postion_fun(10,59,2019) -------a=10,b=59,c=2019
postion_fun(c=10,b=59,a=2019) --------a=2019,b=59,c=10
（3）可变参数：元组
在函数定义时，用*param（一颗星号）表示收集多个参数值组成一个元组。
def tuple_fun(a,b,*c):
  print('a={0},b={1},c={2}'.format(a,b,c))
tuple_fun(10,59,2019,'职说职语')  -------a=10,b=59,c=(2019,'职说职语')
（4） 可变参数：字典，
在函数定义时，用**param（两颗星号）表示收集多个参数值组成一个字典。
def tuple_fun2(a,b,**c):
  print('a={0},b={1},c={2}'.format(a,b,c))
tuple_fun2(10,50，name='职说职语',job='自由工作者') -------a=0，b=50,c={'name':'职说职语','job':'自由工作者'}
（5）可变参数：元组与字典参数融合
两种参数都可以出现在一个函数中，并且按照实参与形参的对应位置进行结果组装。
def tuple_fun3(a,b,*c,**d)：
 print('a={0},b={1},c={2},d={3}'.format(a,b,c,d))
tuple_fun3(10,59,2019,"职说职语",name='职说职语',job='自由工作者')
（6）强制命名参数：定义函数时把元组参数放到最前面，那调用函数时，该参数默认是收集所有传入的实参后组成元组，如果要是后面两个参数有值并保证函数调用正常，则必须采用强制命名参数方式制定实参传入形参的值。
def tuple_fun4(*a,b,c):
 print('a={0},b={1},c={2}'.format(a,b,c))
tuple_fun4(10,59,2019,'职说职语') ------错误，可变参数a 将实参全部组合为元组，缺失两个参数
tuple_fun4(10,59,b=2019,c='职说职语') ------a=(10,59),b=2019,c=职说职语
tuple_fun4(10,b=2019,c='职说职语') --------a=(10,),b=2019,c=职说职语
'''
# 默认位置参数
'''print('{} {}'.format('hello','world'))
print('{0} {1}'.format('hello','world'))
print('{1} {0}'.format('hello','world'))# {1}{0} 表示位置
print('{1} {0} {1}'.format('hello','world'))# {1}{0} 表示位置'''
# 关键字参数
# print('网站名：{name},地址:{url}'.format(name='菜鸟教程',url='www.runb,com'))
#通过字典设置参数
site={'name':'菜鸟教程','url':'www.runoob.com'}
print('网站名：{name},地址：{url}'.format(**site))






