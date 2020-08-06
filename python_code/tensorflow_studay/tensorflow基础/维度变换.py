import numpy as np
import tensorflow as tf
# ***************改变维度*****************
'''tf.constant(np.arange(24).reshape(2,3,4))
a=[[2,3],[3,4],[1,2],[6,7]]
b=tf.reshape(a,[4,-1])#将a转换为4*某个数的维度，但是a的维度必须能被4整除，4为新数据的行数，列数会自己计算出来
print(b)'''
#*******************增加删除维度tf.expand_dims(input,axis)*******************
#*******************增加删除维度 只是改变了张量的视图，并没有改变存储顺序*******************

'''a1=tf.constant([1,2])
b1=tf.expand_dims(a1,1)#在axis=1的轴上增加维度,增加的这个维度上长度为1
print(a1)
print(b1)'''
#  在axis=0的轴上增加维度
'''c2=tf.expand_dims(a1,0)# 轴可以为负数，表示从后向前索引
print(c2)'''
# 分别在0，1，2，3维上，增加维度,z增加的维度长度都是1
'''a4=tf.range(24)
b4=tf.reshape(a4,[2,3,4])
c41=tf.expand_dims(b4,0)
c42=tf.expand_dims(b4,1)
c43=tf.expand_dims(b4,2)
c44=tf.expand_dims(b4,3)
print(c41.shape)
print(c42.shape)
print(c43.shape)
print(c44.shape)'''
#***************删除维度，只能珊瑚长度为1的维度 tf.squeeze(input,axis=None)********************
# eg:shape(1,2,1,3,1) -----  tf.shape(tf.squeeze(t,[2,4]))# 删除长度为1的维度，只是改变了张良的视图，不会改变张量的存储
# ********************交换维度 *****************
'''x=tf.constant([[1,2,3],[4,5,6]])# shape=(2,3)
tf.transpose(x)# 对二维张量交换维度，就是矩阵的转置
#********************* 调整各轴的顺序，不仅改变张量的视图，也改变张量的存储 ***********************
tf.transpose(x,perm=[1,0])#交换索引为0，1的维度,# shape=(3,2);tf.transpose(x,perm=[1,0,2]) 最后已维不变，前两维交换'''
# ******************** 维度变换，拼接和分割 ,改变张量视图，存储顺序不变*****************
# tf.concat(tensors,axis)axis=0,在0轴上拼接
# 分割张量：tf.split( x,2,0) # 在0轴上分割，平均分为2份
# 分割张量：tf.split( x,[1:2:1],0) # 在0轴上分割，可以不均等分割,分割为3个张量，长度分别是1，2，1
# ******************** 维度变换，堆叠和分解 *****************
# (1) 堆叠
x=tf.constant([1,2,3])
y=tf.constant([4,5,6])
z=tf.stack((x,y),axis=0)#在axis=0 轴上堆叠
z1=tf.stack((x,y),axis=1)#在axis=1 轴上堆叠
print(z1)
# (2) 分解
x1=tf.unstack(z,axis=0)
print(x1)
