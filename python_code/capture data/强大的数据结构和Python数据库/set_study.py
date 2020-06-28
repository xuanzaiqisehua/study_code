'''
集合：一个无序不重复的元素组合
可变集合(set);不可变集合(frozenset)
'''
# #创建集合
# aset=set('hello')
# bset=frozenset('hello')
# print(aset,bset)
# 集合的比较
'''aset=set('sunrise')
bset=set('sunset')
reslt1='u' in aset
reslt2=aset==bset
reslt3=aset< bset # 判断aset是不是bset的真子集
reslt4=set('sun')<aset
print(reslt1,reslt2,reslt3,reslt4)'''
## 集合关系运算
# aset=set('sunrise')
# bset=set('sunset')
# result=aset&bset#计算交集
# result1=aset| bset # 计算并集
# result2=aset- bset #差（差补）：属于aset但不属于bset
# result3=aset^ bset# 对称差分：aset中有但bset没有+bset中有但aset没有
# print(result2,result3)
# # 运算符可复合：&=,|=,-=,^=
# aset-=set('sun')# 使用-=作差补
# print(aset)
# 集合内建函数
#面向可变和不可变集合
'''s.issubset(t)# s是不是t的子集
   s.issuperset(t)# s包含t
   s.union(t)并集
   s.insersection(t)交集
   s.difference(t)差补，选出属于s但不属于t
   symmetric_difference(t)# 对称差分
   copy()
'''
# aset=set('sunrise')
# bset=set('sunset')
# cset=aset.copy()
# aset.symmetric_difference(bset)
# print(aset.symmetric_difference(bset))
'''
可变集合：
update(t)
insersection_update(t)
difference_update(t)
symmetric_difference_update(t)
add(obj)
remove(obj)
discard(obj)
pop()
clear()
'''
aset=set('sunrise')
aset.add('!')
print(aset)
aset.remove('!')
print(aset)
aset.update('Yeah')
print(aset)
aset.clear()









