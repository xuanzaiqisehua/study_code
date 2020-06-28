'''数据探索和数据预处理
(1)数据探索包括检查数据错误，了解数据分布特征和内在规律
(2) 数据预处理： 数据清洗（datacleaning）、数据集成（data integration）、数据变换（data transformation）、数据规约（data reduction）
数据清洗中的缺失值处理：删除或填充，
填充：（1）固定值（2）均值、中位数、众数（3）上下数据（4）插值函数：拉格朗日插值（5）最可能的值（使用最近邻或者回归法建模）
异常值：异常值常称为离群点或噪声：数值明显偏离其他观测值的点，异常值可通过简单的统计方法或者绘图检测，或者使用机器学习方法如聚类来检测
异常值处理：同缺失值处理、局部均值（分箱）、不处理
简单的统计方法：（1）数据统计性描述函数describe()（2）箱型图(boxplot())（3）基于3Q原则手工写程序
(1)describe 异常值通过最大、最小、平均等特征值来判断
（2）箱型图以四分位距（IQR就是上四分位和下四分位的差值也就是箱子高度的1.5倍），如果超过上四分位+IQR的1.5倍和下四分位-IQR的1.5倍距离就是异常值
箱型图有它自己的检测异常的公式，也可以自己编写程序
（3）3Q原则：如果这组数据服从正态分布，异常值定义为，一组测定值中与均值的偏差超过3倍标准差的值，即数据：U-3Q<数据<U+3Q，U为均值，Q为标准差
'''
import pandas as pd
data=pd.read_csv('AXP.csv',index_col='Date')#读出数据并将Date设为DataFrame的索引
import matplotlib.pyplot as plt
# data.isnull()#判断是否存在缺失值，如果缺失返回False
# 删除缺失值
# result=data.dropna()#how设置为all时如果某行或某列全部为缺失就删除，默认为any只要缺失就删除缺失那行
# help(data.dropna)
# 填充缺失值,均值填充，inplace为True改变原始数据
# data.fillna(data.mean(),inplace=True)
#上下数据填充缺失值，method='ffill'(上一个)，bfill(下一个)
result=data.fillna(method='ffill')
# print(result)
# 最大值填充data.max()
'''
还可以使用插值函数对缺失值进行插补，例如拉格朗日插值法，它的基本思想是
对于平面上已知的n个点确定一个n-1次多项式使此多项式曲线过这n个点，
然后将缺失的函数值对应的点x带入多项式得到缺失值的近似值L(x)。'''
'''import pandas as pd
from scipy.interpolate import lagrange  # 导入拉格朗日插值函数
df = pd.read_excel("data.xlsx")
for i in df.columns:
    for j in range(len(df)):
        if (df[i].isnull())[j]:  # 如果为空则进行插值
            k = 3  # 设置取前后数的个数为3，默认为5
            y = df[i][list(range(j - k, j)) + list(range(j + 1, j + 1 + k))]  # 取数
            y = y[y.notnull()]  # 去掉取出数中的空值
            df[i][j] = lagrange(y.index, list(y))(j)
print(df)'''
#(1) 假设缺失值已经填充，使用describe()函数查看是否有异常数据
# de_result=result.describe()
# print(de_result)# 输出特征值，观察最小值，最大值，标准差平均值，1/4,1/2,3/4处的值看是否异常
#(2) 箱型图（盒须图）：能够反映原始数据的分布情况
#dresult的数据比较完整，为了测试添加一行异常值
# print(result)
result.loc['2020-02-05']=[200,6,6,89,56,8]
# 因为数据中最后一列数据比其他四列数据都大，所以将其删除或者选择前五列数据
'''result1=result.iloc[:,1:5]# 方法一
result.drop('Volume',axis=1,inplace=True)#方法二
result.boxplot()#绘制箱型图,箱型图最上面是最大值，最下面线是最小值，箱子上面的线是上四分位（75%）的值。下面是1/4（也就是25%）位置的值，
中间是中位数
plt.show()
print(result)'''
#(3) 3Q原则
'''result1=result.iloc[:,1:5]
result2=result1[abs(result1-result1.mean())<3*result1.std()]# 找出异常值
result3=result2.dropna(how='all') #删除异常值
print(result3)'''
'''数据预处理之数据变换：将数据变换为合适的形式，常见方式：规范化、连续属性离散化、特征二值化
 解决哪些影响：（1）量刚不同（比如厘米和米）（2）数值范围差异大
 规范化常用方法：最小-最大规范化（离差规范化）；z-score规范化（也叫零均值规范化或标准化）；小数定标规范化
 不同模型和应用需要用不同的规范化方法，比如聚类：（用距离度量相似性）用z-score来规范化比较好
'''
# 以波斯顿房价数据集为例介绍规范化做法
from sklearn import datasets
boston=datasets.load_boston()
# print(boston)# 查看bosten的详细信息
# print(boston.data)# 查看数据
# print(boston.feature_names)# 查看属性
# print(boston.target)# 查看目标属性MEDV房价中位数具体值
# print(boston.data.shape)
# 选择'NOX','RM','AGE'来做规范化处理，分别表示一氧化氮浓度，平均每居民房数，194.年之前建成的所有者占用单位的比例
import pandas as pd
df=pd.DataFrame(boston.data[:,4:7])
df.columns=boston.feature_names[4:7]# 给boston的4到6行加上columns,切片操作后列标签就没有了，这条语句是加上列标签
# print(df.info())# 查看df的信息
#（1） 最小-最大规范化,比较适合不涉及度量距离的场景，问题是如果值超过了最小值或最大值的范围会越界，
# 需要重新定义，如果某个数字跟大则规范化后的数字会很相近且接近于0
# x=(df-df.min())/(df.max()-df.min())  #min_max 的公式
# print(x)
# 还可以直接调用sklearn中的preprocessing 模块进行数据预处理
# from sklearn  import preprocessing
# minmax_df=preprocessing.minmax_scale(df)
# print(minmax_df)
# （2）Z-score 规范化：特征：使用最多，处理后数据的均值为0，标准差为1
# zscore_df=(df-df.mean())/df.std() #z-scere 的公式
# print(zscore_df)
# from sklearn  import preprocessing #调用函数处理
# zscore=preprocessing.scale(df)
# （3）小数定标标准化，特征：移动小数点位置，移动位数取决于属性绝对值的最大值，常见落在[-1,1]之间
# 比如最大值为90，位数为2，所有值除以10**2（10的2次方）
'''import numpy as np
n=np.ceil(np.log10(df.abs().max())) # 10g10()求出10的多少次为最大值，求出来的数字为小数，向上取整用np.ceil()
result=df/10**n
print(result)'''
# (4）连续属性离散化，方法（1）分箱：等宽法（将数据区间按照设定的箱子个数划分），等频法（要求放进每个箱子记录数相同）（2）聚类
# result=pd.cut(df.AGE,5,labels=(range(5)))# 等宽法，缺点容易受异常值影响，分箱后可能有的区域值很多，有的很少
# result1=pd.qcut(df.AGE[:10],5,labels=(range(5)))# 等频法,查看钱10条记录，等频法缺点：容易将相同的值分到不同箱中，
# print(result1)
#（5） 特征二值化,核心是设定一个阈值，大于阈值设为1小于阈值设为0，很适合用于目标属性把多类问题转换为二分类问题
#可以调用sklearn 中 preprocessing 方法：Binarization，LabelEncoder
'''from sklearn.preprocessing import Binarizer
x=boston.target.reshape(-1,1)# 波斯屯房价的目标值shape原来为一行506列，将其重设为506行
result=Binarizer(threshold=20.0).fit_transform(x)# 将其进行特征二值化处理
print(result)'''
'''数据规约（data reduction）是数据预处理中的最重要步骤,现实生活中数据维度很大，会出现维度灾难，样本稀疏的情况，
也就是样本中有大量的0或者距离过大的问题，常常需要降维（或称为属性规约）缓解维数灾难，也可以从数据集中选择部分数据，
（这叫数值规约），属性规约和数值规约都是数据规约，数据规约后得到一个比原数据集小的规约表示
（1）属性规约：向前选择（空的集合选择最优的数据逐一添加）、向后删除（从最后逐个删除最差的数据）、决策树（机器学习常用方法）、PCA（常用线性
降维方法，通过某种线性关系将高维数据投影到低维空间表示，并期望在所投影的维度上数据的方差最大，选择出较少的维度也就是主成分，忽略对数据不重要的成分，
尽可能多的保留原数据的特征）
（2）数值规约：包括有参方法（回归法对数线性模型）和无参方法（直方图、聚类、抽样）
'''
'''（1）属性规约-PCA方法：sklearn.decomposition'''
from sklearn.decomposition import PCA
from sklearn  import preprocessing #调用函数处理
x=preprocessing.scale(boston.data) #对房价数据做标准化处理
# pca=PCA(n_components=5)#调用PCA函数,参数n_components为none则保留全部特征，为2则保留2个特征，='mle'：算法将自动选择满足所要求的方差百分比的特征个数
# # 用数据训练pca 模型
# result=pca.fit(x)
# result1=pca.explained_variance_ratio_ # 返回成分各自方差百分比（也就是变量的方差贡献率），百分比越大权重越大
# pac_sum=sum(pca.explained_variance_ratio_) # 求出前五个特征值总和，如果五个特征能够表达99%的特征说明用五个特征就行

