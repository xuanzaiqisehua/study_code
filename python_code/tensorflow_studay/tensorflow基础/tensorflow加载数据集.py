# 参考
import tensorflow as tf
#******************* 加载手写数字数据集 *******************
mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()#加载手写数据集
print(x_train.shape)
print(x_test.shape)
y_train=y_train.astype('float32')
y_test=y_test.astype('float32')
# 重置1000个样例
x_val=x_train[-10000:]
y_val=y_train[-10000:]
x_train=x_train[:-10000]
y_train=y_train[:-10000]
'''print(x_train.shape)
print(x_val.shape)
print(x_train[0])
import matplotlib.pyplot as plt
fig=plt.figure()#创建一个窗口
for i in range(15):
    plt.subplot(3,5,i+1)
    plt.tight_layout()# 自动适配子图尺寸
    plt.imshow(x_train[i],cmap='Greys')#使用灰色显示像素灰度值
    plt.title('Label:{}'.format(y_train[i]))# 设置标签为子图标题
    plt.xticks([])#删除x轴
    plt.yticks([])#删除y轴
plt.show()'''
#******************* 使用tf.keras管理Sequential模型 *******************
model=tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),#将图像28*28的数组拉成一列
    tf.keras.layers.Dense(128,activation='relu'),#全连接层使用relu激活函数
    tf.keras.layers.Dropout(0.2),#使用dropout裁剪神经网络
    tf.keras.layers.Dense(10)# 10层全连接层
])
#通过model.summary()输出模型各层的参数状况
model.summary()
tf.keras.utils.plot_model(model, 'mnist_model.png')
# model.compile(optimizer="adam",
#               loss='sparse_categorical_crossentropy',
#               metrics=['accuracy'])
# model.fit(x_train, y_train, epochs=5)
# model.evaluate(x_val, y_val)
# model.save("mnist_model")#保存为 SavedModel 格式模型
# # 加载SaveModel格式模型
# sm=tf.keras.models.load_model('minist_model')
# sm.evaluate(x_val, y_val)