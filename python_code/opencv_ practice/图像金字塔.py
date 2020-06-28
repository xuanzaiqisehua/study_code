#***************** 图像金字塔 *****************
#具有不同分辨率的图像集称为“图像金字塔”，包含两种：1、高斯金字塔 2、拉普拉斯金字塔
#1、高斯金字塔：删除高分辨率中连续的行、列
#2、拉普拉斯金字塔就像边缘图像
#**************** 使用图像金字塔与图像混合 ****************
'''
http://pages.cs.wisc.edu/~csverma/CS766_09/ImageMosaic/imagemosaic.html
金字塔的一个应用是图像混合。例如，在图像拼接中，您将需要将两个图像堆叠在一起，
但是由于图像之间的不连续性，它可能看起来不太好。在这种情况下，
图像与金字塔混合给你无缝混合没有留下太多的数据在图像中。
一个典型的例子就是混合两种水果，橘子和苹果。现在看到结果本身
主要由以下6个步骤组成：
1、加载苹果和橘子两张图片
2、找到两张图片的高斯金字塔（例子中使用级别6）
3、从高斯金字塔中查找他们的拉普拉斯金字塔
4、在每个级别的拉普拉斯金字塔级别中加入苹果的左半边和橘子的右半边
5、从联合图像金字塔中重建图像
'''
#官方例子运行失败
import cv2 as cv
import matplotlib.pylab as plt
'''import cv2 as cv
import numpy as np,sys
A=cv.imread('3.jpg')
B=cv.imread('3.jpg')
G=A.copy()#为A创建一个高斯金字塔
gpA=[G]
for i in range(6):
    G=cv.pyrDown(G)
    gpA.append(G)
G=B.copy()#为B创建一个高斯金字塔
gbB=[G]
for i in range(6):
    G=cv.pyrDown(G)
    gbB.append(G)
lpA=[gpA[5]]#为A生成一个拉普拉斯金字塔
for i in range(5,0,-1):#范围5-0，间隔为-1
    GE=cv.pyrUp(gpA[i])#cv.pyrUp：从一个低分辨率小尺寸的图像向下构建一个金子塔（尺寸变大，但分辨率不会)
    # print(GE.shape)
    # l=cv.subtract(gpA[i-1],GE)
    lpA.append(GE)
lpB=[gbB[5]]#为B生成一个拉普拉斯金字塔
for i in range(5,0,-1):
    GE=cv.pyrUp(gbB[i])#cv.pyrUp：从一个低分辨率小尺寸的图像向下构建一个金子塔（尺寸变大，但分辨率不会)
    l=cv.subtract(gbB[i-1],GE)
    lpB.append(GE)
#将每个级别的苹果和橘子的一般分别加到一起
LS=[]
for la,lb in zip(lpA,lpB):
    rows,cols,dpt=la.shape
    ls=np.hstack((la[:,0:int(cols/2)],lb[:,0:int(cols/2)]))#np.hstack():在水平方向上平铺
    LS.append(ls)
#重建
ls_=LS[0]
for i in range(1,5):
    ls_=cv.pyrUp(ls_)
    ls_=cv.add(ls_,LS[i])
#直接连接图像的每一半
rows,cols,dpt = A.shape
real = np.hstack((A[:,:cols/2],B[:,cols/2:]))
cv.imwrite('Pyramid_blending2.jpg',ls_)
cv.imwrite('Direct_blending.jpg',real)'''
'''import cv2 as cv
img=cv.imread('3.jpg',0)#读灰度图
up_img=cv.pyrUp(img)# 上采样操作
img_1=cv.pyrDown(img)# 下采样
img_2=cv.pyrDown(img_1)#再次下采样
cv.imshow('up_img',up_img)
cv.imshow('img',img)
cv.imshow('img_1',img_1)
cv.imshow('img_2',img_2)
cv.waitKey(0)
cv.destroyAllWindows()'''
#图像的下采样和上采样不是互逆的过程，如果下采样后需要恢复更高的分辨率，就需要拉普拉斯金字塔
'''img=cv.imread('2.jpg',0)
img1=cv.pyrDown(img)#下采样，高斯金字塔
_img1=cv.pyrDown(img1)
_img=cv.pyrUp(_img1)
img2=img1-_img #拉普拉斯金字塔
plt.subplot(1,3,1)
plt.imshow(img,cmap='gray')
plt.subplot(1,3,2)
plt.imshow(img1,cmap='gray')
plt.subplot(1,3,3)
plt.imshow(img2,cmap='gray')
plt.show()'''
# img = cv.imread('2.jpg', 0)
# img1 = cv.pyrDown(img)  # 高斯金字塔
# _img1 = cv.pyrDown(img1)
# _img = cv.pyrUp(_img1)
# img2 = img1 - _img  # 拉普拉斯金字塔
# cv.imshow('img1', img1)
# cv.imshow('img2', img2)
# cv.waitKey(0)
# cv.destroyAllWindows()
from matplotlib import pyplot as plt
import numpy as np




