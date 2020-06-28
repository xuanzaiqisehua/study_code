'''数据探索能够帮助我们更好的理解数据并帮助做出明智的决策：两个任务（1）检查数据错误（2）了解数据分布特征和内在规律
（1）检查数据错误主要是查看原始数据中是否有脏数据(缺失值，异常值，不一致数据：int和float更新表格的时候产生错误)
'''
# -*- coding: UTF-8 -*-
# coding=utf-8
from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import scipy
iris=datasets.load_iris()
iris_df=pd.DataFrame(iris.data)
iris_df.colums=iris.feature_names #iris.data仅仅拿到了数据，没有标签，这条语句加上标签
iris_df['target']=iris.target
iris_df.target.astype(float)# 将target数据类型（int）转换为float'''
'''基本数据特征分析方法，主要学习三种分析方法：
（1）分布分析：包括定量数据分析（了解数据的分布像是否对称：通过属性-频率对的直方图来观察）
和定性数据分析（主要关注其分类的分布：常用饼图观察）
（2）统计量分析：包括集中趋势分析（讨论数据集中或者平均所处的位置，所以最常使用就是均值和中位数）
和离中趋势分析（讨论数据的离散或分散程度：最小值、最大值、标准差：越小越接近均值、四分位距：值越大变异程度大）
（3）相关分析'''
# 使用iris的第0列属性值进行分析
# plt.hist(iris_df.iloc[:,0],30,color='c')# 将150行数据等分为390份
# plt.show()
# 检验是不是正态分布,axis=0表示在数据的每一列进行检验
#如果P值大于0.05说明数据满足正态分布，小于0.05说明不满足正态分布
# scipy.stats.normaltest(iris_df.iloc[:,0],axis=0)
# 定性数据分析：
# 假设不知道iris属性被平均分成三份，从数据上观察
# iris_df.target.value_counts() # 得到数据类别0,1,2各有五十个说明平均分配
# 绘制饼更加直观的分析
'''iris_df.target.value_counts().plot(kind='pie')
iris_df.iloc[:,0].mean()# 平均值
iris_df.iloc[:,0].median()#中位数
iris_df.iloc[:,0].std()# 方差
iris_df.iloc[:,0].quantile() # 求分位数，默认求中位数，参数为0.5
iris_df.iloc[:,0].quantile([0.25,0.75]) # 求分位数，参数为0.25和0.75上下分位数
iris_df.iloc[:,0].quantile([0.75]).loc[0.75]-iris_df.iloc[:,0].quantile([0.25]).loc[0.25]
# 使用loc函数取出下标为0.75的数与0.25数相减得到四分位距
iris_df.iloc[:,0].describe()#使用describe方法能够分别求出mean、max、min、四分位数
juli=iris_df.iloc[:,0].describe()['75%']-iris_df.iloc[:,0].describe()['25%']# 计算得到四分位距
print(juli)'''
'''如果要分析连续变量之间的线性相关强度，可以用相关分析来表示，散点图是最直观的表示数据相关性的形式
散点图常见方式：单个图、散点图矩阵（观察目标属性和其他属性之间的关系）、相关系数分析（判断两个连续变量之间的相
关关系更加精确），如果两个变量独立且符号正态分布一般使用皮尔逊相关系数（r>0相关，r<0不相关，绝对值r=0不相关，绝对值r=1完全相关，如果0<r<1时根据数字判断，一般大于0.5相关，大于0.8显著相关，小于0.3基本不相关，
（0.3,0.5）比较相关），如果不服从使用斯皮尔曼相关系数，另外肯德尔也比较常用
'''
#查看鸢尾花花瓣长度和花萼长度的相关性，获取数据的第0个和第2个属性，绘制散点图
'''x=[item[0] for item in iris.data]
y=[item[2] for item in iris.data]
plt.scatter(x[:50],y[:50],color='red',marker='_')
plt.scatter(x[50:100],y[50:100],color='green',marker='*')
plt.scatter(x[100:],y[100:],color='blue',marker='D')
plt.legend(loc='best')# 图例位置自动选择最合适的位置
plt.show()'''
# 计算相关性用corr()函数，参数为method默认为皮尔逊相关系数
# result=iris_df.iloc[:,[0,1,4]].corr()#查看属性0,1,4 属性之间的关系的相关性
# 计算target 和第0个属性之间的相关性
# result1=iris_df['target'].corr(iris_df.iloc[:,0])
# print(result1)
# 绘制热力图
# import seaborn as sns
# sns.heatmap(iris_df.iloc[:,[0,1,4]].corr(),annot=True,fmat='.1f',cmap='rainbow')#cmap:colormat:色图，故意输错ranbow可以查看所有的色图

