# Matplotlib 是Python的绘图基础，绘图API-pyplot，与matlab类似将一些复杂的绘图隐藏在pyplot中，用的时候对其进行调用
# -*- coding : utf-8 -*-
# -*- coding: ascii -*-
import numpy as np
import matplotlib.pyplot as plt
# plt.plot([3,4,7,6,2,8,9])# y轴的数据，x轴数据默认为1-7
# plt.show()
# plt.savefig('1')#保存图片,写上路径1.jpg,默认为png
# Numpy数组也可以作为Matplotlib的参数，进行多组成对数据绘图
# plot为折线图，scatter为散点图，bar为条形图
# import numpy as np
# import matplotlib.pyplot as plt
# t=np.arange(0,4,0.1)
# plt.plot(t,t,t,t+2,t,t**2)# 两两一对
# plt.show()
# plt.scatter(range(7),[3,4,7,6,2,8,9])
# plt.bar(range(7),[3,4,7,6,2,8,9])
# plt.show()
# help(plt.plot)#查看plot的帮助信心，查看图形的颜色，线条等
'''其他属性
'''
'''import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(8,6),dpi=100)# 图片大小和像素精度
plt.title('Plot Example')#图标题
plt.xlabel('X lable')
plt.ylabel('Y lable')
t=np.arange(0,4,0.1)
plt.plot(t,t,color='red',linestyle='-',linewidth=3,label='line1')# 颜色，线型、线宽，标签
plt.plot(t,t+2,color='green',linestyle='',marker='*',linewidth=8,label='line2')# 颜色，线型、线宽，标签
plt.plot(t,t**2,color='blue',linestyle='',marker='+',linewidth=3,label='line3')# 颜色，线型、线宽，标签
plt.show()
plt.legend(loc='upper left')#图例在图的左上方'''
# 小例子
'''x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
plt.title('测试')
plt.xlabel('X label')
plt.ylabel('Y label')
plt.plot(x, y,'r--')
plt.show()'''
# 绘制子图plt.subplot(行列区域)，plt.subplot(121)表示在第一行第二列第一个区域
'''x=np.linspace(-np.pi,np.pi,300)#等间隔产生数据，参数(上限，下限，间隔)
plt.figure(1)
plt.subplot(211)
plt.plot(x,np.sin(x),color='r')
plt.subplot(212)
plt.plot(x,np.cos(x),color='g')
plt.show()'''
#除了上述subplot方法subplots也很常用
'''x=np.linspace(-np.pi,np.pi,300)
fig,(ax0,ax1)=plt.subplots(2,1)#两行一列，subplots函数返回两个值，一个是对象本身，一个是子图对象
ax0.plot(x,np.sin(x),color='r')#可以直接使用子图对象进行参数设置
ax0.set_title('subplot1')
plt.subplots_adjust(hspace=0.5)#hspace垂直间隔,wspace水平间隔
ax1.plot(x,np.cos(x),color='g')
ax1.set_title('subplot2')
plt.show()'''
# 用axes确定子图区域
'''x=np.linspace(-np.pi,np.pi,300)#等间隔产生数据，参数(上限，下限，间隔)
plt.axes([.1,.1,0.8,0.8])#参数为：距离左边和底边距，这张图的高度和宽度，范围都是0-1，是相对距离
plt.plot(x,np.sin(x),color='r')
plt.axes([.3,.15,0.4,0.3])
plt.plot(x,np.cos(x),color='g')
plt.show()'''
# pandas绘图，整合Matplotlib功能可以实现基于series和DataFrame的某些绘图功能
import pandas as pd
data=pd.read_excel('data.xlsx')
'''ax=data.loc[0:2,'Python'].plot()#  等于ax=data.iloc[0:2,1].plot()
plt.show()
bx=data.loc[0:2,['Python','Math']].plot()# 等于bx=data.iloc[0:2,[1,2]].plot()
plt.show()'''
#设置参数:bar（条形） pie(饼图)
'''ax=data.plot(kind='bar',x='code',y='price',color='g')
ax.set(ylabel='Price',title="Stock Statistics of DJI")
plt.show()'''











