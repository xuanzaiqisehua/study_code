#1 抽取小王子前50条短评内容并计算评分(star)的平均值。提示：有的评论中不包含评分
import requests,re
import time
from bs4 import BeautifulSoup
count=0
s,count_s,count_del=0,0,0
lst_stars=[]
heard={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url='https://book.douban.com/subject/34870933/comments/'
while count<50:
    try:
        r=requests.get(url,headers=heard)
    except Exception as err:
        print('err')
        break
    soup=BeautifulSoup(r.text,'lxml')
    comments=soup.find_all('span','short')
    print(comments)
    pattern=re.compile('span class="user-stars allstar(.*?)rating')
    p=re.findall(pattern,r.text)
    print(p)
    for item in comments:
        count+=1
        if count>50:
            count_del+=1
        else:
             print(count,item.string)
    for star in p:
        lst_stars.append(int(star))
        # print(star)
    time.sleep(5)# 根据豆瓣中robots.txt的延迟请求
    # i=i+1
    for star in lst_stars[:-count_del]:#计算50个评论的评分
        s=s+int(star)
if count>=50:
    print(s//(len(lst_stars)-count_del))