'''基于pandas的数据统计与分析'''
dic_data={'name':['Wangdachui','Liuxin','Niulan','Liubao'],'grade':[3000,3500,2500,4000]}
df_data=pd.DataFrame(dic_data)
# print(df_data)
# print(df_data[df_data.grade>=3000]['name'])
# print(df_data[df_data['grade']>3000].name)
# print(df_data[(df_data.grade>3500)|(df_data.grade<3000)].name)# 选择成绩大于3500或者小于3000 的学生名字
# print(df_data[(df_data.grade>=3000)&(df_data.grade<4000)])# 选择成绩大于3000小于4000的学生信息
import numpy as np
# cha=np.diff(df_data.grade)# np.diff计算相邻两个对象之间的差值
# print(cha)
# print(np.sign(cha))# 取正负号
# print(np.sign(df_data.grade))
status=np.sign(np.diff(df_data.grade))
# print(len(status[status==1]))
## 函数那么多，如何知道应该使用哪个函数，多去查看官方手册，多使用dir和help函数
## 值排序，df_data.sort_values(by='grade',ascending=False(逆序)),索引排序df_data.sort_index()
# temp_data=df_data.sort_values(by='grade',ascending=False)# 将成绩逆序排序
# print(temp_data,temp_data[:2].name)# 切片后选择名字
# print(temp_data.sort_index())data=pd.read_csv('AXP.csv',index_col='Date')
data=pd.read_csv('AXP.csv',index_col='Date')
axp_data=pd.DataFrame(data)
axp_data.fillna(axp_data.mean(),inplace=True)
'''month=[item[5:7] for item in axp_data.index]
# 使用group_by 对月份进行分组
print(axp_data.groupby(month).groups)
print(axp_data.groupby(month).Open.count())# 计算这个月的开盘数
month=[item[5:7] for item in axp_data.index]# 与上面的方法相似
print(axp_data.groupby(month).apply(len))'''
# for k,value in axp_data.groupby(month):
#     print(k)
#     print(value)
# print(axp_data.apply(max))# 计算最大值
import numpy as np
# print(axp_data.loc[:,['Close','Open']].apply(np.int32))#转换类型
# print(axp_data.loc[:,['Close','Open']].applymap(int))#applymap作用在每一个元素上
# 把美国运通公司2019年9月1日至9月5日间的股票交易信息追加到2019年6月最后2天的股票
'''p=axp_data['2019-06-01':'2019-06-30'][-2:]
q=axp_data['2019-09-01':'2019-09-05']
p1=p.append(q)
print(p1)'''
# 把美国运通公司2019年9月股票数据中的前3个和后3个合并
tempdf=axp_data[(axp_data.index>='2019-09-01')&(axp_data.index<='2019-09-30')]# 选出2019年9月的数据
price=[tempdf[:3],tempdf[-3:]]
print(pd.concat(price))
#concat(ignore_index=True)的时候可以将两个属性不一致的数据连接到一起，比如一个为10个属性，另一个为8个属性
# pd.merge(a.drop(['price'],axis=1),b,on='code')#merge函数与数据库中join功能类似，将两张表join到一起，两张表必须有相同的字段








