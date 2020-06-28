import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#******************** Sobel、Laplacia 边缘检测 ********************
'''img=cv.imread('2.jpg',0)
laplacian=cv.Laplacian(img,cv.CV_64F)#64F代表每一个像素点元素占64位浮点数
sobelx=cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
sobely=cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
plt.title('Oridinal'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray')
plt.title('Laplacian'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap='gray')
plt.title('sobelx'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap='gray')
plt.title('sobely'),plt.xticks([]),plt.yticks([])
plt.show()'''
'''
但这有一个小问题。黑色到白色的过渡被视为正斜率（具有正值），而白色到黑色的过渡被视为负斜率（具有负值）。因此，当您将数据转换为np.uint8时，所有负斜率均​​设为零。简而言之，您会错过这一优势。
如果要检测两个边缘，更好的选择是将输出数据类型保留为更高的形式，例如cv.CV_16S，cv.CV_64F等，取其绝对值，然后转换回cv.CV_8U。下面的代码演示了水平Sobel滤波器的处理过程以及结果的差异。
'''

#******************** 如果要检测两个边缘，先将其输出为更高精度然后再转回低精度 ********************
'''img = cv.imread('edge.PNG',0)
# Output dtype = cv.CV_8U
sobelx8u = cv.Sobel(img,cv.CV_8U,1,0,ksize=5)
# Output dtype = cv.CV_64F. Then take its absolute and convert to cv.CV_8U
sobelx64f = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)
plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])
plt.show()'''

#******************** canny 边缘检测 ********************
#步骤：1、降噪 2、查找图像的强度梯度 3、非最大抑制 4、滞后阈值法
img=cv.imread('2.jpg',0)
edges=cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Original Image'),plt.xticks([]),plt.yticks([])#plt.xticks([]),plt.yticks([])不显示坐标轴
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Edge Image'),plt.xticks([]),plt.yticks([])
plt.show()











