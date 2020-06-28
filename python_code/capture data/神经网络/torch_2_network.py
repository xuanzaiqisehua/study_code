import torch
x1=torch.empty(5,3)#构造未初始化矩阵
x2=torch.rand(5,3)#随机初始化矩阵
x3=torch.zeros(5,3,dtype=torch.long)#构造dtype long 的矩阵
x4=torch.tensor([5.5,3])#从数据构造张量
x5=x4.new_ones(5,3,dtype=torch.double)#基于现有张量创建张量，这些方法将重用输入张量的属性，除非提供新值
x6=torch.randn_like(x5,dtype=torch.float)#创建一个shape像x5的矩阵
print(x6)
print(x6.size())#输出x6的大小
#************运算
# https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py
'''result=torch.empty(5,3)
torch.add(x,y,out=result)
print(result)'''
#调整张量的大小，用torch




