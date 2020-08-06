import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import numpy as np
# from tensorflow.keras import layers
'''tf.compat.v1.disable_eager_execution()#tensorflow V1与V2版本不兼容
hello = tf.constant('hello,tensorflow')
a=tf.constant(2)
b=tf.constant(3)
with tf.compat.v1.Session() as sess:
    print(sess.run(hello))'''
# print(tf.__version__)
# print(tf.keras.__version__)
#*******************构建模型的三种方式************************
'''
1、Sequential 按层顺序构建模型：对于顺序结构的模型，优先使用Sequential方法构建
2、使用函数API构建任意结构模型：模型有多输入或者多输出推荐使用函数式API构建
3、继承Model基类构建自定义模型：如果无特定必要避免使用这种方式
'''
#*****************************Mnist数据集*************************
'''import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
mnist=tf.keras.datasets.mnist
(train_x,train_y),(test_x,test_y)=mnist.load_data()#加载数据集
for i in range(4):
    num=np.random.randint(1,50000)#产生随即索引
    plt.subplot(1,4,i+1)#将画布分为几个区域
    plt.axis('off')
    plt.imshow(train_x[num],cmap='gray')
    plt.title(train_y[num])
plt.show()'''
#****************minis时尚用品数据集******************888
'''import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
fashion_mnist=tf.keras.datasets.fashion_mnist
(train_x,train_y),(test_x,test_y)=fashion_mnist.load_data()#加载数据集
for i in range(4):
    num=np.random.randint(1,50000)#产生随即索引
    plt.subplot(1,4,i+1)#将画布分为几个区域
    plt.axis('off')
    plt.imshow(train_x[num],cmap='gray')
    plt.title(train_y[num])
plt.show()'''
#*********************基本操作（常数）*******************
'''a=tf.constant(2)
b=tf.constant(3)
add=tf.add(a,b)#+
sub=tf.subtract(a,b)#-
mul=tf.multiply(a,b)#*
div=tf.divide(a,b)#/
mean=tf.reduce_mean([a,b])#平均数
sum=tf.reduce_sum([a,b])#和
print(add.numpy())#add.numpy()将tensor类型转换为numpy数组
print(mean.numpy())
print(sum.numpy())
matrix1 = tf.constant([[1., 2.], [3., 4.]])
matrix2 = tf.constant([[5., 6.], [7., 8.]])
produc=tf.matmul(matrix1,matrix2)
print(matrix1)'''
#*********************线性回归*******************
'''import tensorflow as tf
import numpy as np
rng=np.random
learning_rate=0.01
training_steps=1000
diaplay_step=50
#训练数据
X = np.array([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,
              7.042,10.791,5.313,7.997,5.654,9.27,3.1])
Y = np.array([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,
              2.827,3.465,1.65,2.904,2.42,2.94,1.3])
W=tf.Variable(rng.randn(),name='weight')
b=tf.Variable(rng.randn(),name='weight')
def linear_regression(x):
    return  W*x+b
def mea_square(y_pred,y_true):
    return  tf.reduce_mean(tf.square(y_pred-y_true))
optimizer=tf.optimizers.SGD(learning_rate)
def run_optimization():
    with tf.GradientTape() as g:
        pred=linear_regression(X)
        loss=mea_square(pred,Y)
    gradients=g.gradient(loss,[W,b])
    optimizer.apply_gradients(zip(gradients,[W,b]))
#训练数据
for step in range(1,training_steps+1):
    run_optimization()
    if step%diaplay_step==0:
        pred=linear_regression(X)
        loss=mea_square(pred,Y)
        print('step:%i,loss:%f,W:%f,b:%f'%(step,loss,W.numpy(),b.numpy()))'''
#********************手写数据集**********************8
'''from tensorflow.keras import Model,layers
import numpy as np
num_classes=10
num_features=784
#训练参数
learning_rate=0.1
training_steps=2000
batch_size=256
display_step=100
#网络参数
n_hidden_1=128
n_hidden_2=256
from tensorflow.keras.datasets import mnist
(x_train,y_train),(x_text,y_text)=mnist.load_data()
x_train,x_text=np.array(x_train,np.float32),np.array(x_text,np.float32)
x_train,x_text=x_train.reshape([-1,num_features]),x_text.reshape([-1,num_features])#将训练测试数据转换为784*1的数据
x_train,x_text=x_train/255,x_text/255#将像素值转换为0-1的数据，标准化像素值
train_data=tf.data.Dataset.from_tensor_slices((x_train,y_train))#将数据与标签进行切分,比如shape(5,2)切分后为5个元素，每个元素的形状为2
#此处切分后为{”image”:image_tensor,”label”:label_tensor｝的形式。
train_data = train_data.repeat().shuffle(5000).batch(batch_size).prefetch(1)#shuffle(5000)数字越大混乱程度越大，
# repeat()表示将原字符串重复n次。prefetch(1)预抓数据
class NeuralNet(Model):
    def __init__(self):
        super(NeuralNet, self).__init__()
        #全链接隐藏层
        self.fc1=layers.Dense(n_hidden_1,activation=tf.nn.relu)
        self.fc2 = layers.Dense(n_hidden_2, activation=tf.nn.relu)
        self.out=layers.Dense(num_classes)
    #前向传播
    def call(self, x, is_training=False, mask=None):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.out(x)
        if not is_training:
             x=tf.nn.softmax(x)
        return x
neural_net=NeuralNet()
def cross_entropy_loss(x, y):
    # Convert labels to int 64 for tf cross-entropy function.
    y = tf.cast(y, tf.int64)
    # Apply softmax to logits and compute cross-entropy.
    loss = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=x)
    # Average loss across the batch.
    return tf.reduce_mean(loss)

# Accuracy metric.
def accuracy(y_pred, y_true):
    # Predicted class is the index of highest score in prediction vector (i.e. argmax).
    correct_prediction = tf.equal(tf.argmax(y_pred, 1), tf.cast(y_true, tf.int64))
    return tf.reduce_mean(tf.cast(correct_prediction, tf.float32), axis=-1)

# Stochastic gradient descent optimizer.
optimizer = tf.optimizers.SGD(learning_rate)


def run_optimization(x, y):
    # Wrap computation inside a GradientTape for automatic differentiation.
    with tf.GradientTape() as g:
        # Forward pass.
        pred = neural_net(x, is_training=True)
        # Compute loss.
        loss = cross_entropy_loss(pred, y)

    # Variables to update, i.e. trainable variables.
    trainable_variables = neural_net.trainable_variables

    # Compute gradients.
    gradients = g.gradient(loss, trainable_variables)

    # Update W and b following gradients.
    optimizer.apply_gradients(zip(gradients, trainable_variables))


for step, (batch_x, batch_y) in enumerate(train_data.take(training_steps), 1):
    # Run the optimization to update W and b values.
    run_optimization(batch_x, batch_y)

    if step % display_step == 0:
        pred = neural_net(batch_x, is_training=True)
        loss = cross_entropy_loss(pred, batch_y)
        acc = accuracy(pred, batch_y)
        print("step: %i, loss: %f, accuracy: %f" % (step, loss, acc))'''













