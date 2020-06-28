# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 13:21
# @Author  : Gepenghua
# @FileName: Basic Operations on Images.py
# @Email : 578517264@qq.com
# @Software: PyCharm
# @github    ：https://github.com/xuanzaiqisehua?tab=repositories
import cv2 as cv
# img=cv.imread('1.jpg')
# *********************通过行列坐标值获取像素点，对于BGR图片返回Blue, Green, Red 组成的数组，对于灰度图只返回强度
'''px=img[100,100]
print(px)
gray=img[100,100,0]
print(gray)'''
#******************修改像素值
'''img[100,100]=[255,255,255]
print(img[100,100])'''
#*************
#虽然上面的方法能够获得一个单独的像素值，但是使用numpy遍历每个像素并修改非常慢，可以用array.item()/array.itenset()方法更好
# 访问RED
# print(img.item(10,10,2))
# #修改RED
# img.itemset((10,10,2),100)
# print(img.item(10,10,2))
# *****************图像属性
'''print(img.shape)#图像形状，彩色图像返回3维数组，灰度图返回二维数组（没有通道数）
print(img.size)#图像总像素
print(img.dtype)#图像数据类型'''
#**************图像检测，将图像中的感兴趣区域框出来
'''ball=img[280:340,330:390]
# print(img.shape)
img[273:333,100:160]=ball
cv.imshow('image',img)
cv.waitKey(0)&0xFF
print(img)'''
#***************分割和合并图像通道
#有时需要将三通道分开单独使用或者有时候需要将三通道合并
'''b,g,r=cv.split(img)
print(b,g,r)
img=cv.merge((b,g,r))
# 或者b=img[:,:,0]
# 将所有红色像素都设置为0
img[:,:,2]=0'''
#***************为图像设置边框（填充）
'''from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv.imread('1.jpg')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()'''
'''img1=cv.imread('1.jpg')
img2=cv.imread('2.jpg')
print(img1.shape,img2.shape)
dst=cv.addWeighted(img1,0.7,img2,0.3,0)#两张图片相加大小必须一样
cv.imshow('dst',dst)
cv.waitKey(0)
cv.destroyAllWindows()'''
#*******************按位操作
#加载两个图象
'''img1=cv.imread('1.jpg')
img2=cv.imread('logo.jpg')
#将logo加载到左上角
rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]
#创建logo遮罩，并同时创建其反遮罩
img2gray=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret,mask=cv.threshold(img2gray,10,255,cv.THRESH_BINARY)
mask_inv=cv.bitwise_not(mask)
#将logo中的ROI涂黑
img_logo_bg=cv.bitwise_and(roi,roi,mask=mask_inv)
img_logo2_fg=cv.bitwise_and(img2,img2,mask=mask)
dst=cv.add(img_logo_bg,img_logo2_fg)
img1[0:rows,0:cols]=dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()'''
#*******************处理图片过程中，需要度量代码的性能
'''import time
img=cv.imread('1.jpg')
e1=cv.getTickCount()
# e1=time.time()
#代码执行部分
for i in range(5,49,2):
    img=cv.medianBlur(img,1)#中值滤波
e2=cv.getTickCount()
# e2=time.time()
time=(e2-e1)/cv.getTickFrequency()
print(time)'''
#***************************8Ipython魔术功能
'''#opencv使用SSE2, AVX等进行了优化，假如系统支持可以通过设置使用优化功能，使用优化功能比不使用优化快2倍，在代码顶端使用
flag=cv.useOptimized()
print(flag)# 返回true
cv.setUseOptimized(False)
flag2=cv.useOptimized()
print(flag2)#返回False
#有时您可能需要比较两个类似操作的性能。IPython为您提供了一个神奇的命令计时器来执行此操作。它会多次运行代码以获得更准确的结果。再一次，它适合于测量单行代码。
#x = 5  ％timeit y = x ** 2'''
'''
1、更多IPython魔术命令
还有其他一些魔术命令可以用来衡量性能，性能分析，行性能分析，内存测量等。它们都有很好的文档记录。因此，此处仅提供指向这些文档的链接。建议有兴趣的读者尝试一下。
性能优化技术
2、有几种技术和编码方法可以充分利用Python和Numpy的性能。注意：首先尝试以一种简单的方式实现该算法。工作正常后，对其进行概要分析，找到瓶颈并进行优化。
1）尽可能避免在Python中使用循环，尤其是双/三重循环等。它们本来就很慢。
2）由于Numpy和OpenCV已针对向量运算进行了优化，因此将算法/代码向量化到最大程度。
利用缓存一致性。
3）除非有必要，否则切勿复制数组的副本。尝试改用视图。阵列复制是一项昂贵的操作。
4）如果执行完所有这些操作后代码仍然很慢，或者不可避免地需要使用大循环，请使用Cython等其他库来使其更快'''
#*************************改变图像色彩空间
#RGB 颜色空间适合于显示系统，却并不适合于图像处理
'''flags=[i for i in dir(cv) if i.startswith('COLOR_')]
print(flags)'''
#***********************实现对蓝色目标的跟踪，步骤：获取视频帧，将视频帧转换为hsv颜色空间，设定hsv图片的蓝色范围阈值
'''import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)#0表示打开电脑中的摄像头捕获视频，cv.VideoCapture('1.mov')表示读取本地视频文件
while(1):
    _,frame=cap.read()#返回的是捕获视频的状态和视频帧，如果_为True表示获取成功
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)#将视频帧BGR颜色转换问HSV
    lower_blue=np.array([110,50,50])
    upper_blue = np.array([130, 255, 255])
    # inRange()函数可实现二值化功能（这点类似threshold()函数），更关键的是可以同时针对多通道进行操作，使用起来非常方便！
    # 检查数组元素是否在另外两个数组元素值之间
    mask=cv.inRange(hsv,lower_blue,upper_blue)
    #cv.bitwise_and解释参考：https://blog.csdn.net/u011028345/article/details/77278467
    res=cv.bitwise_and(frame,frame,mask=mask)#mask掩膜操作,bitwise_and对二进制数据进行“与”操作
    #     数字图像处理中,掩模为二维矩阵数组,有时也用多值图像，图像掩模主要用于：
    # ①提取感兴趣区,用预先制作的感兴趣区掩模与待处理图像相乘,得到感兴趣区图像,感兴趣区内图像值保持不变,而区外图像值都为0。
    # ②屏蔽作用,用掩模对图像上某些区域作屏蔽,使其不参加处理或不参加处理参数的计算,或仅对屏蔽区作处理或统计。
    # ③结构特征提取,用相似性变量或图像匹配方法检测和提取图像中与掩模相似的结构特征。
    # ④特殊形状图像的制作。
    cv.imshow('frame',frame)#显示原视频
    cv.imshow('mask',mask)#类似于做了一个二值化操作，低于阈值设为0，高于阈值设为1
    cv.imshow('res', res)#显示
    k=cv.waitKey(5)&0xFF
    if k==27:
        break
cv.destroyAllWindows()
'''
#*****************如何找到想要跟踪的HSV值
'''import numpy as np
white=np.uint8([[[255,255,255]]])
hsv_white=cv.cvtColor(white,cv.COLOR_BGR2HSV)
print(hsv_white)#[[[ 60 255 255]]] 分别将[H-10，100,100]和[H + 10，255，255]作为下限和上限，也即是[[[ 50 255 255]]] [[[ 70 255 255]]]'''
import numpy as np
cap=cv.VideoCapture(0)#0表示打开电脑中的摄像头捕获视频，cv.VideoCapture('1.mov')表示读取本地视频文件
while(1):
    _,frame=cap.read()#返回的是捕获视频的状态和视频帧，如果_为True表示获取成功
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)#将视频帧BGR颜色转换问HSV
    lower_blue=np.array([110,50,50])
    upper_blue = np.array([130, 255, 255])
cap=cv.VideoCapture(0)
while(1):
    _,frame=cap.read()
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_white=np.array([0,0,])




















