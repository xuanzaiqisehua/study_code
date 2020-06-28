# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 11:07
# @Author  : Gepenghua
# @FileName: Trackbar_study.py
# @Email : 578517264@qq.com
# @Software: PyCharm
# @github    ：https://github.com/xuanzaiqisehua?tab=repositories
import numpy as np
import cv2
def nothing(x):
    pass
img=np.zeros((300,512,3),np.uint8)
# img=cv2.imread('1.jpg')
# print(img)
cv2.namedWindow('image')
#创建颜色选择
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
#定义一个开关功能
switch='0 : OFF\n1:ON'
cv2.createTrackbar(switch,'image',0,1,nothing)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(0)&0xFF
    if k==27:
        break
    #获取颜色模式目前的位置
    r=cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G', 'image')
    b=cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch, 'image')
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]
cv2.destroyAllWindows()













