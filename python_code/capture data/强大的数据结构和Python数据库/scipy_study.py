'''
（1）scipy是一个基于Python的软件生态圈，包括NumPy，Scipy，Matplotlib和pandas核心库，具有丰富强大的数据结构和函数
非常流行的科学计算库，是Python的第三方扩展库
Scipy扩展python中原有的数据结构：ndarray(N维数组)，Series(变长字典)，DataFrame(数据框)
Scipy常用的数据库:Numpy:有强大的ndarray对象和ufunc函数
（2）Matplotlib：基于Numpy，二维绘制图库，简单快速地生成曲线图、直方图和散点图等形式的图。
常用的pyplot是一个简单提供类似MATLAB借口的模块
（3）基于Scipy还让Numpy数据结构，高效的Series(变长字典)，DataFrame(数据框)，高效的处理大数据集的切片等功能
提供优化库功能读写多种文件格式，如：CSV、HDF5
Python中的数组：
列表和元组可以表示数组，但是列表保存的是数据的指针，每个数据都有一个指针，计算量大
array：提供append、read、insert等方法但是不支持多维数组
ndarry：Numpy中的基本数据结构，所有元素都是同一种类型，别名array，利于节省内存和提高CPU利用率
维度称为轴，轴的个数称为秩
'''
# numpy
'''基本属性：
ndarray.ndim(秩)，ndarray.shape(维度)，ndarray.size(元素总个数)
ndarray.dtype(元素类型)，ndarray.itemsize(元素字节大小)
'''
import numpy as np
# aArray=np.array([1,2,3])
# barray=np.array([(1,2,3),(4,5,6)])# shape为(2,3),ndim(秩)为2
# carray=np.arange(1,5,0.5)#arange范围可以为浮点数，range为整数，range(上限，下限，间隔)
# darray=np.random.random((2,2))#2行2列的数组，范围为0-1
# earray=np.linspace(1,2,10,endpoint=False)#从起始点到终止点创建一个等差数组,(起始点，终止点，个数，不包括终止点)
# farray=np.ones([2,3])
# harray=np.zeros([2,3])
# iarray=np.fromfunction(lambda i,j:(i+1)*(j+1),(9,9))#从一个函数来创建某一个维度的数组，生成九九乘法表
# a=np.arange(1,5,dtype=np.float64)
# b=np.power(a,2).sum()
# c=np.add(a,np.arange(4))
# print(b)
# ndarray操作
aArray=np.array([(1,2,3),(4,5,6)])
# print(aArray[1])#输出第1行，[4,5,6]
# print(aArray[0:2])# 选择0-2行不包括2，也就是1行和2行
# print(aArray[:,[0,2]])#冒号表示行，[0,1]表示列
# print(aArray[1,[0,1]])#选择第2行，第1和第2列
# for row in aArray:#遍历数组
#     print(row)
# 创建3*3维数据按要求选择需要的数据
x=np.array([(1,2,3),(4,5,6),(7,8,9)])
# print(x)
# 选择第1行
# print(x[0])
# 选择第1和第3行
# print(x[:,[0,2]])
# 选择第1行和第3行，加上步长就可以
# print(x[::2])
#选择第1列和第3列
# print(x[:,::2])#行和列都不考虑选择步长为2就可以
# print(x[::-1])#交换行
# 交换列
# print(x[:,::-1])
#改变维度
y=np.array([(1,2,3),(4,5,6)])
# print(x.reshape(1,9),x)#不改变原有数组
# x.resize(3,2)#重置原有数组
# print(x)
# 创建一个范围为1-16的4*4维数组
# array=np.arange(1,17).reshape(4,4)
# # print(array)
# reshape_array=array.reshape(2,-1)#指定2后会自动计算另一维度值
# print(reshape_array)
# 拼接
# bArray=np.array([1,3,7])
# cArray=np.array([3,5,8])
# c1Array=np.array([(3,5,8),(1,2,3)])
# v=np.vstack((bArray,cArray))#垂直拼接
# h=np.hstack((bArray,cArray))#水平拼接
# # print(v,h)
# # ndarray的运算
# dArray=bArray*cArray
# bArray+=cArray #[ 4  8 15]
# eArray=cArray+c1Array# 使用了numpy的广播功能[[ 6 10 16][ 4  7 11]]
# print(eArray)
aArray=np.array([(1,2,3),(4,5,6)])
add=aArray.sum()
print(add) # 输出21
add1=aArray.sum(axis=0)# 按列求和
add2=aArray.sum(axis=1)# 按行求和
min=aArray.min()#最小值
max=aArray.argmax()#返回最大值的索引
ave=aArray.mean()#平均值
aArray.var()# 方差
aArray.std() # 标准差
result=np.dot(x,x)# 计算矩阵的内积
# Numpy中有linalg模块,它可以被认为是Scipy的子集
'''result1=np.linalg.det(x)# 行列式
result2=np.linalg.inv(x)# 逆矩阵
np.linalg.solve(x)# 多元一次方程求根
np.linalg.eig(x)#求特征值和特征向量'''
# 计算sin(t)的运行时间比较,numpy的通用函数运行时间较短，所以在数据量较大时采用numpy更合适
# import time
# import math
# import numpy as np
# x=np.arange(0,100,0.01)
# t_m1=time.process_time()
# for i,t in enumerate(x):
#     x[i]=math.pow((math.sin(t)),2)
# t_m2=time.process_time()
# y=np.arange(0,100,0.01)
# t_n1=time.process_time()
# y=np.power(np.sin(y),2)
# t_n2=time.process_time()
# print('Running time of math:',t_m2-t_m1)
# print('Running time of numpy:',t_n2-t_n1)























































