# 也可以直接用'mle'来自动选择特征个数
'''pca=PCA(n_components='mle')mel:（自动选择了12个数据）
pca.fit(x)
pac_sum=pca.explained_variance_ratio_ # 表示各个成分各自的方差百分比也就是变量的方差贡献率
print(sum(pac_sum))# 累计贡献率为0.995'''

'''（2）数据规约-直方图:直方图规约就是将直方图中箱子个数由观测值的数量n减少到k个
表现：用分箱表示数据分布
     每个箱子代表一个属性-频率对

'''
import numpy as np
import matplotlib.pyplot as plt
data= np.random.randint(1,10,50)#范围1-10，,5个数据
# plt.hist(data)
# bins=np.linspace(data.min(),data.max(),3,endpoint=True)# 找到箱子的三个分割点，endpoint=True包含终止值
# plt.hist(data,bins=bins,rwidth=0.95,edgecolor='k')
# plt.show()
'''抽样是是数值规约最常见的方法，从原始数据中采用抽样方法对数据进行降维从而达到数据规约的目的
   抽样包括：随机抽样（放回和不放回）、聚类抽样、分层抽样
'''
from sklearn import datasets
import pandas as pd
iris=datasets.load_iris()
# 随机抽样
iris_df=pd.DataFrame(iris.data)
iris_df.columns=iris.feature_names
iris_df['target']=iris.target # 将鸢尾花的目标数据赋给iris_df的target属性
# iris_df.sample(n=10)# n为抽样个数
# iris_df.sample(frac=0.3,replace=True)# 抽取数据的30%,replace=True：有放回抽样
# 分层抽样：抽取类别0数据的30%
A=iris_df[iris_df.target==0].sample(frac=0.3) #抽取目标数据的30%
B=iris_df[iris_df.target==1].sample(frac=0.2)#抽取目标数据的20%
C=A.append(B)# 将两次抽取结果合并
print(C)




































