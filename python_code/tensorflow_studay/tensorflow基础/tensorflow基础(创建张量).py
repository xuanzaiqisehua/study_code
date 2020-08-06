import tensorflow as tf
import numpy as np
# ****************创建张量**********************
#(1) python 列表
'''a=tf.constant([[1,2],[3,4]])
# print(a)
#(2) 张量.numpy()方法
b1=a.numpy()# 通过.numpy()得到对应数组
# print(b1)
#(3) 参数为常数，类型：tf.int8/int16/int32/int64, tf.uint8(无符号位整数),
c=tf.constant(1.0)# tensorflow创建的浮点数，默认是32位
# 创建张量指定数据类型
d=tf.constant(1.0,dtype=tf.float64)
#(4)参数为numpy数组
tf.constant(np.array([1,2]))# numpy创建的数组默认int为32位，float为64位
tf.constant(np.array([1,2]),dtype=tf.float32)# 可以在创建的时候指定数据类型
# (5) 改变张量中的元素数据类型
a1=tf.constant(np.array([1,2]))
b1=tf.cast(a,dtype=tf.float32)
#(6) 参数为布尔型
a3=tf.constant([True,False])
b3=tf.cast(a3,tf.int32)
#(7) 参数为字符串
a4=tf.constant('hello')# b表示字符串b'hello'
# (8) (数组/列表/数字/布尔型/字符串)转换为tensor类型
na=np.arange(12).reshape(3,4)
ta=tf.convert_to_tensor(na)# 数组转换为tensor类型
#(9) 判断是不是张量类型
flag=tf.is_tensor(ta)
# print(flag)
#(10) 创建全0或全1张量
tf.zeros((3,4))# 可以用圆括号
tf.ones(shape=(2,1))
tf.ones([2,3])# 也可以用方括号
tf.fill([2,3],9)# 参数为shape和要填充的数字
#(11) 创建元素值都相同的张量----tf.constant()函数
tf.constant(value=9,shape=[2,3])
# 创建随机张量----正态分布
#(1) 创建 2*2 的张量，其元素服从标准正态分布
tf.random.normal([2,2])
#(2) 创建一个三维张量，其元素服从正态分布
tf.random.normal([3,3,3],mean=0.0,stddev=2.0)
#(3)创建随机张量----截断正态分布
# eg:当均值为0标准差为1时
# tf.random.truncated_normal()#使用这个函数不可能出现[-2,2]以外的点
# tf.random.random_normal()# 可能出现[-2,2]以外的点
# 创建随即张量----截断正态分布
a5=tf.random.truncated_normal([3,3,3],mean=0.0,stddev=2.0)
print(a5)'''
# ***************设置随机种子,可以产生同样的随即张量*************
tf.random.set_seed(8)
tf.random.normal([2,2])
#***************创建均匀分布张量 tf.random.uniform() 函数*****************
tf.random.uniform(shape=(3,3),minval=0,maxval=10,dtype='int32')# minval=0,最小值，maxval=10 最大值
# *************随机打乱 tf.random.shuffle() 函数************
x=tf.constant([[1,2],[3,4],[5,6]])
tf.random.shuffle(x)# 参数可以为列表，数组张量

#*************张量既可以用到CPU也可以用到GPU，但是数组只能用到CPU