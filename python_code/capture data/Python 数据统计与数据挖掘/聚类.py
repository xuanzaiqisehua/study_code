'''聚类：K均值算法，执行流程：（1）选择K个对象作为初始的聚类中心，通过（均方差）计算距离确定每个点的聚类中心（2）计算新聚类的聚类中心'''
# 根据成绩寻找潜在的学霸,已知大萌为学霸
'''import numpy as np
from scipy.cluster.vq import vq,kmeans,whiten
list1=[88.0,74.0,96.0,85.0]
list2=[92.0,99.0,95.0,94.0]
list3=[91.0,87.0,99.0,95.0]
list4=[78.0,99.0,97.0,81.0]
list5=[88.0,78.0,98.0,84.0]
list6=[100.0,95.0,100.0,92.0]# 大萌
data=np.array([list1,list2,list3,list4,list5,list6])
whiten=whiten(data)# whiten算出各列元素的标准差
centroids,_=kmeans(whiten,3) # 2表示两类：学霸和非学霸，返回元组，但我们只需要第一个返回结果：聚类中心数组
result,_=vq(whiten,centroids)# vq可以对每一类人进行归类，然后得到结果
print(result)'''
'''import numpy as np
from sklearn.cluster import KMeans
list1=[88.0,74.0,96.0,85.0]
list2=[92.0,99.0,95.0,94.0]
list3=[91.0,87.0,99.0,95.0]
list4=[78.0,99.0,97.0,81.0]
list5=[88.0,78.0,98.0,84.0]
list6=[100.0,95.0,100.0,92.0]# 大萌
X=np.array([list1,list2,list3,list4,list5,list6])
kmeans=KMeans(n_clusters=2).fit(X)#fit()是一个学习过程
pred=kmeans.predict(X)# predict()根据聚类结果确定所属类别
print(pred)'''
#************************* 使用支持向量机算法对数据进行分类********************
'''from sklearn import datasets
from sklearn import svm
clf=svm.SVC(gamma=0.001,C=100.)
digits=datasets.load_digits()
clf.fit(digits.data[:-1],digits.target[:-1])
result=clf.predict(digits.data[-1])
print(result)'''
# 基于10只道指成分股近一年来相邻两天的收盘涨跌数据规律对它们进行聚类
''' 模型的选择和评估1
 对于比较复杂的数据使用机器学习方法时，首先需要选择合适的模型比如分类或者聚类模型，然后需要确定参数值，
 除了需要经验调参外，还有一些方法选择参数，比如K均值中的K值选择用“肘方法”（SSE）'''
'''from sklearn import neighbors,datasets
iris=datasets.load_iris()
knn=neighbors.KNeighborsClassifier()
knn.fit(iris.data,iris.target)# 从已有数据中学习
result=knn.predict(([[5.0,3.0,5.0,2.0]]))# 利用分类模型进行未知数据的预测（确定标签）
print(result)'''
# 利用K-means 聚类算法进行聚类
'''from sklearn import cluster,datasets
iris=datasets.load_iris()
kmeans=cluster.KMeans(n_clusters=3).fit(iris.data)
pred=kmeans.predict(iris.data) # 确定数据类别
# 比较算法正确率
for label in pred:
    print(label,end='')# 打印预测出的各条数据的标签
print('\n')
for label in iris.target:
    print(label,end='')'''#  打印原始标注好的正确标签
# 进一步可以利用其它算法实现类似功能，例如使用常用的SVM(支持向量机)分类算法对数据进行分类：
'''from sklearn import svm,datasets
iris=datasets.load_iris()
svc=svm.LinearSVC()
svc.fit(iris.data,iris.target)# 学习
result=svc.predict([[5.0,3.0,5.0,2.0]])#   预测
print(result)'''
# 对一组数据进行傅里叶变换
'''import scipy as sp
import matplotlib.pyplot as plt
listA=sp.ones(500)
listA[100:300]=-1
f=sp.fft(listA)
plt.plot(f)
plt.show()'''
# 常用Python图像处理库:Pillow(PIL);OpenCV,SKimage
'''from PIL import Image
im1=Image.open('1.jpg')
print(im1.size,im1.format,im1.mode)
Image.open('1.jpg').save('2.jpg')
im2=Image.open('2.jpg')
size=(288,180)
im2.thumbnail(size)
out=im2.rotate(45)
im1.paste(out,(50,50))
im1.show()
# 生物信息学库：Biopython'''
'''学习使用Python对音频信号进行简单的处理'''
#**************************理工类问题**************************
'''import scipy.io.wavfile
import wave
import matplotlib.pyplot
import matplotlib.pylab
import urllib.request
import numpy
response=urllib.request.urlopen('http://www.nch.com.au/acm/11k16bitpcm.wav')
Wav_FILE='english.wav'
file=open(Wav_FILE,'wb+')
file.write(response.read())
file.close()
wavefile=wave.open(Wav_FILE,'r')
params=wavefile.getparams()
nchannels,sample_width,framerate,numframes=params[:4]
sample_rate,data=scipy.io.wavfile.read(Wav_FILE)
matplotlib.pyplot.subplot(2,1,1)
matplotlib.pyplot.title('Original')
matplotlib.pyplot.plot(data)
# matplotlib.pyplot.plot.show()
newdata=data*0.2
newdata=newdata.astype(numpy.int16)
scipy.io.wavfile.write('silent.wav',sample_rate,newdata)
matplotlib.pyplot.subplot(2,1,2)
matplotlib.pyplot.title('Quiet')
matplotlib.pyplot.plot(newdata)
matplotlib.pyplot.show()
# result=matplotlib.pylab.specgram(newdata,NFFT=1024,Fs=sample_rate,novelap=900)
# matplotlib.pyplot.show()'''
#**************************人文社科类问题**************************
# 以自然语言语料库NLTK为例
'''from nltk.corpus import gutenberg
allwords=gutenberg.words('shakespeare-hamlet.txt')# 古藤堡项目中的书籍《哈姆雷特》
print(len(allwords))# 计算这本书中所有的单词数
len(set(allwords))#  计算不重复的字符数
allwords.count('Hamlet')# 计算单词Hamlet出现次数
A=set(allwords)
longwords=[w for w in A if len(w)>12] # 计算单词长度大于12的所有不重复单词
print(sorted(longwords))#  排序后输出
from nltk.corpus import inaugural
fd3=FreqDist([s for s in inaugural.words()])
print(fd3.freq('freedom'))# 计算freedom出现时频率'''






























