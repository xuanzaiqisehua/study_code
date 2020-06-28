import requests,os,datetime
from bs4 import BeautifulSoup
start = datetime.datetime.now()
def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        print('产生异常')
# 获取分类链接列表
def  getCategory():
     url='http://www.ruanyifeng.com/blog/weekly/'
     html=getHTML(url)
     soup=BeautifulSoup(html,'html.parser')
     Categorylist = soup.find('div',attrs={'id':'beta-inner'}).find_all('ul','module-list')
     Categorylinks = []
     for ul in Categorylist:
         li = ul.find_all('li')
         for link in li:
             Categorylink = link.a['href']
             Categorylinks.append(Categorylink)
     return Categorylinks
def getArticlelist(html):
    soup=BeautifulSoup(html,'html.parser')
    Articlelist=soup.find('div',attrs={'id':'alpha-inner'}).find_all('ul','module-list')
    Articlelinks=[]
    for ul in Articlelist:
        li=ul.find_all('li')
        for link in li:
            Articlelink=link.a['href']
            Articlelinks.append(Articlelink)
    return  Articlelinks
def getContent(url):
    html=getHTML(url)
    soup=BeautifulSoup(html,'html.parser')
    title=soup.find('article','hentry').h1.text
    contents=soup.find('div',attrs={'id':'main-content'}).find_all('p')
    text=''
    for content in contents:
        text+=content.text+'\n'
    return title+'\n'+text
def savaFile(content,path,filename):
    if not os.path.exists(path):
       os.makedirs(path)
    with open(path+filename,'w',encoding='utf-8') as f:
        f.write(content)
def main(url,out):
    Categorylinks=getCategory()
    for i in range(len(Categorylinks)):
        Categorylink=Categorylinks[i]
        categoryname=Categorylink.split('/')[4]
        print(categoryname)
        categoryurl = url+ categoryname + '/'
        html=getHTML(categoryurl)
        Articlelinks=getArticlelist(html)
        print(Articlelinks)
        count=0
        path=out+categoryname+'/'
        for j in range(2):
            Articlelink=Articlelinks[j]
            count+=1
            text=getContent(Articlelink)
            filename=Articlelink.split('/')[-1].split('.')[0]+'.txt'
            savaFile(text, path, filename)
            print('成功保存{}篇文章'.format(count))
data='weekly'
out='./output/'
url='http://www.ruanyifeng.com/blog/'
main(url,out)
end = datetime.datetime.now()
print(end-start)