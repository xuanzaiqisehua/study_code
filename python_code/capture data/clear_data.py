'''from sklearn import datasets
import pandas as pd
import matplotlib.pyplot as plt
import scipy
coffe_list=['32Latte','_Americano30','/34Cappuccino','Mocha35']
def clean_list(lst):
    cleaned_list=[]
    for item in lst:
        for c in item:
            if c.isalpha()!=True:
                item=item.replace(c,'')
        cleaned_list.append(item)
    return cleaned_list
cleaned_list=clean_list(coffe_list)
print(cleaned_list)
for i,j in zip(range(1,len(cleaned_list)+1),cleaned_list):
    print(i,j)'''
from sklearn import datasets
iris=datasets.load_iris()
import pandas as pd
iris_df=pd.DataFrame(iris.data)
iris_df.columns=iris.feature_names
iris_df['target']=iris.target
# print(iris_df.target.astype(float))# 将其转换为float类型
# 三种分析方式：分布分析、统计量分析、相关分析
import matplotlib.pyplot as plt
# plt.hist(iris_df.iloc[:,0],30,color='b')# 设置直方图为30等份，颜色为蓝色
# plt.show()
import scipy
# print(scipy.stats.normaltest(iris_df.iloc[:,0],axis=0))# axis=0 对数据的每一列进行检验
# print(iris_df.target.value_counts())
# iris_df.target.value_counts().plot(kind='pie')
# print(iris_df.iloc[:,0].mean())# 求平均值
# print(iris_df.iloc[:,0].median())# 求中位数
# plt.show()
# x=[item[0] for item in iris.data]
# y=[item[2] for item in iris.data]
# plt.scatter(x[:50],y[:50],marker='_')
# plt.scatter(x[50:100],y[50:100],marker='*')
# plt.scatter(x[100:],y[100:],marker='D')
# plt.legend(loc='best')
# plt.legend(loc='best')
print(iris_df.iloc[:,[0,4]].corr())
print(iris_df['target'].corr(iris_df.iloc[:,0]))
# plt.show()
# 验证是不是符合正态分布












