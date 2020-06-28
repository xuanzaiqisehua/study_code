import numpy as np
# def npSum():
#     a=np.array([0,1,2,3,4])
#     b=np.array([9,8,7,6,5])
#     c=a**2+b**3
#     return a**2,b**3,c
# print(npSum())
# a=np.arange(10)
# b=np.ones((2,3,4))
# c=np.zeros((3,6),dtype=np.int32)
# d=np.full((2,3,4),25,dtype=np.int32)
# e=np.eye(5)#对角线全为1，正方形矩阵
# f=np.linspace(1,10,4)#等间隔划分数组，起始为1，结束为10，共四个数，endpoint如果为false，则最后分组的数字为结束数字10则重新划分
# g=np.linspace(1,10,4,endpoint=False)
# h=np.concatenate((f,g))
# # b1=b.reshape((3,8))#不改变原来数组的元素个数
# b2=b.resize((3,8))#将原数组改变为3*8维
# k=b.flatten()#将多维数组降维
# c1=c.astype((np.float))#数组类型变换
# d1=d.tolist()#将数组转换为列表
# print(d1)
# #数组的操作
# a=np.array([9,8,7,6,5,4,3,2,1])
# a1=a[1:7:2] #一维数组切片与Python的列表类似，索引从1开始到3（4不算）,步长为2 ,输出为[8 6 4 2]
# #多维数组的索引
# b=np.arange(24).reshape((2,3,4)) #索引从0开始,[[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], [[12, 13, 14, 15], [16, 17, 18, 19], [20, 21, 22, 23]]]
# b1= b[1,2,3]#输出 23
# b2= b[-1,-2,-3] #如果维度为负，从后往前数
# b3=b[:,:,-3]#第一个第二维度范围不关心，第三个维度为-3 [[1 5 9] [13 17 21]]
# b4=b[:,1,-3] #第一个第二维度为1，第三个维度为-3 [5 17]
# b5=b[:,1:3,:]#第二个维度为1到2,3不算,[[[4, 5, 6, 7], [8, 9, 10, 11]], [[16, 17, 18, 19], [20, 21, 22, 23]]]
# b6=b[:,:,::2]#第三个维度使用跳跃切片，步长为2，输出[[[0, 2], [4, 6], [8, 10]], [[12, 14], [16, 18], [20, 22]]]
# print(b6.tolist())
#数组的运算
#（1）数组与标量的运算相当于数组中每一个元素与这个标量进行运算
'''a=np.arange(24).reshape((2,3,4))
a=a/a.mean()
np.ceil()#表示大于等于这个元素的整数值，np.floor()表示小于这个元素的最大整数值，np.modf表示将元素的小数和整数部分分开并以独立的两个数组返回
np.sign表示计算元素的符号值
np.square(a)
a1=np.sqrt(a)
a2=np.ceil(a1)
a3=np.floor(a1)
a4=np.modf(a1)
print(a1,a4)
'''
# numpy常见应用
import numpy as np
# 创建一个10*10的全1的数组
'''x=np.ones((10,10))
x[1:-1,1:-1]=0
y=np.full((10,10),np.pi)# 创建一个全为π的数组
z=np.array([[1,2,3],[4,5,6]],dtype=np.float64)
z1=np.full_like(z,4)
# 创建一个对角线全为1，正方形矩阵
a=np.eye(10)# 比identity功能强大
a1=np.eye(8,k=1)#参数k=1表示向上偏移1，k=-2表示向下偏移2
b=np.identity(10)
# 如何使用函数从正态分布或者均匀分布中采样若干个数
c=np.random.normal(0,5,100)#期望和标准差分别设为0和5，采样100个数
d=np.random.uniform(-5,5,100)#均匀采样边界值分别设为-5到5，采样100个'''
# 有放回和无放回对数据进行采样
# A=np.random.rand(3,5)#通过本函数可以返回一个或一组服从“0~1”均匀分布的随机样本值。随机样本取值范围是[0,1)，不包括1。
# #从shape[0]当中随机选择两行，replace=True为有放回随机采样，出现的数字可重复，如果改为False则为不重复采样
# mask=np.random.choice(np.arange(A.shape[0]),2,replace=True)
# print(A[mask])
#创建一个0-100的数组
'''x=np.arange(1,100)
y=x<=50 #返回布尔类型
z=x[x<=50] #返回<=50的数
print(x[(x>50)&(x%2==0)])# 返回>=50且为偶数的数
x[x%2==0]=-1#把所有偶数都赋值为-1，这种方法会把修改原始数据，可以修改为where函数
x1=np.where(x%2==0,-1,x) #参数(条件，为真的时候值，为假的时候值)
print(x1)
'''
# 计算每个同学每门课与该课程的均值的差值
scores=np.array([[98,76,87],[76,88,91]])
score_mean=scores.mean(axis=1,keepdims=True)# axis=1行，axis=0为列,keepdims保持原来的维度（二维数组），才能用numpy的广播功能
print(scores-score_mean)
