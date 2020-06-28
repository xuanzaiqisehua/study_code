#********************基于pandas的男女电影评分差异分析***********************
import pandas as pd
import numpy as np
unames=['user id','age','gender','occupation','zip code']
users=pd.read_csv('ml-100k/u.user',sep='|',names=unames)
rnames=['user id','item id','rating','timestamp']
ratings=pd.read_csv('ml-100k/u.data',sep='\t',names=rnames)
user_df=users.loc[:,['user id','gender']]
ratings_df=ratings.loc[:,['user id','rating']]
rating_df=pd.merge(user_df,ratings_df)
# print(rating_df)
'''# 对性别分组
# print(rating_df.groupby('gender').rating.std())#
# print(rating_df.groupby('gender').rating.apply(pd.Series.std))#  等同于print(rating_df.groupby('gender').rating.apply(pd.Series.std))#'''
# 对性别分组后计算标准差可看出女生的评分差异较大，换一种思路，对每个用户的评分均值进行分析，首先需要对每个用户和性别进行分组
# print(rating_df.groupby(['user id','gender']).rating.mean())
# print(rating_df.groupby(['user id','gender']).apply(np.mean))
# 也可以使用pandas中的透视表功能
# print(pd.pivot_table(rating_df,values='rating',index='gender',aggfunc=pd.Series.std))
# 均值聚合,默认的聚合函数为均值聚合
# t=pd.pivot_table(rating_df,index=['user id','gender'],values='rating')
# print(t)
# # 寻找性别为女的均值
# female=t.query("gender==['F']")
# print(pd.Series.std(female))
#**************************基于UCI葡萄酒数据集，从数据获取、预处理和探索、机器学习建模、调参及模型评估等较为完整的过程，实现利用机器学习模型实现分类任务
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
# from sklearn.linear_model import GridSearchCV
red_wine=pd.read_csv('winequality-red.csv',sep=';')
# import seaborn as sns
# duplicated判断是否有重复值，如果是返回True
# print(red_wine.duplicated().sum())
red_wine=red_wine.drop_duplicates()#删除重复值
# print(red_wine)
# print(red_wine.describe())# 查看基本统计信息
# print(red_wine.quality.value_counts())# 查看 quality 各个数字的个数
# red_wine.quality.value_counts().plot(kind='pie',autopct='%.2f')
# plt.show()
# 使用皮尔逊系数查看quality与其他属性之间的相关性,皮尔逊相关系数变化从-1到 +1，当r＞0表明两个变量是正相关，即一个变量的值越大，另一个变量的值也会越大；r＜0表明两个变量是负相关，即一个变量的值越大另一个变量的值反而会越小。
# print(red_wine.corr().quality )#alcohol :0.480343;volatile acidity:-0.395214  相关性比较大，一个是正相关、一个是负相关
# 将酒的分类转换为二分类问题
'''from sklearn.preprocessing  import LabelEncoder
bins=(2,4,6,8)
group_names=['low','medium','high']
red_wine['qulity_lb']=pd.cut(red_wine['quality'],bins=bins,labels = group_names) # 将分类重新划分组
lb_quality=LabelEncoder()# 为了对数据进行处理，将label重新编码
red_wine['label']=lb_quality.fit_transform(red_wine['qulity_lb'])
red_wine_copy=red_wine.copy()
red_wine.drop(['quality','quality_lb'],axis=1,inplace=True)# 删除两列
x=red_wine.iloc[:,:-1]
y=red_wine.label
from sklearn.linear_model import train_text_split
x_train,x_test,y_train,y_test=train_text_split()
from sklearn.preprocessing import scale
x_train=scale(x_train)
x_test=scale(x_test)
from sklearn.metrics import confusion_matrix
### 随机森林模型是对原数据进行多次随机采样形成多个不同的数据集，然后基于每个采样集训练一个决策树基学习器，然后将这些基学习器进行结合，最终通过投票或均值等方式使得模型获得较高的精准度和泛华性能
rfc=RandomForestClassifier(n_estimators=200)# 构建随机森林分类器，n_estimators设置为200表示在利用最大投票数或者均值前想要建立的最大子树，比较多的子树能够让模型具有更好的性能，但是代码会变慢
rfc.fit(x_train,y_train)
y_pred=rfc.predict(x_test)# 使用测试集进行预测
print(confusion_matrix(y_test,y_pred))# 混淆举证对真实值和预测值进行判断，混淆矩阵中行的和代表真实值的数量，列表示预测类别
# print(red_wine)'''
#**************现实世界被描绘成完全自治的封装的一些对象，抽象和对象，类：描述某一类对象的特征（数据和操作）对象（实例）：由数据及能对其实施的操作所构成的封装体
'''def zimu(srt):
    count=0
    for item in str:
        if item.isalpha():
         count+=1
    return count
str='i--#hell213$'
result=zimu(str)
print(result)'''
# 找出一个文件夹下的 "6个数字.png"形式的文件，比如 123456.png

'''import os
import re
root = "H:\\ab123"
def findtxt(path, ret):
    """Finding the *.txt file in specify path"""
    filelist = os.listdir(path)
    for filename in filelist:
            pattern = re.compile('[0-9]{6}.png')
            result = pattern.findall(filename)
            if result.endswith(".jpg"):  # Specify to find the txt file.
                ret.append(result)
ret = []
findtxt(root, ret)
for path in ret:
    print(path)'''

'''import re
with open ('pandas_study'):


str='123456.png'
pattern = re.compile('[0-9]{6}.png')
result=pattern.findall(str)
print(result)'''
'''import os
import re
root = "../Python 数据统计与数据挖掘"
def findjpg(path, ret):
    filelist = os.listdir(path)
    for filename in filelist:
     pattern = re.compile('[0-9].jpg')
     result = pattern.findall(filename)
     if result!=[]:
       ret.extend(result)
ret = []
findjpg(root, ret)
print(ret)'''

















