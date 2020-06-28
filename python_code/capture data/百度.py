import requests,os
# 百度搜索接口
'''keyword='python'
try:
    kv={'wd':keyword}
    r=requests.get('http://www.baidu.com/s',params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')
# 360 接口通过关键词爬取信息
keyword='python'
try:
    kv={'q':keyword}
    r=requests.get('http://www.so.com/s',params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print('爬取失败')'''
# 图片爬取全代码
'''url='http//:image,nationalgeographic.con.cn/2017/2011/0211/20170211061910157.jpg'#图片地址
root='D://pics//'
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)#content为字节格式,写入图片的时候需要用这个格式
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except:
    print('爬取失败')'''
# lxml 资料：https://www.cnblogs.com/wsg-python/articles/10182177.html
from lxml import etree
keyowrd='python'
try:
    kv={'word':keyowrd,
        'pn' : 0
        }
    r=requests.get('https://zhidao.baidu.com/search',params=kv)
    # print(r.request.url)
    # print(r.text)
except:
    print('爬取失败')
html=etree.HTML(r.text)
# link_html=html.xpath('//div[@class="list"]')#获取div节点下属性为class='list'的内容
# link_html=html.xpath('/div[contains(@class,"list")]//dl//dt//a/text()')#如果一个节点有多个属性是用contains获取
# link_html=html.xpath('//div[@class="list"]')#有多个属性时，如果通过一个属性不能获得节点，可以通过获取多个属性精确匹配，获取属性为class='list'的节点
# link_html1=html.xpath('//div[@class="list" and @id="wgt-list" and @data-log-area="list"]')
# print(link_html,link_html1)
links=html.xpath('//div[@class="list"]//dt[@class="dt mb-4 line"]/a/@href')#获取a标签下的属性为href的值，也就是提取了链接
next_url='https://zhidao.baidu.com/search?word=python&ie=gbk&site=-1&sites=0&date=0&pn=10'
t=requests.get(links[0])
t.encoding='utf-8'
# print(t.text)
t_html=etree.HTML(t.text)
text=t_html.xpath('//h1[@class="wgt-header-title-text"]/text()')
print(text)
exit()
text='''
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
        <tr class="h">
            <td class="l" width="374">职位名称</td>
            <td>职位类别</td>
            <td>人数</td>
            <td>地点</td>
            <td>发布时间</td>
        </tr>
        <tr class="even">
            <td class="l square"><a target="_blank" href="position_detail.php?id=33824&amp;keywords=python&amp;tid=87&amp;lid=2218">22989-金融云区块链高级研发工程师（深圳）</a></td>
            <td>技术类</td>
            <td>1</td>
            <td>深圳</td>
            <td>2017-11-25</td>
        </tr>'''
# html=etree.HTML(text)
#1 获取所有tr标签
'''trs=html.xpath('//tr')
for tr in trs :
    print(tr)
print(trs)'''
# 2 获取第2个tr标签
# tr=html.xpath('//tr[2]')[0]
# print(tr)
# 3 获取class等于even的tr标签
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr,encoding='utf-8').decode("utf-8"))
# 4. 获取所有a标签的href属性
# aList = html.xpath("//a/@href")
# for a in aList:
#     print("http://hr.tencent.com/"+a)
# 5. 获取所有的职位信息（纯文本）
'''trs = html.xpath("//tr[position()>1]")
positions = []
for tr in trs:
    # 在某个标签下，再执行xpath函数，获取这个标签下的子孙元素
    # 那么应该在//之前加一个点，代表是在当前元素下获取
    href = tr.xpath(".//a/@href")[0]
    fullurl = 'http://hr.tencent.com/' + href
    title = tr.xpath("./td[1]//text()")[0]
    category = tr.xpath("./td[2]/text()")[0]
    nums = tr.xpath("./td[3]/text()")[0]
    address = tr.xpath("./td[4]/text()")[0]
    pubtime = tr.xpath("./td[5]/text()")[0]

    position = {
        'url': fullurl,
        'title': title,
        'category': category,
        'nums': nums,
        'address': address,
        'pubtime': pubtime
    }
    positions.append(position)
print(positions)'''














