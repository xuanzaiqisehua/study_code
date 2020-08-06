# 注意，只要数据能够被描述为凸函数就可以使用梯度下降法求最优解
'''
共5步：
（1）加载样本数据
（2）设置超参数、迭代次数
（3）设置模型参数初值，初值可以为任意
（4）训练模型，使用模型公式迭代训练次数
（5）结果可视化
'''
import tensorflow
import numpy as np
import matplotlib.pyplot as plt

# （1）加载数据
x = np.array(
    [137.97, 104.50, 100.00, 124.32, 79.20, 99.00, 124.00, 114.00, 106, 69, 138.05, 53.75, 46.91, 68.00, 63.02, 81.26,
     86.21])
y = np.array(
    [145.00, 110.00, 93.00, 116.00, 65.32, 104.00, 118.00, 91.00, 62.00, 133.00, 51.00, 45.00, 78.50, 69.65, 75.69,
     95.30, 98])
# （2）设置超参数
learn_rate = 0.00001
iter = 200
# display_step不属于超参数，设置得数值完全不会对模型训练产生影响，设置每多少次显示一次
display_step = 10
# （3）设置模型参数初值
np.random.seed(612)  # 设置随机种子，每次生成的我，w,b都相同
w = np.random.randn()
b = np.random.randn()
# （4）训练模型
mse = []
for i in range(0, iter + 1):  # 迭代101次
    # 计算损失函数对w和b得偏导数
    dL_dw = np.mean(x * (w * x + b - y))
    dL_db = np.mean(w * x + b - y)
    # 使用迭代公式更新w和b
    w = w - learn_rate * dL_dw  # 迭代方向
    b = b - learn_rate * dL_db
    # 以上实现了梯度下降法的一次迭代

    # 为了观察每次迭代的结果，判断什么时候收敛，所以通过使用每次迭代后的w和b计算损失并将其存在mse中显示出来
    pred = w * x + b
    Loss = np.mean(np.square(y - pred)) / 2
    mse.append(Loss)

    # 每10次迭代显示一次结果
    if i % display_step == 0:
        print('i:{},Loss:{},w:{},b:{}'.format(i, mse[i], w, b))
#可视化结果
'''plt.rcParams['font.sans-serif']=['SimHei']#设置显示字体
plt.figure()
plt.scatter(x,y,color='red',label='销售记录')#绘制 x,y散点图
plt.scatter(x,pred,color='blue',label='梯度下降法')
plt.plot(x,pred,color='blue')#绘制直线

plt.xlabel('Area',fontsize=14)
plt.ylabel('Price',fontsize=14)

plt.legend(loc='upper left')#图例放在左上方
plt.show()'''

#绘制损失函数(1)
'''plt.figure()
plt.plot(mse)

plt.xlabel('Iteration',fontsize=14)
plt.ylabel('Loss',fontsize=14)

plt.show()'''

print(w,b)
#绘制损失函数(2)
plt.figure()
plt.plot(range(20,100),mse[20:100])

plt.xlabel('Iteration',fontsize=14)
plt.ylabel('Loss',fontsize=14)

plt.show()


