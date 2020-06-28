'''# pytorch 构建网络的四种方法:
#https://blog.csdn.net/qq_37385726/article/details/81740233
# 假设构建一个网络模型如下：
# 卷积层--》Relu层--》池化层--》全连接层--》Relu层--》全连接层'''
# 导入必要的包
import torch
import torch.nn.functional as F
from collections import OrderedDict
class Net1(torch.nn.Module):
    def __init__(self):
        super(Net1,self).__init__()
        self.conv1=torch.nn.Conv2d(3,32,3,1,1)
        self.dese1=torch.nn.Linear(32*3*3,128)
        self.dese2=torch.nn.Linear(128,10)
    def forward(self, x):
        x = F.max_pool2d(F.relu(self.conv(x)), 2)
        x = x.view(x.size(0), -1)
        x = F.relu(self.dense1(x))
        x = self.dense2(x)
        return x
print("Method 1:")
model1 = Net1()
print(model1)

#构建输入集
# 构建输入集
#****************************
#参考：https://blog.csdn.net/zkk9527/article/details/88399176
import torch as t
from torch import nn
from torch.autograd import Variable as V
import torch.nn.functional as F
class Net(nn.Module):    # 自定义层继承nn.Module,class 主要写两个函数一个是初始化函数，另一个是forward函数
     def __init__(self):  #
         super.__init__()#super给父类nn.Module初始化
         self.cov1=nn.Conv2d(1,6,5)#第一层卷积层，输入通道为1，输出通道为6，卷积核5*5
         self.cov2 = nn.Conv2d(6, 16, 5)#注意前后输出通道和输入通道的一致性，比如第一个卷积层输出6通道，第二个输入也为6通道
     def forward(self, *input):
         x=F.max_pool2d(F.relu(self.cov1(input),2))
         x = F.max_pool2d(F.relu(self.cov2(x), 2))
         return  x
#实例化一个Net，Net只是一个类不能直接传参，此处的类与python定义的类有点不同，python中的class可以传参，传入的是__init__中，
#而此处的class中传参是要传到forward中的，所以先实例化，在传参
net=Net()
output=net(input)#input为tensor类型
