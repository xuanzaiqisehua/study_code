'''from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import matplotlib.pyplot as plt
import numpy as np
#绘制3D玫瑰
fig = plt.figure()
ax = fig.gca(projection='3d')
[x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 17 * np.pi - 2 * np.pi)
p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
u = 1 - (1 - np.mod(3.6 * t, 2 * np.pi) / np.pi) ** 4 / 2
y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
r = u * (x * np.sin(p) + y * np.cos(p))
h = u * (x * np.cos(p) - y * np.sin(p))
surf = ax.plot_surface(r * np.cos(t), r * np.sin(t), h, rstride=1, cstride=1,
                       cmap=cm.gist_rainbow_r, linewidth=0, antialiased=True)
plt.show()'''
from matplotlib import pyplot as plt#用来绘制图形
import numpy as np #用来处理数据
from mpl_toolkits.mplot3d import Axes3D#用来给出3D坐标系
figure=plt.figure()#打开画布
axes=Axes3D(figure)#画出3维坐标系

'''#限定x和y的画图范围
x=np.arange(-10,10,0.25)
y=np.arange(-10,10,0.25)
#限定图形的样式维网格样式：
x,y=np.meshgrid(x,y)
#给出二元函数的解析式
z=np.cos(((x**2)+y**2)**(1/6))
#绘制曲面，采用彩虹色着色
axes.plot_surface(x,y,z,rstride = 1, cstride = 1,cmap='rainbow')#rstride, cstride分别为行间隔，列间隔
#绘制3D图像的投影,默认投影在z轴，可以设置x，y轴,offset为投影偏移量
axes.contour(x,y,z,zdir='z',offset=-1,cmap='rainbow')
plt.show()#图形可视化'''
#二维数组转3维
import numpy as np
import pandas as pd
import os
import scipy.ndimage
import matplotlib.pyplot as plt
from skimage import measure, morphology
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def plot_3d(image, threshold=-300):
    # Position the scan upright,
    # so the head of the patient would be at the top facing the camera
    p = image.transpose(2, 1, 0)
    p = p[:, :, ::-1]

    verts, faces = measure.marching_cubes(p, threshold)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Fancy indexing: `verts[faces]` to generate a collection of triangles
    mesh = Poly3DCollection(verts[faces], alpha=0.1)
    face_color = [0.5, 0.5, 1]
    mesh.set_facecolor(face_color)
    ax.add_collection3d(mesh)

    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")
    ax.set_zlabel("z-axis")

    ax.set_xlim(0, p.shape[0])  # a = 6 (times two for 2nd ellipsoid)
    ax.set_ylim(0, p.shape[1])  # b = 10
    ax.set_zlim(0, p.shape[2])  # c = 16

    plt.show()


















