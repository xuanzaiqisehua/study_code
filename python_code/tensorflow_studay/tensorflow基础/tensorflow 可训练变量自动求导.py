# 创建可训练变量
import tensorflow as tf
import numpy as np
'''x=tf.constant(3)# print(isinstance(x,tf.Tensor))#判断是不是tensor类
y=5
print(isinstance(y,int))#判断是不是int类型'''
# Tensorflow 的自动求导机制---GradientType
'''
用法：
with GradientType() as tape:
   函数表达式
grad=tape.gradient(函数，自变量)
'''
#*****************一阶导数***********************
'''x=tf.Variable(3.)
with tf.GradientTape() as tape:
    y=tf.square(x)
dt_dx=tape.gradient(y,x)# 求函数y对x的偏导
print(dt_dx)# y=x^2'''
#*****************对含有x变量求多个一阶导数：会报错，只能使用一次，要想多次使用需要设置参数persistent=True***********************
'''x=tf.Variable(3.)
with tf.GradientTape(persistent=True) as tape:
    y=tf.square(x)
    z=pow(x,3)
dy_dx=tape.gradient(y,x)
dz_dx=tape.gradient(z,x)
print(dz_dx)'''
#*****************添加监视变量*****
#加入创建一个常数，后续相对其进行监视
'''x=tf.constant(3.)# 这里好像必须是浮点数？
with tf.GradientTape(watch_accessed_variables=False) as tape:
    tape.watch(x)
    y=tf.square(x)
dy_dx=tape.gradient(y,x)
print(y,dy_dx)'''
#*************多元函数求偏导**************
#加入创建一个常数，后续相对其进行监视
'''x=tf.Variable(3.)
y=tf.Variable(4.)
with tf.GradientTape() as tape:
    f=tf.square(x)+2*tf.square(y)+1
df_dx,df_dy=tape.gradient(f,[x,y])
print(f)
print(df_dx)
print(df_dy)'''
#**************************求二阶导数*************************
# 由于默认情况下求导数，变量只能使用一次，如果想求多阶导数需要设置参数persistent=True
'''x=tf.Variable(3.0)
y=tf.Variable(4.0)
with tf.GradientTape(persistent=True) as tape2:
    with tf.GradientTape(persistent=True) as tape1:
        f=tf.square(x)+2*tf.square(y)+1
    first_grads=tape1.gradient(f,[x,y])
second_grade=[tape2.gradient(first_grads,[x,y])]
print(first_grads)
print(second_grade)'''
#************************** 对向量求偏导  *************************
'''x=tf.Variable([1.,2.,3.])# 变量都为浮点数
y=tf.Variable([4.,5.,6.])
with tf.GradientTape() as tape:
    f=tf.square(x)+2*tf.square(y)+1
df_dx,df_dy=tape.gradient(f,[x,y])# 求f对x和y的偏导数
print(df_dx)
print(df_dy)'''
#************************** tensorflow 实现梯度下降法  *************************
# numpy 实现一元线性回归
import numpy as np
import matplotlib.pyplot as plt
x = np.array(
    [137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 106, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26,
     86.21])
y = np.array(
    [145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00, 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69,
     95.30])
# 设置超参数
learn_rate=0.00001
iter=100
dispaly=10
np.random.seed(612)
w=np.random.randn()
b=np.random.randn()

#实现梯度下降法
mse=[]
for i in range(0,iter+1):
    dl_dw=np.mean(x*(w*x+b-y))
    dl_db=np.mean(w*x+b-y)

    w=w-learn_rate*dl_dw
    b=b-learn_rate*dl_db

    pred=w*x+b
    loss=0.5*np.mean(np.square((y-pred)))
    mse.append(loss)

    # plt.plot(x,pred)

    if i%dispaly==0:
        print('i:%i,loss:%f,w:%f,b:%f'%(i,mse[i],w,b))
plt.plot(mse)
plt.show()