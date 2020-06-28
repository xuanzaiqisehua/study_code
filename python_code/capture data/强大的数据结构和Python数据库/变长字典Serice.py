# pandas中的Series是一种有序定长的字典，由数据和索引组成
# 创建
import pandas as pd
# aSer=pd.Series([1,2,'a'])# 自带索引
# bSer=pd.Series(['apple','peach','lemon'],index=[1,2,3])
# #查看index和value bSer.index,bSer.values
# aSer*2#每个元素都乘以2,访问数据元素aSer['a']
# print(bSer)
# 数据对齐
data={'AXP':'86.40','CSCO':'122.64','BA':'99.44'}
sindex=['AXP','CSCO','BA','AAPL']
aser=pd.Series(data,index=sindex)#sindex中有的数据一一对应，没有的对应为NaN(没有对应数据)
# print(pd.isnull(aser))# 检测aser中哪些值为空
bser=pd.Series(data)
cser=bser+aser
print(cser)