# -*- coding: utf-8 -*-
# @Time    : 2020/5/20 14:19
# @Author  : Gepenghua
# @FileName: 图像的几何变换.py
# @Email : 578517264@qq.com
# @Software: PyCharm
# @github    ：https://github.com/xuanzaiqisehua?tab=repositories
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
# img=cv.imread('2.jpg')
#重置输入图片大小,interpolation 参数为插值算法，fx、fy是沿x轴和y轴的缩放系数
'''
最优一个参数interpolation表示插值方式，有以下几种：
INTER_NEAREST - 最近邻插值
INTER_LINEAR - 线性插值（默认）
INTER_AREA - 区域插值
INTER_CUBIC - 三次样条插值
INTER_LANCZOS4 - Lanczos插值
'''
# res=cv.resize(img,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)
'''height,width=img.shape[:2]
res=cv.resize(img,(2*width,2*height),interpolation=cv.INTER_CUBIC)
cv.imshow('img',res)
cv.waitKey(0)
cv.destroyAllWindows()'''
#*******************************平移*******************************
'''img=cv.imread('2.jpg',0)#读取灰度图
rows,cols=img.shape#灰度图shape为2
M=np.float32([[1,0,100],[0,1,50]])
dst=cv.warpAffine(img,M,(cols,rows))#图像仿射变换warpAffine
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()'''
#*******************************旋转*******************************
'''M=cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()'''
#*******************************仿射变换*******************************
#将图片进行仿射变换，仿射变换需要一个M矩阵，getAffineTransform函数可以自动求出，getAffineTransform获得根据三点计算的仿射变换矩阵
'''import matplotlib.pyplot as plt
img = cv.imread('2.jpg')
rows,cols,ch=img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])#原始图像中的三个坐标
pts2 = np.float32([[10,100],[200,50],[100,250]])#变换后三个点对应的坐标
M = cv.getAffineTransform(pts1,pts2)#cv.getAffineTransform(原图像的三个点,变换后图像的三个点)根据给出的点左边自动求出M函数
dst = cv.warpAffine(img,M,(cols,rows))#仿射变换，参数为输入图像，输出图像，仿射矩阵
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()'''
#*******************************透视变换************************
#原理：plt.imshow()函数负责对图像进行处理，并显示其格式，而plt.show()则是将plt.imshow()处理后的函数显示出来。
'''img = cv.imread('2.jpg')
rows,cols,ch=img.shape
pts1=np.float32([[56,65],[368,62],[28,387],[389,390]])
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])
M=cv.getPerspectiveTransform(pts1,pts2)#取得图像透视矩阵
dst=cv.warpPerspective(img,M,(300,300))#透视变换
plt.title('Input')
plt.subplot(121)
plt.imshow(img)
plt.title('output')
plt.subplot(122)
plt.imshow(dst)
plt.show()'''
#*******************简单阈值设定、自适应阈值设定***************
'''
THRESH_BINARY:过门限的值为最大值，其他值为0
THRESH_BINARY_INV:过门限的值为0，其他值为最大值
THRESH_TRUNC:过门限的值为门限值，其他值不变
THRESH_TOZERO:过门限的值不变，其他设置为0
THRESH_TOZERO_INV:过门限的值为0，其他不变
'''
'''ret,thresh1=cv.threshold(img,127,255,cv.THRESH_BINARY)
ret,thresh2=cv.threshold(img,127,255,cv.THRESH_BINARY_INV)
ret,thresh3=cv.threshold(img,127,255,cv.THRESH_TRUNC)
ret,thresh4=cv.threshold(img,127,255,cv.THRESH_TOZERO)
ret,thresh5=cv.threshold(img,127,255,cv.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.xticks([]),plt.yticks([])#范围和标签xticks(np.arange(5), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue'))
plt.show()'''
#******************自适应阈值*****************
'''
ADAPTIVE_THRESH_MEAN_C，为局部邻域块的平均值。该算法是先求出块中的均值，再减去常数C。
ADAPTIVE_THRESH_GAUSSIAN_C ，为局部邻域块的高斯加权和。该算法是在区域中（x，y）周围的像素根据高斯函数按照他们离中心点的距离进行加权计算， 再减去常数C。
'''
'''img=cv.imread('2.jpg',0)
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)#ret接受阈值127，th1是一个全0矩阵
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,7,2)#均值
th3=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,7,2)#高斯
images=[img,th1,th2,th3]
for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(i)
    plt.xticks([]),plt.yticks([])
plt.show()'''
#******************大津法/最大类间方差*****************
'''img=cv.imread('2.jpg',0)
# global thresholding
ret1,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# Otsu's thresholding
ret2,th2 = cv.threshold(img,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# Otsu's thresholding after Gaussian filtering
blur = cv.GaussianBlur(img,(5,5),0)
ret3,th3 = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)
# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,
          blur, 0, th3]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=127)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding",
          'Gaussian filtered Image','Histogram',"Otsu's Thresholding"]
for i in range(3):
    plt.subplot(3,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(3,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()'''
