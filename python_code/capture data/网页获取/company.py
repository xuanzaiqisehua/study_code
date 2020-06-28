# 2 在http://money.cnn.com/data/dow30/
# 抓取道指成分股份数据并将30家公司的代码、公司名称和最近一次成交价放到一个列表中
import requests
import re
def retrieve_dji_list():
    r=requests.get('http://money.cnn.com/data/dow30/')
    search_pattern=re.compile('class="wsod_symbol">(.*?)</a>.*?<span.*?>(.*?)</span></td>\s+.*? class="wsod_stream">(.*?)</span>')
    dji_list_in_text=re.findall(search_pattern,r.text)
    return dji_list_in_text
dji_list=retrieve_dji_list()
print(dji_list)
# 3 爬取网页(http://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1)上的数据
# (包括TEAMS and TOTAL,WON,LOST of MATCHES)
#提示：处理时可以将每个TEAM的相关数据按组解析出来，但是由于包含这4项信息的源代码分在多行并且有多个空格，
# 处理时将正则表达式把空白字符表达出来用\s+(可表示多个空白字符，包括换行符和空格)
# import requests,re
# def crawler(url):
#     try:
#         r=requests.get(url)
#     except requests.exceptions.RequestException as err:
#         return err
#     pattern=re.compile('href="/en/vnl/2018/women/teams/(.*?)">(.*?)</a></figcaption>\s+ </figure>\s+</td>\s+<td>(.*?)</td>\s+<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>')
#     p=re.findall(pattern,r.text)
#     return p
# if __name__=='__main__':
#     ad='http://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1'
#     results=crawler(ad)
#     print(results)






































