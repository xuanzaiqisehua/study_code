import torch
import numpy as np
'''np_data=np.arange(6).reshape(2,3)
# print(np_data)
# 将numpy转换为tensor
torch_data=torch.from_numpy(np_data)
print(torch_data)
# 将torsor转换为numpy
tensor2array=torch_data.numpy()'''
'''#数学运算
data=[-1,-2,1,2]
tensor=torch.FloatTensor(data)#转换问32位浮点tensor
print(tensor,torch.abs(tensor),torch.sin(tensor),torch.mean(tensor))#绝对值，sin三角函数，均值'''
#矩阵乘法
'''data=[[1,2],[3,4]]
tensor=torch.FloatTensor(data)
print(torch.mm(tensor,tensor))#第一个矩阵的第一行乘第二个矩阵的第一列作为第一个元素，然后再乘第二个矩阵的第二列作为第二个元素'''
'''import numpy as np
N,D_in,H,D_out=64,1000,100,10# N为batch size，D_in 是输入维度，H是隐含维度，D_out为输出数据
#创建一个随机输入和输出数据
x=np.random.randn(N,D_in)
y=np.random.randn(N,D_out)
# 随机初始化权重
W1=np.random.randn(D_in,H)
W2=np.random.randn(H,D_out)
learning_rate=1e-6
for t in range(500):
    h=x.dot(W1)#等价于np.dot(x,y)
    h_relu=np.maximum(h,0)#用np.maximum实现relu函数
    y_pred=h_relu.dot(W2)
    loss=np.square(y_pred-y).sum()#计算预测值与实际值差值平方的和
    print(t,loss)
    #计算梯度值
    grad_y_pred=2.0*(y_pred-y)
    grad_w2=h_relu.T.dot(grad_y_pred)
    grad_h_relu=grad_y_pred.dot(W2.T)
    grad_h = grad_h_relu.copy()
    grad_h[h < 0] = 0
    grad_w1 = x.T.dot(grad_h)
    # Update weights
    W1 -= learning_rate * grad_w1
    W2 -= learning_rate * grad_w2'''

# 指定设备CPU或者GPU
'''import torch
dtype = torch.float
device = torch.device("cpu")
# device = torch.device("cuda:0") # Uncomment this to run on GPU

# N is batch size; D_in is input dimension;
# H is hidden dimension; D_out is output dimension.
N, D_in, H, D_out = 64, 1000, 100, 10

# Create random input and output data
x = torch.randn(N, D_in, device=device, dtype=dtype)
y = torch.randn(N, D_out, device=device, dtype=dtype)

# Randomly initialize weights
w1 = torch.randn(D_in, H, device=device, dtype=dtype)
w2 = torch.randn(H, D_out, device=device, dtype=dtype)

learning_rate = 1e-6
for t in range(500):
    # Forward pass: compute predicted y
    h = x.mm(w1)
    h_relu = h.clamp(min=0)
    y_pred = h_relu.mm(w2)

    # Compute and print loss
    loss = (y_pred - y).pow(2).sum().item()
    if t % 100 == 99:
        print(t, loss)

    # Backprop to compute gradients of w1 and w2 with respect to loss
    grad_y_pred = 2.0 * (y_pred - y)
    grad_w2 = h_relu.t().mm(grad_y_pred)
    grad_h_relu = grad_y_pred.mm(w2.t())
    grad_h = grad_h_relu.clone()
    grad_h[h < 0] = 0
    grad_w1 = x.t().mm(grad_h)

    # Update weights using gradient descent
    w1 -= learning_rate * grad_w1
    w2 -= learning_rate * grad_w2'''










