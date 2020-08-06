import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
'''a=[0,2,3,5]
b=tf.one_hot(a,6)
pred=np.array([[0.1,0.2,0.7],[0.1,0.7,0.2],[0.3,0.4,0.3]]) #设置预测值
y=np.array([2,1,0]) #标记
y_onehot=np.array([[0,0,1],  # 标记独热编码
                   [0,1,0],
                   [1,0,0]])

# 取出预测值中的最大值得索引
tf.argmax(pred,axis=1)

# 判断预测值和真实值是不是相同
tf.equal(tf.argmax(pred,axis=1),y)

# 将布尔值转化为数字
tf.cast(tf.equal(tf.argmax(pred,axis=1),y),tf.float32)

# 求平均准确率
tf.reduce_mean(tf.cast(tf.equal(tf.argmax(pred,axis=1),y),tf.float32))

# 交叉熵损失函数
y_onehot*tf.math.log(pred)

# 所有样本交叉熵之和
-tf.reduce_sum(y_onehot*tf.math.log(pred))

# 平均交叉熵损失
-tf.reduce_sum(y_onehot*tf.math.log(pred))/len(pred)'''

#**************************** 鸢尾花数据多酚类 ********************************

#(1) 准备数据
TRAIN_URL='http://download.tensorflow.org/data/iris_training.csv'
train_path=tf.keras.utils.get_file(TRAIN_URL.split('/')[-1],TRAIN_URL)
df_iris_train=pd.read_csv(train_path,header=0)
iris_train=np.array(df_iris_train)
x_train=iris_train[:,2:4]# 提取花瓣长度、花瓣宽度属性
y_train=iris_train[:,4]
num_train=len(x_train)# 训练数据长度为120
x0_train=np.ones(num_train).reshape(-1,1)#将训练数据重置为全为1的120*1的数组
X_train=tf.cast(tf.concat([x0_train,x_train],axis=1),tf.float32)
Y_train=tf.one_hot(tf.constant(y_train,dtype=tf.int32),3) # y_train 为数组，将其转换为tensor常数类型,然后将其转换为one_hot类型

#(2) 设置超参数，设置模型初始化参数
learn_rate=0.2
iter=500
display_step=100

np.random.seed(612)
w=tf.Variable(np.random.randn(3,3),dtype=tf.float32)

#(3) 训练模型
acc=[]
cce=[]

for i in range(0,iter+1):
    with tf.GradientTape() as tape:
        PRED_train=tf.nn.softmax(tf.matmul(X_train,w))# matmul对应位置元素相乘
        loss_train=-tf.reduce_sum(Y_train*tf.math.log(PRED_train))/num_train
    accuracy=tf.reduce_mean(tf.cast(tf.equal(tf.argmax(PRED_train.numpy(),axis=1),y_train),tf.float32))
    acc.append(accuracy)
    cce.append(loss_train)

    dl_dw=tape.gradient(loss_train,w)
    w.assign_sub(learn_rate*dl_dw) # 权值w不断变化

    if i % display_step==0:
        print('i:{},Acc:{},loss:{}'.format(i,accuracy,loss_train))

# 可视化
'''plt.subplot(1,2,1)
plt.plot(cce)
plt.subplot(1,2,2)
plt.plot(acc)
plt.show()'''
# PRED_train 得到属于每种类别的概率
# tf.resuce_sum(PRED_train,axis=1) #概率之和为1

tf.argmax(PRED_train.numpy(),axis=1)# 转换为自然顺序码

# 绘制分类图
M=500

x1_min,x2_min=x_train.min(axis=0)
x1_man,x2_max=x_train.max(axis=0)
t1=np.linspace(x1_min,x1_min,M) # 产生从start到stop的等差数列
t2=np.linspace(x2_min,x2_max,M)
m1,m2=np.meshgrid(t1,t2)


m0=np.ones(M*M)
X_=tf.cast(np.stack((m0,m1.reshape(-1),m2.reshape(-1)),axis=1),tf.float32)
y_=tf.nn.softmax(tf.matmul(X_,w))

y_=tf.argmax(y_.numpy(),axis=1)# 转换为自然顺序码，决定网格颜色
n=tf.reshape(y_,m1.shape)

plt.figure(figsize=(8,6))
cm_bg=mpl.colors.ListedColormap(['#A0FFA0','#FFA0A0','#A0A0FF'])
plt.pcolormesh(m1,m2,n,cmap=cm_bg)
plt.scatter(x_train[:,0],x_train[:,1],c=y_train,cmap='brg')
plt.show()
