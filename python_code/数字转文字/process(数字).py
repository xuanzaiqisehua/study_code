import re
common_used_numerals_tmp = {'零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9,
                            '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000}
common_used_numerals = {}
for key in common_used_numerals_tmp:
    common_used_numerals[key] = common_used_numerals_tmp[key]
def chinese2digits(uchars_chinese):
    total = 0
    r = 1  # 表示单位：个十百千...
    for i in range(len(uchars_chinese) - 1, -1, -1):
        val = common_used_numerals.get(uchars_chinese[i])
        if val >= 10 and i == 0:  # 应对 十三 十四 十*之类
            if val > r:
                r = val
                total = total + val
            else:
                r = r * val
                # total =total + r * x
        elif val >= 10:
            if val > r:
                r = val
            else:
                r = r * val
        else:
            total = total + r * val
    return total


num_str_start_symbol = ['一', '二', '两', '三', '四', '五', '六', '七', '八', '九',
                        '十']
more_num_str_symbol = ['零', '一', '二', '两', '三', '四', '五', '六', '七', '八', '九', '十', '百', '千', '万', '亿']


def changeChineseNumToArab(oriStr):
    lenStr = len(oriStr)
    aProStr = ''
    if lenStr == 0:
        return aProStr

    hasNumStart = False
    numberStr = ''
    for idx in range(lenStr):
        if oriStr[idx] in num_str_start_symbol:
            if not hasNumStart:
                hasNumStart = True

            numberStr += oriStr[idx]
        else:
            if hasNumStart:
                if oriStr[idx] in more_num_str_symbol:
                    numberStr += oriStr[idx]
                    continue
                else:
                    numResult = str(chinese2digits(numberStr))
                    numberStr = ''
                    hasNumStart = False
                    aProStr += numResult

            aProStr += oriStr[idx]
            pass

    if len(numberStr) > 0:
        resultNum = chinese2digits(numberStr)
        aProStr += str(resultNum)

    return aProStr


#************************************************************************************************

filename1='分词词性训练集-总-20w句-匹配(1).txt'
filename2='concat.txt'
with open(filename1,'r',encoding='utf-8') as r:
    lines1=r.readlines()
with open(filename2,'r',encoding='utf-8') as r:
    lines2=r.readlines()

dic1={}
for line in lines1:
    # dig = re.findall('[0-9]', line)# 查找汉字
    dig=re.findall('[0-9]{1,}',line.split('\t')[1])#含数字句子
    if dig!=[]:
        k_str=line.split('\t')[1]
        k_sentence=re.findall('[\u4e00-\u9fa5]',changeChineseNumToArab(k_str))
        k_sentence=''.join(k_sentence)
        if k_sentence not in dic1:
            dic1[k_sentence]=line
    else:
        k_sentence=re.findall('[\u4e00-\u9fa5]',line)
        if k_sentence!=[]:
            k_sentence=''.join(k_sentence)
            # print(k_sentence)
            if k_sentence not in dic1:
                dic1[k_sentence]=line
dic2={}
for line in lines2:
    # dig=re.findall('[0-9]',line)# 查找汉字
    dig = re.findall('[0-9]{1,}', line.split('\t')[1])#含数字句子
    if dig != []:
        k_str = line.split('\t')[1]
        k_sentence = re.findall('[\u4e00-\u9fa5]', changeChineseNumToArab(k_str))
        k_sentence = ''.join(k_sentence)
        if k_sentence not in dic2:
            dic2[k_sentence] = line
    else:
        k_sentence=re.findall('[\u4e00-\u9fa5]',line)
        if k_sentence!=[]:
            k_sentence=''.join(k_sentence)
            if k_sentence not in dic2:
                dic2[k_sentence]=line

write_file1='similar_分词词性训练集总.txt'
write_file2='similar_35万韵律训练集分领域总.txt'

for k,v in dic1.items():
    if k in dic2.keys():
        with open(write_file1,'a',encoding='utf-8') as w:
            w.write(v)
        with open(write_file2,'a',encoding='utf-8') as w:
            w.write(dic2[k])
