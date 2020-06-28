'''
‘r’只读模式，必须打开一个已有的文件，且只能执行读操作。
‘r+’读+追加模式，可读可写，与‘r’相同之处在于也是必须打开一个已有的文件，不同的是它可写可读，而且写与读不分先后，即随时都可进行读与写。（写为追加在文件末尾）
‘w’只写模式，打开即默认创建一个新的空文件，当然若打开的是已有文件，则清空文件，且只能执行写操作。
‘w+’写读模式，打开创建新文件，因此需要先把内容写进去在读。即保证文件有内容通过移动光标来读自己想要的部分。
‘a’追加模式，若打开的是已有文件则直接对已有文件操作，若打开文件不存在则创建新文件，只能执行写（追加在后面），不能读。即追加写。
‘a+’追加读写模式，打开文件方式同‘a’一样，写方式也和'a'一样，但是可以读。且是任意时刻读写。需要注意的是你若刚用
‘a+’打开一个文件，则不能立即读，因为此时光标已经是文件末尾，除非你把光标移动到初始位置或任意非末尾的位置。
 文件游标移动操作: seek(offset,wheece)
 offset:需要偏移的字节数，whence:表示从哪个位置开始偏移，0：文件开头开始，1：当前位置，2 ：文件末尾
'''
#打开文件夹
# f1=open('./result.txt')
# f2=open(r'./result1.txt',"w")
# f3=open('record.dat','wb',0)
#写文件
# with open('companies.txt','w+') as f1:
#     result1=f1.write('Goole \n Microsoft \nCorporation \nApple')
# #读文件：
# with open('companies.txt') as f2:
#     result2=f2.read(5)#读取5个字节
# 在文件的字符串前加上1、2、3、后写到另一个文件中
# with open('companies.txt','r') as f3:
#     results=f3.readlines()
# for i in range(len(results)):
#     results[i]=str(i+1)+' '+results[i]
# with open('scompanies.txt','w') as f5:
#     f5.writelines(results)
# 写入数据
# with open('D:\\python code\\data processing\\firstpor.txt','r') as f1:
#    cNames=f1.readlines()
# for i in range(0,len(cNames)):
#     cNames[i]=str(i+1)+" "+cNames[i]
# with open('newfirstpor.txt','w') as f2:
#     f2.writelines(cNames)
# s='Tencent Tenchonogy Company Limited'
# with open('firstpor.txt','a+') as f:
#     f.writelines('\n')
#     f.writelines(s)
#     f.seek(0)
#     cNames=f.readlines()
# print(cNames)
#读取数据，统计文件行数
# file_name='firstpor.txt'
# try:
#     with open(file_name) as f:
#         data=f.readlines()
# except FileNotFoundError:
#     print(file_name+"dos not exist")
# lens=len(data)
# print('firstpor.txt'+' has '+str(lens)+' lines')
# import os
# import shutil
# def countlines(fname):
#     try:
#         with open(fname,encoding='utf-8') as f:
#             data=f.readlines()
#     except FileNotFoundError:
#         print(fname+'does not exost')
#     lens=len(data)
#     print(fname.split('\\')[1]+' has '+str(lens) + " lenes")
# # files=['firstpor.txt','newfirstpor.txt']
# # for fname in files:
# #     countlines(fname)
# path='.//testdata'
# for fname in os.listdir(path):
#     if fname.endswith('.txt'):
#         file_path=os.path.join(path,fname)
#         print(file_path)
#         countlines(file_path)
#         if os.path.exists('./output'):
#             shutil.rmtree('./output')
#         os.mkdir('./output')
# from bs4 import BeautifulSoup
# markup='<p class="title"><b>The Little Prince</b></p>'
# soup=BeautifulSoup(markup,'lxml')
# print(soup.p)
# print(r'.//testdata')
# age=21
# height=1.758
# print('Age:{0:<5d},Height:{1:5.2f}'.format(age,height))
# song='Blowing in the wind'
# print(song.find('the'))
# print(song.lower())
# print(song.split(' '))
# print(song.replace('the','that'))
# alist=['hello','word']
# a=' '.join(alist)
# print(a)
# b="你好"
# b1=b.encode('utf-8')
# astr='what do you think of this saying"No pain,No gain"?'
# lindex=astr.index('\"',0,len(astr))
# rindex=astr.rindex('\"',0,len(astr))
# tempstr=astr[lindex+1:rindex]
# if tempstr.istitle():
#     print('yes')
# else:
#     print('no')
# from functools import reduce
# lst=['3','2','5','8','1']
# lst1=list(map(lambda x:x*2,lst))
# print(lst1)
# lst2=list(filter(lambda x:x%2==0,lst))
# print(lst2)
# lst3=reduce(lambda x,y:x+y,lst)
# astr='hello,word'
# bstr=astr[:7]+'python!'
# count=0
# for ch in bstr[:]:
#     if ch in ',!?':
#         count+=1
# print(bstr,count)
#format使用
# age,hight=21,1.758
# print('{0:<5f},{1:5.2f}'.format(age,hight))#{:}冒号前面是位置，后面是格式
# cCode=['AXP','BA','CAT','CSCO','CVX']
# cPrece=['78.51','184.76','33.71','106.09','4.5']
# for i in range(5):
#     print('{:<8d}{:<8s}{:s}'.format(i,cCode[i],cPrece[i]))
#
astr='What do you think of this saying"No Pain,No Gain"'
lindex=astr.index('\"',0,len(astr))
rindex=astr.rindex('\"',0,len(astr))
tempstr=astr[lindex+1:rindex]
if tempstr.istitle():
    print('Yes')
else:
    print('no')
print(tempstr.title())
