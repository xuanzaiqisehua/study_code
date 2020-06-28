import requests
from bs4 import BeautifulSoup
import os
'''人民日报网页内容包括日期，每一个日期有版面目录，每一版有好多标题，点开标题里面有文本内容'''
# 定义一个获取网页内容的函数
def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return  r.text
    except:
        print('爬取异常')
def getCataloguelink(year,month,day): #通过给定的参数：年月日获取某一天的新闻内容
    url = 'http://paper.people.com.cn/rmrb/html/' + year + '-' + month + '/' + day + '/nbs.D110000renmrb_02.htm'
    html=getHTML(url)
    soup=BeautifulSoup(html,'html.parser')# 获取版面目录
    links=soup.find_all('div','right_title-name')
    linklist=[]
    for page in links:
        cataloguelink=page.a['href']
        linklist.append(cataloguelink)
    return linklist # 获得一个目录链接列表
def Titlelist(year,month,day,pageurl):# 获取每个版本的的标题链接
    html=getHTML(pageurl)
    soup=BeautifulSoup(html,'html.parser')
    titlelist=soup.find('div',attrs = {'id': 'titleList'}).ul.find_all('li')
    titlelink=[]
    for title in titlelist:
        templist=title.find_all('a')
        for temp in templist:
            link = temp['href']
            if 'nw.D110000renmrb' in link:
                url = 'http://paper.people.com.cn/rmrb/html/' + year + '-' + month + '/' + day + '/' + link
                titlelink.append(url)
    return titlelink
# 给定一个标题链接提取其中的标题和内容
def getContent(url):
    html=getHTML(url)
    soup=BeautifulSoup(html,'html.parser')
    title = soup.h1
    contents=soup.find('div',attrs={'id':'articleContent'}).find_all('p')
    content=''
    for p in contents:
        content+=p.text+'\n'
    # print(title+'\n'+content)
    return title.text+content
def savaFile(content,path,filename):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path+filename,'w',encoding='utf-8') as f:
        f.write(content)
# 将所有函数整合到一起
def download(year,month,day,output):
    pagelinks=getCataloguelink(year,month,day)# 通过给定的年月日获得某一日期的目录链接
    for pagelink in pagelinks:
     pageurl ='http://paper.people.com.cn/rmrb/html/' + year + '-' + month + '/' + day +'/'+ pagelink
     titlelinks=Titlelist(year, month, day, pageurl) # 调用函数获得某个版面的标题链接
     for titlelink in titlelinks:# 遍历标题链接获得某一具体标题链接
        content=getContent(titlelink) # 调用函数获得内容和标题
        titleNo=titlelink.split('_')[2].split('-')[0]
        pageNo= titlelink.split('_')[2].split('-')[1].split('.')[0]
        filename=year+month+day+pageNo+titleNo+'.txt'
        path=output + '/' + year + month + day + '/'
        savaFile(content,path,filename)
if __name__=='__main__':
    newdata=input('请输入要爬取的日期（格式如 20200122）')
    year=newdata[0:4]
    month=newdata[4:6]
    day=newdata[6:8]
    output='./out'
    download(year,month,day,output)
    print("爬取完成：" + year + month + day)
















