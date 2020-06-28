# -*- coding: utf-8 -*-
# @Author  : Gepenghua
# @FileName: read.py
# @Software: PyCharm
# @github    ：https://github.com/xuanzaiqisehua?tab=repositories
# @function  ：opencv入门
#参考：https://www.cnblogs.com/silence-cho/p/10926248.html
#  https://blog.csdn.net/wang342626/article/details/90765440
# 官方使用：https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html
import cv2,os
#****************读图片****************
'''cv2.namedWindow('img1',cv2.WINDOW_AUTOSIZE)
path='1.jpg'# 名字尽量不要为中文
img=cv2.imread(path,-1)#1为彩色,0为灰度,-1为不变
#创建窗口，显示图片
# cv2.namedWindow('新建窗口名',flag)
# 创建一个窗口名叫image
# flag=cv2.WINDOW_AUTOSIZE时候就自动适应大小这是默认的
# flag=cv2.WINDOW_NORMAL就是图片自适应窗口大小
cv2.imshow('img1',img)
key=cv2.waitKey(0)&0xFF#参数0表示一直等待键盘操作
#如果你用的是 64 位系统，你需要将 k = cv2.waitKey(0) 这行改成
# k = cv2.waitKey(0)&0xFF
if key==27:#如果按下esc键，退出
    cv2.destroyAllWindows()
elif key==ord('s') :#如果按下s键，保存图片
    cv2.imwrite('2.png',img)
    cv2.destroyAllWindows()#不加参数是关闭所有窗口，加窗口名是关闭指定窗口'''
'''#***********************保存图片，保存视频*********************
cv2.imwrite('2.png',img)#保存图片
cv2.imwrite('1.jpg',frame)#保存视频'''
#******************使用plt
# 使用opencv加载的是BGR模式，但matplotlib是GRB模式，如果彩色图像被opencv读取那它将不会被matplotlib修正，所有读取出来会不一样
'''from matplotlib import pyplot as plt
# img=cv2.imread('1.jpg',1)
imge = plt.imread('1.jpg')
plt.imshow(imge,cmap='gray',interpolation='bicubic')
# plt.imshow(img,cmap='gray',interpolation='bicubic')#cmap颜色映射取值，interpolation为插值运算
plt.show()'''
#*****************使用摄像头捕捉视频
import numpy as np
#（1）打开摄像头
'''cap=cv2.VideoCapture(0)
while(True):
    #一帧一帧捕获视频
    ret,frame=cap.read()
    cv2.imshow("frame",frame)
    #q键退出
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()'''

