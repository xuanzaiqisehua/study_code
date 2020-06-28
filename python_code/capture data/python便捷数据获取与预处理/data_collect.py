# 数据处理的四个步骤：数据收集、数据探索与预处理、数据分析与挖掘、结果评价与呈现
# 读取excel表格数据并进行数据处理
'''import pandas as pd
data=pd.read_excel('data.xlsx')#读取excel文件
data['sum']=data['Python']+data['Math']
data.to_excel('save_data.xlsx','Scores')#保存excel文件
print(data)'''
# 从网页抓取源代码获取数据
# 抓取道指成分股份数据并将30家公司的代码、公司名称和最近一次成交价放到一个列表中，并将其转为二维列表
'''import requests,re
import pandas as pd
def search_list():
    try:
        data=requests.get('http://money.cnn.com/data/dow30')
    except requests.exceptions.ConnectionError:
        print('连接超时')
    search_pattern=re.compile('class="wsod_symbol">(.*?)</a>.*<span.*>(.*?)</span></td>\s+.*class="wsod_stream">(.*?)</span></td>')
    # 正则表达式规则，要寻找某个字符，需要把这个字符前面和后面的都找见，这个字符用.*?(通配符)表示
    dji_list_in_text=re.findall(search_pattern,data.text)
    dji_list=[]
    for item in dji_list_in_text:
        dji_list.append({'code':item[0],'name':item[1],'price':float(item[2])})
    return dji_list
if __name__ == '__main__':
    result=search_list()
    dji_frame=pd.DataFrame(result)
    print(dji_frame)'''
# 从美国股票运通公司获取股票代码为AXP的历史数据
# import requests,re
# import pandas as pd
#
# history_list=requests.get('http://finance.yahoo.com/quote/%s/history?p=%s')
# history_data=re.findall('"HistoricalPriceStore":')

# print(history_data.text)
# 代码不是很理解
'''import requests
import re
import json
import pandas as pd
def retrieve_quotes_historical(stock_code):
    quotes = []
    url = 'https://finance.yahoo.com/quote/%s/history?p=%s' % (stock_code, stock_code)
    try:
        r = requests.get(url)
    except ConnectionError as err:
        print(err)
    m = re.findall('"HistoricalPriceStore":{"prices":(.*?),"isPending"', r.text)#这里不清楚
    if m:
        quotes = json.loads(m[0])  # m = ['[{...},{...},...]']#json格式代码
        quotes = quotes[::-1]# 使用逆序排序让最新数据排在最前面
    return [item for item in quotes if 'type' not in item]

quotes = retrieve_quotes_historical('AXP')
quotesdf_ori = pd.DataFrame(quotes)
quotesdf = quotesdf_ori.drop(['adjclose'], axis=1)# drop删除第一列数据
print(quotesdf)'''
# 直接下载数据：简单方便并且快速获得财经网站上公司股票历史数据CSV格式或者json格式
#通过应用程序接口API获得历史数据，利用API获取数据更加方便，因为网页源代码还需要解析，API获取数据为清洗过的数据
# 比如利用pandas_ataader.data模块中的DataReader函数从stooq网站获取美国运通公司的近几年历史数据
# 有些网站提供API接口，如果网站有API接口获取数据时优先考虑用API接口获取数据
# import pandas_datareader.data as web
# f=web.DataReader('AXP','stoop')
# f.head(5)# 获取前五行数据










