import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
'''boston_hosing=tf.keras.datasets.boston_housing# 加载波士顿房价数据集
(train_x,train_y),(test_x,test_y)=boston_hosing.load_data()
# print(train_x.shape,train_y.shape)

# 数据处理
x_train=train_x[:,5]
y_train=train_y


x_test=test_x[:,5]
y_test=test_y

# 设置超参数
learn_rate=0.04
iter=2000
display_step=200

# 设置模型参数初始值
np.random.seed(612)
w=tf.Variable(np.random.randn())
b=tf.Variable(np.random.randn())


# 训练模型
mse_train=[]
mse_test=[]

for i in range(0,iter+1):
    with tf.GradientTape() as tape:
        pred_train=w*x_train+b# 求偏导的函数
        loss_train=0.5*tf.reduce_mean(tf.square(y_train-pred_train))# 损失函数公式

        pred_test = w * x_test + b  # 求偏导的函数
        loss_test = 0.5 * tf.reduce_mean(tf.square(y_test - pred_test))  # 损失函数公式
    mse_train.append(loss_train)
    mse_test.append(loss_test)

    dl_dw,dl_db=tape.gradient(loss_train,[w,b])
    # 更新权值, w=w-learn_rate*dl_dw
    w.assign_sub(learn_rate*dl_dw) # tf.assign_sub(ref, value, use_locking=None, name=None) 释义：变量 ref 减去 value值，即 ref = ref - value
    b.assign_sub(learn_rate*dl_db)
    if i % display_step==0:
        print('i:%i,Train Loss: %f,Test Loss:%f'%(i,loss_train,loss_test))

    # 可视化
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置显示字体
    plt.subplot(1,2,1)
    plt.plot(mse_train)
    plt.subplot(1,2,2)
    plt.plot(mse_test)
plt.show()'''


# 多元线性回归
# 一维数组归一化

area=np.array(  [137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 106, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26,
     86.21])
room=np.array([3,2,2,3,1,2,3,2,2,3,1,1,1,1,2,2])
print(area.shape)

# 归一化，将数值全部统一为[0,1]范围内，房屋面积和房间数不是同一量级的数，归一化后可以归为同一量级
x1=(area-area.min())/area.max()-area.min()
x2=(room-room.min())/(room.max()-room.min())

# 二维数组归一化----循环实现
'''x=np.array([[3.0,10,500],
            [2.,20,200],
            [1.,30,300],
            [5.,50,100]])
for i in range(x.shape[1]):# x.shape()为列，每一列为一种属性值
    x[:,i]=(x[:,i]-x[:,i].min())/(x[:,i].max()-x[:,i].min())
print(x)'''

#  ********************* 广播运算 **************
x=np.array([[3.0,10,500],
            [2.,20,200],
            [1.,30,300],
            [5.,50,100]])
# print(x.min(axis=0))# 求每一列的最小值
# print(x.max(axis=0))# 求每一列的最大值
diff=x.max(axis=0)-x.min(axis=0)
# print(diff)
(x-x.min(axis=0))/(x.max(axis=0)-x.min(axis=0))