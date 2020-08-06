import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# ************************ 实现一元逻辑回归 ************************
'''
x=np.array([1.,2.,3.,4.])
w=tf.Variable(1.)
b=tf.Variable(1.)
1/(1+tf.exp(-(w*x+b)))# sigmoid 函数： 1/(1+e(-w*x+b))
y=np.array([0,0,1,1])
pred=np.array([0.1,0.2,0.8,0.49])
-tf.reduce_sum(y*tf.math.log(pred)+(1-y)*tf.math.log(1-pred))# 交叉熵损失函数,数学公式转换为代码形式'''
#***************准确率判断*********************
'''y=np.array([0,0,1,1])
pred=np.array([0.1,0.2,0.8,0.49])
tf.round(pred)#  四舍五入,当pred值为0.5的时候round(pred) 为0
tf.equal(pred,y)# 判断预测值与真实值是不是相等
tf.cast(tf.equal(tf.round(pred),y),tf.int8) # tf.cast() 作用是执行tensorflow中张量数据类型转换
print(tf.cast(tf.equal(tf.round(pred),y),tf.int8) )
tf.reduce_mean(tf.cast(tf.equal(tf.round(pred),y),tf.float32))
print(tf.reduce_mean(tf.cast(tf.equal(tf.round(pred),y),tf.float32)))# 求平均准确率'''
#**************tf.where(condition,a,b)*******************
# 根据condition判定返回, condition是True，选择x；condition是False，选择y。
'''pred=np.array([0.1,0.2,0.8,0.49])
print(tf.where(pred<0.5,0,1))# 直接可以输出one-hot 形式'''


'''pred=np.array([0.1,0.2,0.8,0.49])
a=np.array([1,2,3,4])
b=np.array([10,20,30,40])
result=tf.where(pred<0.5,a,b)#a,b值不为空,条件为真替换a条件为假替换b
print(result)
result1=tf.where(pred>=0.5)# 如果a、b均为空，那么返回condition中值为True的位置的Tensor：
print(result1)
# 计算准确率
y=np.array([0,0,1,1])
result2=tf.reduce_mean(tf.cast(tf.equal(tf.where(pred<0.5,0,1),y),tf.float32))
print(result2)'''

#*******************实践***********************
x=np.array(  [137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 106, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26,
     86.21])
y=np.array([1,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0])

plt.subplot(2,1,1)
plt.scatter(x,y)


x_train=x-np.mean(x)
y_train=y

plt.subplot(2,1,2)
plt.scatter(x_train,y_train)
plt.show()

# 设置超参数
learn_rate=0.005
iter=5

display_step=1

# 设置模型初始变量
np.random.seed(612)
w=tf.Variable(np.random.randn())
b=tf.Variable(np.random.randn())

# 训练模型

cross_train=[]
acc_train=[]
for i in range(0,iter+1):
    with tf.GradientTape() as tape:
        pred_train=1/(1+tf.exp(-(w*x_train+b)))
        loss_train=-tf.reduce_mean(y_train*tf.math.log(pred_train)+(1-y_train)*tf.math.log(1-pred_train))
        Accuracy_train=tf.reduce_mean(tf.cast(tf.equal(tf.where(pred_train<0.5,0,1),y_train),tf.float32))
    cross_train.append(loss_train)
    acc_train.append(Accuracy_train)
    dl_dw,dl_db=tape.gradient(loss_train,[w,b])

    w.assign_sub(learn_rate*dl_dw)
    b.assign_sub(learn_rate*dl_db)

    if i % display_step==0:
        print('i:%i,Train loss:%f,Accuracy:%f'%(i,loss_train,Accuracy_train))
