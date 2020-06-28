#爬取一段时间内的新闻热点进行分析，从新闻标题中获得热点词并绘制词云
#ajax技术渲染的网页应该如何抓取数据（ajax动态生成网页，不需要加载整个页面就可以更新部分内容）
#比如新浪滚动新闻https://news.sina.com.cn/roll/#pageid=153&lid=2509&k=&num=50&page=1，
#动态生成网页-查看源代码会发现并没有刚刚看到的新闻标题-这时候需要使用开发者工具查看-(Network-All)
# 然后清除日志-手动刷新产生的请求地址即为此时页面的请求地址
import requests
regex=requests.get('https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=' \
                   '0.017065019492790157&callback=jQuery1112031010181218575994_1580351355294&_=1580351355318')
#输出标题内容需要编码为utf-8然后解码才能变为中文,将unicode的内存编码值进行存储，读取文件时再反向转回来
#总结如果遇到编码问题，先检查响应内容text是什么类型，如果type（regex.text）is bytes那么：text.decode('unicode-escape'）;
# 如果type(text)isbytes那么:text.encode('utf-8').decode('unicode-escape')或者text.encode('latin-1').decode('unicode-escape')
print(type(regex.text))
r=regex.text.encode('utf-8').decode('unicode-escape')
print(r)
