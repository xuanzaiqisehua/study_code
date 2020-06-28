# DataFrame的集合对应二维表结构，可以将其视为共享同一个index的Series
# DataFrame 创建：可以由列表、元组、字典、Series、ndarray或者文件创建
import pandas as pd
import numpy as np
# data={'name':['Wangdachui','Linling','Niuyun'],'pay':[4000,5000,6000]}
# frame=pd.DataFrame(data)
# print(frame)
# data=np.array([('Wangdachui',4000),('Linling',5000),('Niuyun',6000)])
# frame1=pd.DataFrame(data,index=range(1,4),columns=['name','pay'])
# print(frame1.index)
# print(frame1.columns)
# print(frame1.values)
# print(frame1['name'])#选择第0列数据两种方式
# print(frame1.pay)#第1列
# #选择某个区域，比如第0，1行的第一列
# print(frame1.iloc[:2,1])#逗号前面为行0-1行，后面为列范围
# # DataFrame的基本操作
# #DataFrame对象的修改和删除
# frame1['name']='admin'#修改frame1中的name为admin
# print(frame1)
# del frame1['pay']
# print(frame1)
# DataFrame 的统计功能
# DataFrame对象成员找最低工资和高工资人群信息
data={'name':['Wangdachui','Linling','Niuyun'],'pay':[4000,5000,6000]}
frame=pd.DataFrame(data)
# min_data=frame.pay.min()
# max_data=frame.pay.max()
# range_data=frame[frame.pay>=5000]
# print(min_data,max_data)
# print(range_data)
# 创建DataFrame小练习
# music_data=[('the rolling stone','Satisfaction'),('Beatles','Let It Be'),
#             ("Guns N'Roses","Don't Cry"),('Metallica','Nothing Else Matters')]
# music_frame=pd.DataFrame(music_data,index=range(1,5),columns=['singer','song_name'])
# # 或者写为：music_frame.index=range(1,5),music_frame.colums=['singer','song_name']
# print(music_frame)
# 修改操作
# 添加列
# frame['Id']=[2013,2014,2015]
# 添加行,对象标签loc,位置索引iloc,append()或者concat()等函数
# frame.loc[3]=['Liubei','5000','2017']# 添加一行
# 删除数据：del直接对原始数据操作，pandas中drop（）方法删除指定轴上的数据返回一个新的对象，不删除原数据
# del_frame=frame.drop(3)
# print(del_frame)
# 删除指定列、多列
# del1_frame=frame.drop('Id',axis=1)
# del2_frame=frame.drop(['pay','Id'],axis=1)
# print(del1_frame,del2_frame)
# 修改，将pay列全部修改为统一值
# frame['pay']=0
# print(frame)
# 修改某一行
# frame.loc[2]=['Mayun',3000]
# print(frame)


















