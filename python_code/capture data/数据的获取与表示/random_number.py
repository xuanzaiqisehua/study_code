'''
(1)random.random()返回一个随机数，范围在0-1内import random print ("随机数: ", random.random())
(2)random.uniform()返回指定范围内随机数：print (random.uniform(2, 6))
(3)random.randint()返回指定范围整数：print (random.randint(6,8))
(4)random.randrange(上限，下限，递增量)在指定范围中递增选择随机数
(5)random.choice()从一个序列中获取随机元素
(6)random.shuffle()函数是将一个列表中的元素打乱，随机排序num = [1, 2, 3, 4, 5] random.shuffle(num)
(7)random.sample(序列，片段长度)函数是从指定序列中随机获取指定长度的片段,原有序列不会改变 random.sample(num, 3)
'''
# 2 请用随机函数产生500行1-100之间的随机整数存入文件random.txt中，编程寻找这些整数的众数并输出，众数即为一组数中出现最多的数
import random
i=0
with open('random.txt','w+') as f:# w 为只写，w+为写读，写完在读
    while i < 10:
        i += 1
        f.write(str(random.randint(1,5)))
        f.write('\n')
    f.seek(0)# 文件游标移动操作
    num=f.readlines()
nums=[tem.strip('') for tem in num]#strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
print(nums)
#  注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符
lst=[0]*11 # 设置一个全为0的列表，列表中元素个数为11
setnums=set(nums) #set()函数创建一个无序不重复元素集,可进行关系测试,删除重复数据,还可以计算交集、差集、并集等
print(setnums)
for item in setnums:
    c=nums.count(item)#str.count(sub, start= 0,end=len(string)),用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。
    lst[int(item)-1]=c #将所有不重复的元素个数赋值给刚刚定义的列表
    print("数字{}出现次数为：{}".format(item,c))
for i in lst:
  if i==max(lst):
       print(i)


















