import  tensorflow as tf
import numpy as np
# ************************一维张量切片 ***********************
'''a=tf.constant(np.arange(24))
print(a[1::2])# 取出所有的奇数,a[1::-1]逆序取所有元素
print(a[::-2])# 从最后一个开始逆序取间隔为2元素'''
# ************************二维张量切片：为度之间用逗号隔开 ***********************
# iris[0,:]
# ************************三维张量切片：***********************
#mnist[0,:,:] 第一张图片
# mnist[0:10,:,:] 前十张图片
# mnist[0:20,0:28:2,:] 前20张图片所有行隔行采样
# mnist[,0:28:2,:0:28:2,] 所有图片隔行采样隔列采样
# ************************三维张量切片：彩色图片lena(512,512,3) ***********************
# lena[:,:,0] R通道图片；lena[:,:,2] B通道图片
# ************************四维张量切片：多张彩色图片(4,512,512,3)***********************
# image[0,:,:,0]# 第一张图片的R通道
# image[0:2,:,:,2]# 前2张图片的B通道
# image[0:2,0:512:2,:,2]# 前2张图片的B通道图片隔行采样
# ************************数据提取：根据索引，抽取没有规律的、特定的数据***********************
# a=tf.range(params,indices)#参数为输入张量和索引列表
'''a=tf.range(5)
b=tf.gather(a,indices=[0,2,3])# 提取索引值分别为0，2，3的元素
print(b)'''
# *********** 对多维张量采样 ***********
'''tf.gather(b,axis=0,indices=[0,2,3])#需要指明在哪个维度上进行抽取，每次只能对一个维度上进行采样
# **********  同时对多个点,和多个维度 进行采样 gather_nd()  ***************
tf.gather_nd(b,[[0,0],[1,1],[2,3]])#多个点的坐标'''
# 彩色图像：(512,512,3)tf.gather_nd(lena,[[0,0],[1,1],[2,3]]) #对前两维采样，取得这些点所有通道的值
# 手写数据集tf.gather_nd(minist,[[0],[2],[3]])# t取索引为0，2，3的图片

#*******************张量运算(+/1/*//取模/幂对数运算)*****************
# tf.add(x,y)

#************** 广播机制 ****************
# 一维张量+二/三维张量,两个张量的最后一个维度长度必须相等
# 数字+ N维张量：这个数字广播到张量的各个元素

#***************张量金额numpy数组之间的相互转换**********************
# numpy 转为张量 tf.constant();tf.convert_to_tensor
# 张量转为numpy数组 Tensor.numpy()
# ********当张量和numpy共同参与运算：
# t=tf.multiply(x,36)# 自动将numpy转为张量
# 执行mumpy操作自动将张量转为numpy：np.add(x,t)
# 如果使用运算符操作：a+b：只要数据中有一个数位tensor对象就会把全部操作数转为张量
#********************多维向量乘法************************8
'''# (1)三维张量*二维张量：最后两维做向量乘法，高维采用广播机制，如：(2,3,5)*(5,4)-----(3,5)*(5,4)------(2,3,4)
# (2)三维张量*三维张量：最后两维做向量乘法，高维采用广播机制
a=tf.constant(np.arange(12),shape=(2,2,3))
b=tf.constant(np.arange(12),shape=(2,2,3))
b1=tf.constant(np.arange(12),shape=(2,3,2))
c=tf.multiply(a,b)# 对应位置元素相乘
d=tf.matmul(a,b1)
print(a)
print(b1)
print(d)'''
#******************** 使用GPU ************************
'''import tensorflow as tf
print(tf.__version__)#查看tensorflow版本
# 查看当前主机上的运算设备i
gpu=tf.config.experimental.list_physical_devices(device_type='GPU')
cpu=tf.config.experimental.list_physical_devices(device_type='CPU')
print(gpu)'''
# 使用GPU
'''with tf.device('/cpu:0'):
    cpu_a=tf.random.normal([10000,1000])
    cpu_b= tf.random.normal([1000, 2000])
    cpu_c=tf.matmul(cpu_a,cpu_b)
print('cpu-a',cpu_a.device)
print('cpu-b',cpu_b.device)
print('cpu-c',cpu_c.device)'''
# **************** 在GPU 上是否可用**********************
tf.test.is_gpu_available()
# 指定在GPU上执行随即操作数
'''with tf.device('/cpu:0'):
    gpu_a=tf.random.normal([10000,1000])
    gpu_b= tf.random.normal([1000, 2000])
    gpu_c=tf.matmul(gpu_a,gpu_b)
print('gpu-a',gpu_a.device)
print('gpu-b',gpu_b.device)
print('gpu-c',gpu_c.device)'''
