#字符串连接的三种方式;
# 1 直接用+操作
str1='I '+ 'am '+ 'a'+'student'
# 2 join 方法
listStr=['I ', 'am ', 'a','student']
str2=''.join(listStr)
# 3 替换
# str3='%s%s%s%s'%('I', 'am', 'a','student')
# str4='{0},{1},{2},{3}'.format('I', 'am', 'a','student')
# print(str4)
''' ^, <, > 分别是居中、左对齐、右对齐，后面带宽度，
 : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。
+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
b、d、o、x 分别是二进制、十进制、八进制、十六进制。'''

# 1 从键盘输入整数n(1-9之间)，对于1-100之间的整数删除包含n并且能被n整除的数，
# 例如如果n为6，则要删除包含6，如6,16这样的数以及6的倍数如12和18等，输出所有满足条件的数，要求每满10个数换行
'''n=int(input('Enter the number:'))
count=0
new_str=''
print('The result string:')
for i in range(1,101):
    s=str(i)
    if i%n!=0 and s.find(str(n))==-1:
        new_str=new_str+s+','
        count+=1
    if count%10==0:
        print(new_str[:-1])
        new_str=''
if len(new_str)>0:
    print(new_str)'''
##filter 函数：将不符合条件的序列过滤掉，filter(function, iterable)，参数1：函数，参数2：可迭代序列,然后可以将结果转换为列表返回
# map() 会根据提供的函数对指定序列做映射。map(function, iterable)eg：map(square, [1,2,3,4,5]) # 计算列表各个元素的平方
# s=input()
# i=int(s)
# num=list(map(str,filter(lambda x:x%i and s not in str(x),range(1,101))))
# for i in range(0,len(num),10):# i 在0-len(num)范围，间隔为10
#     print(','.join(num[i:i+10]))






