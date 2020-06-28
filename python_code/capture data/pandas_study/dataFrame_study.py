import pandas as pd
import numpy as np
# sa=pd.Series([1,2,3],index=list('abc'))
# sa['a']=7 # 等于sa.a=7
# x=pd.DataFrame({'x':[1,2,3],'y':[3,4,5]},index=[3,4,5])
# x.iloc[1]={'x':9,'y':99}
df1=pd.DataFrame(np.random.randn(6,4),index=list('abcdef'),columns=list('ABCD'))# 随机产生6行4列的数据
# print(df1)
# print(df1.loc[['a','b','c'],:])
# print(df1.loc['a':,['A',"B"]])
# print(df1.loc['a':,'A':"B"])
# print(df1)
# print(df1.loc[:,df1.loc["a"]>0])
# print(df1.at['a','A'])# 等于df1.loc['a','A']
s=pd.Series(list('abcde'),index=[0,3,2,5,4])
print(s)
# print(s.loc[3:5])
# print(s.iloc[3:5])
# print(s.sort_index())
# print(s.sort_values())
# print(s.sort_index().loc[2:6])# 排序后选择区域[2:6]
# 通过位置选择
s1=pd.Series(np.random.randn(5),index=list(range(0,10,2)))
s1.iloc[:3]=0 # 对位置0,1,2进行赋值
# print(s1.iloc[0:2])