#************************平滑图像************************
#使用卷积核对图像进行滤波
'''img=cv.imread('2.jpg')
kernel=np.ones((5,5),np.float32)/25#卷积核
dst=cv.filter2D(img,-1,kernel)#cv.filter2D函数将卷积核与图像做卷积操作
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]),plt.yticks([])
plt.show()'''
#平均滤波器图像模糊
'''img = cv.imread('logo.jpg')
# blur = cv.blur(img,(5,5))
# blur = cv.GaussianBlur(img,(5,5),0)#高斯滤波器，高斯模糊对于从图像中去除高斯噪声非常有效。
# median=cv.medianBlur(img,5)#中值滤波器,提取内核区域下所有像素的中值，并将中心元素替换为该中值,去除椒盐噪声有效
blur = cv.bilateralFilter(img,9,75,75)#双边滤波，在去除噪声的同时保持边缘清晰锐利非常有效
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()'''
#***********************图像形态学转换：侵蚀，膨胀，打开，关闭等。**************************
#***********************侵蚀***********************
#思想：侵蚀了前景物体的边界（始终尝试使前景保持白色），卷积核内所有像素都为1时才为1，否则全为0，所有对边界产生侵蚀现象
'''import cv2 as cv
import numpy as np
img=plt.imread('j.png',0)
kernel=np.ones((5,5),np.uint8)
erosion=cv.erode(img,kernel,iterations=1)#iterations侵蚀倍数
dilation = cv.dilate(img,kernel,iterations = 1)#iterations膨胀倍数
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)#开运算：先腐蚀，再膨胀，可清除一些小东西(亮的)，放大局部低亮度的区域
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)#闭运算：先膨胀，再腐蚀，可清除小黑点
gradient = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)#形态学梯度：膨胀图与腐蚀图之差，提取物体边缘
tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)#原图像-开运算图，突出原图像中比周围亮的区域
blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)#黑帽：闭运算图-原图像，突出原图像中比周围暗的区域
plt.subplot(231)
plt.title('origin')
plt.imshow(img)
plt.subplot(232)
plt.title('erosion')
plt.imshow(erosion)
plt.subplot(233)
plt.title('dilation')
plt.imshow(dilation)
plt.subplot(234)
plt.title('opening')
plt.imshow(opening)
plt.subplot(235)
plt.title('closing')
plt.imshow(closing)
plt.subplot(236)
plt.title('blackhat')
plt.imshow(blackhat)
plt.show()'''
#*********************** 结构元素 ***********************
'''rect=cv.getStructuringElement(cv.MORPH_RECT,(5,5))#cv.getStructuringElement函数，只要传递核的形状和大小，就能得到想要的核
ellipse=cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))#椭圆
cross=cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))#十字
print(ellipse)'''










