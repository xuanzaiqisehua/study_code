import re

def get_elemento_one_hot(line):
    line=line.strip()
    line=re.sub('[^\s\w-]','',line).strip()
    word_list=re.split('\s+',line.lower())
    '''vowel = ['uai', 'uei', 'uiu', 'uão', 'uem', 'uõe',  # 三重元音
             'ai', 'au', 'ei', 'éi', 'eu', 'éu', 'iu', 'oi', 'ói', 'ou', 'ui', 'am',
             'an', 'em', 'en', 'im', 'in', 'om', 'on', 'um', 'un', 'ão', 'ãe', 'õe',  # 二重元音
             'a', 'e', 'i', 'o', 'u', 'á', 'ã', 'à', 'â', 'é', 'ê', 'è', 'í', 'õ', 'ó', 'ô', 'û', 'ù', 'ú']  # 单元音'''
    vowel = ['uai', 'uei', 'uiu', 'uão', 'uem', 'uõe',  # 三重元音
             'ai', 'au', 'ei', 'éi', 'eu', 'éu', 'iu', 'oi', 'ói', 'ou', 'ui','uí','ex','ão', 'ãe', 'õe', # 二重元音
             'a', 'e', 'i', 'o', 'u', 'á', 'ã', 'à', 'â', 'é', 'ê', 'è', 'í', 'õ', 'ó', 'ô', 'û', 'ù', 'ú']  # 单元音
    # 辅音
    consonant = ['ch', 'gu', 'lh', 'nh', 'qu', 'br', 'pr', 'cr', 'gr', 'dr', 'tr', 'fr', 'vr', 'bl', 'pl', 'cl',
                     'gl', 'fl', 'tl','rr','ss','b', 'c', 'ç', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's','t', 'v', 'w', 'x', 'y', 'z']
    # 使用0/1将代替元音和辅音
    syllable_one_hot=[]
    for word in word_list:
        temp_list=[] #元辅音标记
        temp_syllable=[]
        # 有无数字都同样执行下面的代码
        i = 0
        while i < len(word):
            if i == 0 and word[i] == 'a':
                temp_list.append(0)
                temp_syllable.append(word[i])
                i += 1
                continue  # 跳出本次循环，继续下一个
            if word[i:i + 3] in vowel:  # 三重元音
                temp_list.append(0)
                temp_syllable.append(word[i:i + 3])
                i += 3
                continue  # 跳出本次循环，继续下一个
            elif word[i:i + 2] in vowel:  # 二重元音
                temp_list.append(0)
                temp_syllable.append(word[i:i + 2])
                i += 2
                continue  # 跳出本次循环，继续下一个
            elif word[i:i + 2] in consonant:  # 二重辅音
                temp_list.append(1)
                temp_syllable.append(word[i:i + 2])
                i += 2
                continue  # 跳出本次循环，继续下一个
            elif word[i] in vowel:  # 单元音
                temp_list.append(0)
                temp_syllable.append(word[i])
                i += 1
                continue  # 跳出本次循环，继续下一个
            elif word[i] in consonant:  # 单辅音
                temp_list.append(1)
                temp_syllable.append(word[i])
                i += 1
                continue  # 跳出本次循环，继续下一个
            else:
                # 其他特殊字符
                i += 1
        syllable_one_hot.append((temp_syllable, temp_list))
        # 将含有数字的整个单词都忽略掉
        '''
        dig=re.findall('\d',word)
        if dig!=[]:
        
            temp_syllable.append(word)
            syllable_one_hot.append((temp_syllable, temp_list)) #追加的temp_list为空列表
        else:
            i=0
            while i <len(word):
                if i==0 and word[i]=='a':
                    temp_list.append(0)
                    temp_syllable.append(word[i])
                    i += 1
                    continue  # 跳出本次循环，继续下一个
                if word[i:i + 3] in vowel:  # 三重元音
                    temp_list.append(0)
                    temp_syllable.append(word[i:i + 3])
                    i+=3
                    continue  # 跳出本次循环，继续下一个
                elif word[i:i + 2] in vowel:  # 二重元音
                    temp_list.append(0)
                    temp_syllable.append(word[i:i + 2])
                    i += 2
                    continue  # 跳出本次循环，继续下一个
                elif word[i:i+2] in consonant :  # 二重辅音
                    temp_list.append(1)
                    temp_syllable.append(word[i:i + 2])
                    i += 2
                    continue  # 跳出本次循环，继续下一个
                elif word[i] in vowel: #单元音
                    temp_list.append(0)
                    temp_syllable.append(word[i])
                    i += 1
                    continue  # 跳出本次循环，继续下一个
                elif word[i] in consonant:# 单辅音
                    temp_list.append(1)
                    temp_syllable.append(word[i])
                    i += 1
                    continue  # 跳出本次循环，继续下一个
                else:
                    # 其他特殊字符
                    i+=1
            syllable_one_hot.append((temp_syllable, temp_list))'''
    return syllable_one_hot
if __name__=='__main__':
    line = 'A， roupa que 18 a Rita levou na terça-feira para a escola era muito engraçada.'
    syllable_one_hot=get_elemento_one_hot(line)
    print(syllable_one_hot)