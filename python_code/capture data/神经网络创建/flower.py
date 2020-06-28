# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 14:39
# @Author  : Gepenghua
# @FileName: mnist.py
# @Email : 578517264@qq.com
# @Software: PyCharm
# @github    ：https://github.com/xuanzaiqisehua?tab=repositories
import tensorflow as tf
from sklearn import datasets
from matplotlib import pyplot as plt
import np
x_data=datasets.load_iris().data()#加载鸢尾花数据
y_data=datasets.load_iris().target()#加载鸢尾花标签
#随机打乱数据，因为原始数据是顺序的，顺序不打乱会影响准确率
#seed：随机种子，是一个整数，当设置之后，每次生成的随机数都一样
np.random.seed(116)
np.random.shuffle(x_data)#shuffle() 方法将序列的所有元素随机排序。
np.random.seed(116)
np.random.shuffle(y_data)
np.random.set_seed(116)
#将打乱的数据集分为训练姐和测试集
x_train=x_data[:-30]
y_train=y_data[:-30]
x_test=x_data[-30:]
y_test=y_data[-30:]
#转换x的数据类型，否则后界句矩阵相乘会因数据类型不一样报错
x_train=tf.cast(x_train,tf.float32)
x_test=tf.cast(x_test,tf.float32)
#from_tensor_slices函数使输入特征和标签一一对应(把数据分批次，每个批次batch组数据)
train_db=tf.data.Dataset.from_tensor_slices((x_train,y_train).batch(32))
test_db=tf.data.Dataset.from_tensor_slices((x_test,y_test).batch(32))
#生成神经网络的参数，4个输入特征，故输入层为4个节点，，因为分为3类，故输出层为3个神经元
#用tf.Variable()标记参数可训练
#使用seed使每次生成的随机数相同
w1=tf.Variable(tf.random.truncated_normal([4,3],stddev=0.1,seed=1))#产生截断正态分布随机数
b1=tf.Variable(tf.random.truncated_normal([3],stddev=0.1,seed=1))
lr=0.1#学习率为0.1
train_loss_results=[]#将每轮的lsoo记录在此列表中，为后续画loss曲线提供数据
test_acc=[]#将每轮的acc记录在此列表中，为后续的acc曲线提供数据
epoch=500#循环500次
loss_all=0#每轮分为4个step，loss_all记录4个step生成的4个loss






















