# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 10:27
# @Author  : Gepenghua
# @FileName: cnn_tensorflow.py
# @Email : 578517264@qq.com
# @Software: PyCharm
# @github    ：https://github.com/xuanzaiqisehua?tab=repositories
#参数含义：参考https://www.jianshu.com/p/208995cf1001
#tensorflow 学习https://github.com/outman123/tensorflow

'''import tensorflow as tf
import numpy as np
x_data=np.float32(np.random.rand(2,100))#返回一个或一组服从“0~1”均匀分布的随机样本值,2*100维
y_data=np.dot([0.100,0.200],x_data)+0.300
# print(x_data)
# print(y_data.shape)
#构造线性模型
b=tf.Variable(tf.zeros[1])
w=tf.Variable(tf.random_uniform_initializer([1,2],-1.0,1.0))#生成标准正态分布的随机数
y=tf.matmul(w,x_data)+b# matmul函数表示w*x_data,tf.multiply表示对应位置元素相乘
#最小化方差
#tf.reduce_mean 函数用于计算张量tensor沿着指定的数轴（tensor的某一维度）上的的平均值
#求平均(y-y_data)^2，使得损失最小
loss=tf.reduce_mean(tf.square(y-y_data))
optimizer=tf.train.GradientDescentOptimizer(0.5)#随机梯度下降优化函数，学习率设为0.5
train=optimizer.minimize(loss)#最小化损失函数
#初始化变量
init=tf.initializer_all_variables()
#启动图
sess=tf.Session()
sess.run(init)'''
import tensorflow as tf
import os
tf.compat.v1.disable_eager_execution()#版本不一致加入这条语句才能执行
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'#忽略不支持编译的警告
'''# import tensorflow.compat.v1 as tf
# 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# 加到默认图中.
#
# 构造器的返回值代表该常量 op 的返回值.
matrix1 = tf.constant([[3., 3.]])

# 创建另外一个常量 op, 产生一个 2x1 矩阵.
matrix2 = tf.constant([[2.],[2.]])

# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果.
product = tf.matmul(matrix1, matrix2)
# 启动默认图.
sess = tf.compat.v1.Session()
# 调用 sess 的 'run()' 方法来执行矩阵乘法 op, 传入 'product' 作为该方法的参数.
# 上面提到, 'product' 代表了矩阵乘法 op 的输出, 传入它是向方法表明, 我们希望取回
# 矩阵乘法 op 的输出.
#
# 整个执行过程是自动化的, 会话负责传递 op 所需的全部输入. op 通常是并发执行的.
#
# 函数调用 'run(product)' 触发了图中三个 op (两个常量 op 和一个矩阵乘法 op) 的执行.
#
# 返回值 'result' 是一个 numpy `ndarray` 对象.
result = sess.run(product)
print (result)
# ==> [[ 12.]]
# 任务完成, 关闭会话.
sess.close()
# 除了显式调用 close 外, 也可以使用 "with" 代码块 来自动完成关闭动作.
with tf.compat.v1.Session() as sess:
  result = sess.run([product])
  print (result)
'''
input1=tf.constant(3.0)
input2=tf.constant(2.0)
input3=tf.constant(5.0)
intermed=tf.add(input2,input3)
mul=tf.multiply(input1,intermed)
with tf.compat.v1.Session() as sess:
  result=sess.run([mul,intermed])
  print(result)