# （2）打开摄像头
'''cap = cv2.VideoCapture(0)  # 表示第几个摄像头
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('1.avi',fourcc,20.0,(640,480)) # 视频保存路径
while cap.isOpened(): # 如果摄像头开着的话
    ret,frame = cap.read() # 返回的ret==true表示获取帧率成功
    if ret==True:
        # frame = cv2.flip(frame,0) # 旋转颠倒过来
        out.write(frame)
        cv2.imshow('标题：正在录制...按q退出并且保存到D:/1.avi',frame)
        if cv2.waitKey(1)&0xFF==ord('q'): # 按q退出
            break
    else:
        break
cap.release() # 释放视频
out.release()
cv2.destroyAllWindows()'''
#***************读取视频文件
'''cap=cv2.VideoCapture('1.mov')
out='output/'
if not os.path.exists(out):
    os.mkdir(out)
i=0
while True:
    ret,frame=cap.read() #ret返回true表示获取帧率成功
    if ret ==True:
        title="标题"
        cv2.imshow('show', frame)
        key=cv2.waitKey(1)&0xFF#0xff补充到16位，就是高位补0,操作系统为64位
        if key==ord('q'):
            break
        elif key==ord('p') :#按p截图保存
           cv2.imwrite(out+str(i)+'.jpg',frame)
           i+=1
    else:
        break
cap.release()#释放视频
cv2.destroyAllWindows()'''
#**********************在图片上绘画
import numpy as np
# 创建黑色背景：长1280，宽720
#画直线
# img=np.zeros((720,1280),np.uint8)
'''point1=(0,0)
point2=(500,500)
color=(255,0,0)
width=5#线条粗细
cv2.line(img,point1,point2,color,width)
cv2.imshow('title',img)
cv2.waitKey(0)'''
#画矩形
'''cv2.rectangle(img,(5,5),(100,100),(255,0,0),cv2.FILLED)#实心矩形
cv2.imshow('rectangle1',img)
cv2.waitKey(0)
cv2.rectangle(img,(5,5),(100,100),(255,0,0),-1)#实心矩形
cv2.imshow('rectangle2',img)
cv2.rectangle(img,(5,5),(100,100),(255,0,0),5)#圆角矩形
cv2.imshow('rectangle3',img)
cv2.waitKey(0)'''
#画圆
'''point1=(360,300)
color=(255,0,0)
# cv2.circle(img,point1,50,color,-1)#圆心，半径
cv2.ellipse(img,point1,(100,50),0,0,180,255,-1)#椭圆，圆心坐标，长轴，短轴，开始角度，结束角
cv2.imshow('circle',img)
cv2.waitKey(0)'''
#绘制文字
'''color=(255,0,0)
point2=(100,100)#文字左下位置的坐标
font=cv2.FONT_HERSHEY_SIMPLEX#设置字体
cv2.putText(img,'english word',point2,font,4,color,2)
cv2.imshow('circle',img)
cv2.waitKey(0)
help(cv2.putText)'''
#绘制文字
'''point2=(100,100)
color=(255,0,0)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'english word',point2,font,4,color,2) #绘制文字
winname = 'example'
cv2.namedWindow(winname) # 创建窗口
cv2.imshow(winname, img)
cv2.waitKey(0)
cv2.destroyWindow(winname)'''
#鼠标点击画圆
'''def func(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:#双击
        cv2.circle(img,(x,y),100,(255,0,0),-1)
    elif event==cv2.EVENT_LBUTTONDOWN:#鼠标放下
        cv2.circle(img,(x,y),100,(255,0,0),-1)
#创建图像与窗口
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
#将窗口与回调函数绑定
cv2.setMouseCallback('image',func)
while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20)&0xFF==27:#按esc退出
        break
# cv2.destroyAllWindows()#关闭所有窗口
cv2.destroyWindow('image')#关闭指定窗口'''
#******************查看cv2中鼠标事件
'''import cv2
events=[i for i in dir(cv2) if 'EVENT' in i]
print(events)'''
#*****************鼠标拖动画圆
# 鼠标事件参考https://blog.csdn.net/qq_22033759/article/details/48415613
#当鼠标按下变为True

'''drawing=False
#如果mode为true绘制矩形，按下m绘制曲线
mode=True
ix,iy=-1,-1
#创建回调函数
def func(event,x,y,flags,param):
    global ix,iy,drawing,mode
    # 当按下左键，返回起始坐标
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    #当鼠标左键按下并移动是绘制图形，event可以查看移动，flag查看是否按下
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:#鼠标左键按下拖拽EVENT_FLAG_LBUTTON
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                #绘制圆圈，小圆点连在一起成为曲线，3代表画笔的粗细
                cv2.circle(img,(x,y),3,(0,0,255),-1)
                # 起始点为圆心，起点到终点为半径的圆
                # r = int(np.sqrt((x - ix) ** 2 + (y - iy) ** 2))
                # cv2.circle(img, (x, y), r, (0, 0, 255), -1)
                #当鼠标松开，就开始绘画
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,100,0),-1)
        else:
            cv2.circle(img, (x, y), 3, (0, 0, 100), -1)
            # 起始点为圆心，起点到终点为半径的圆
            # r = int(np.sqrt((x - ix) ** 2 + (y - iy) ** 2))
            # cv2.circle(img, (x, y), r, (0, 0, 255), -1)
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',func)#新建图像窗口并将窗口与回调函数绑定
while(1):#while语句的原型是while(表达式)语句，当表达式为非0值时，执行while语句中的嵌套语句，while(1)其中1代表一个常量表达式，它永远不会等于0。循环会一直执行下去
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==ord('m'):#按m切换模式，true表示画矩形，flase表示画曲线
        mode=not mode
    elif k==27:#按esc退出
        break'''




