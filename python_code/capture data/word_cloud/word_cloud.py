# import requests,json,re,time,os,jieba
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud,ImageColorGenerator
# from collections import Counter
# 最简单的词云
import matplotlib.pyplot as plt
from  wordcloud import  WordCloud
import jieba
text_from_file_with_apath=open('').read()
wordlist_after_jieba=jieba.cut(text_from_file_with_apath,cut_all=True)
wl_space_split=''.join(wordlist_after_jieba)
my_wordcloud=WordCloud().generate(wl_space_split)
plt.imshow(my_wordcloud)
plt.axis('off')
plt.show()





























