import re
import syllable_one_hot,syllable_list

#**************************** 发音词典构建 ****************************
# 样例
# line='Ainda há tempo para dizeres o que preciso de saber para evitar esta loucura'
# line='É importante consumir o vinho Torre de Ferro a pelo menos 18 graus.'



# 带重读符号的元音
vowel_syllable=['a','e','i','o','ã','u','á','à','â','é','ê','è','í','õ','ó','û','ù','ú']
# 辅音

one_pronounce_dic={'uai': 'waj', 'uei': 'wɐj', 'uiu': 'wiw', 'uão': 'wãw', 'uem': 'wãj', 'uõe': 'wõj', 'ai': 'aj', 'au': 'aw', 'ei': 'ɐi', 'éi': 'Ɛj', 'eu': 'ew', 'éu': 'Ɛw', 'iu': 'iw', 'oi': 'oj', 'ói': 'ɔj',
                   'ou': 'o w', 'ui': 'uj', 'an': 'ɐ͂', 'en': 'e͂', 'im': 'ĩ', 'in': 'ĩ', 'om': 'õ', 'on': 'õ', 'um': 'ũ', 'un': 'ũ', 'ão': 'ɐ͂w', 'ãe': 'ɐ͂j', 'õe': 'õj', 'ch': 'ʃ', 'lh': 'ʎ', 'nh': 'ɲ', 'á': 'a',
                   'à': 'a', 'â': 'ɐ', 'ã': 'ɐ͂', 'é': 'ɛ', 'ê': 'e', 'i': 'i', 'ó': 'ɔ', 'ô': 'o', 'u': 'u', 'ú': 'u', 'b': 'b', 'ç': 's', 'Ç': 's', 'd': 'd', 'f': 'f', 'j': 'ʒ', 'k': 'k', 'm': 'm', 'n': 'n',
                   'p': 'p', 'r': 'ɾ', 't': 't', 'v': 'v', 'w': 'w', 'y': 'j','ss':'s','rr':'R','pr': 'pɾ','gr':'gɾ','fr': 'fɾ','dr': 'dɾ','cr': 'kɾ',
                   'tr': 'tɾ','br': 'bɾ','vr': 'vɾ','bl': 'bl','cl': 'kl','pl': 'pl','fl': 'fl','tl': 'tl','gl': 'gl'}
mul_pronounce_dic={'am': 'ɐ͂,ɐ͂w', 'em': 'e͂,ɐ͂j', 'ex': 'iʃ,eʃ', 'gu': 'g,gw', 'qu': 'k,kw', 'a': 'a,ɐ', 'e': 'e,i,ə,ɛ', 'o': 'u,o,ɔ', 'c': 'k,s', 'g': 'g,ʒ', 'l': 'l,ɫ', 's': 'z,s,ʃ,ʒ', 'x': 'ʃ,z,ks,s', 'z': 'ʃ,z'}


stress_tail=['ar','er','ir','im','um','om','is','us','i','u','ch', 'gu', 'lh', 'nh', 'qu','rr','b', 'c', 'ç', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r','t', 'v', 'w', 'x', 'y', 'z']
dic = {}
def get_line(line):
    Syllable_one_hot=syllable_one_hot.get_elemento_one_hot(line)#获取元辅音元素以及0，1标记列表
    word_syllable_line=[]
    for elemento_one_hot in Syllable_one_hot:
        Syllable_dic = syllable_list.get_syllable(elemento_one_hot)
        for syllable,ele in Syllable_dic.items():
            # print(syllable)
            # print(ele)
            # ****************************** 添加重读标记 *******************************
            stress_flag=-1# 初始化为-1
            stress_symbol_list=[]#记录重读符号的位置
            dot_loc=[]# 记录音节分隔位置
            # 是否有重读符号
            for march in re.finditer('[áãàâéêèíõóôûùú]', ''.join(ele)):
                stress_symbol_list.append(march.start())
            if stress_symbol_list!=[]:
                stress_flag=stress_symbol_list[0]#一般一个单词中有一个重读音节，顾默认一个单词中只有一个有重读符号的字母，将重读字母位置赋值给stress_flag
            for dot in re.finditer('\.',''.join(ele)):# 找到所有的音节分隔位置
                dot_loc.append(dot.start())
            # 有多个音节并有重音符号
            if  dot_loc !=[] and stress_flag!=-1:
                for d in range(len(dot_loc)):
                    if stress_flag>dot_loc[d]:
                        continue
                    else:
                        stress_flag=d
                        break
            # 有多个音节分情况讨论
            elif dot_loc !=[]:
                if len(syllable)>0:
                    if syllable[-2:] in stress_tail:#后两个字符以固定字符结尾
                        stress_flag = len(dot_loc)
                    elif syllable[-1] in stress_tail:#后一个字符以固定字符结尾
                        stress_flag = len(dot_loc)
                    else:
                        stress_flag =len(dot_loc)-1#否则就将倒数第二个音节作为重读音节
            # 没有多个音节，但有重音符号,只有一个音节时,stress_fla=-1
            elif stress_flag!=-1:#有重读符号
                stress_flag=-2
            #************************************** 为单词分配发音 *****************************************
            e = 0
            dot_flag = 0
            syl = []
            while e<len(ele):
                if ele[e] == '.':
                    if stress_flag==dot_flag:
                        syl.append('1 .')
                    else:
                        syl.append('.')
                    dot_flag += 1
                    e+=1
                    continue

                if ele[e] == 'a':
                    # an发音
                    if e < len(ele) - 1:
                        if ele[e + 1] == 'n':
                            syl.append(one_pronounce_dic['an'])
                            e += 2
                            continue
                        elif ele[e + 1] == 'm':
                            if dot_flag==stress_flag:
                              syl.append(mul_pronounce_dic['a'].split(',')[1])
                            else:
                                syl.append(mul_pronounce_dic['am'].split(',')[0])
                            e += 2
                            continue
                        else:
                            if dot_flag==stress_flag:
                              syl.append(mul_pronounce_dic['a'].split(',')[0])
                            else:
                                syl.append(mul_pronounce_dic['a'].split(',')[1])
                            e += 1
                            continue
                    else:
                        if dot_flag == stress_flag:
                            syl.append(mul_pronounce_dic['a'].split(',')[0])
                        else:
                            syl.append(mul_pronounce_dic['a'].split(',')[1])
                        e += 1
                        continue

                if ele[e] == 'e':
                    if e < len(ele) - 1:
                        if ele[e + 1] == 'n':
                            if dot_flag == stress_flag:
                                syl.append(mul_pronounce_dic['e'].split(',')[0])
                            else:
                                syl.append(one_pronounce_dic['en'])
                            e+=2
                            continue
                        elif ele[e + 1] == 'm':
                            # e在 m之前且重读
                            if dot_flag == stress_flag:
                                  syl.append(mul_pronounce_dic['e'].split(',')[0])
                            # e 在 m 之前但不重读
                            else:
                                # em在末尾
                                if e==len(ele)-2:
                                    syl.append(mul_pronounce_dic['em'].split(',')[1])
                                #  em不在末尾
                                else:
                                    syl.append(mul_pronounce_dic['em'].split(',')[0])
                            e += 2
                            continue
                        else:
                            if dot_flag == stress_flag:
                                syl.append(mul_pronounce_dic['e'].split(',')[0])
                                e+=1
                                continue
                            else:
                                if e == 0 or ele[e + 1] in vowel_syllable:
                                    syl.append(mul_pronounce_dic['e'].split(',')[1])
                                    e+=1
                                    continue
                                else:
                                    syl.append(mul_pronounce_dic['e'].split(',')[2])
                                    e+=1
                                    continue
                    if e == len(ele) - 1:
                        if dot_flag == stress_flag:
                            syl.append(mul_pronounce_dic['e'].split(',')[0])
                        else:
                            syl.append(mul_pronounce_dic['e'].split(',')[2])
                        e += 1
                        continue
                elif ele[e] == 'ex':
                    if e == 0:
                        syl.append(mul_pronounce_dic['ex'].split(',')[0])
                    else:
                        syl.append(mul_pronounce_dic['ex'].split(',')[1])
                    e += 1
                    continue
                if ele[e]=='i':
                    if e<len(ele)-1:
                        if ele[e+1]=='m' or ele[e+1]=='n':
                            syl.append(one_pronounce_dic['im'])
                            e += 2
                            continue
                if ele[e] == 'gu':
                    if e < len(ele) - 1:
                        if ele[e + 1] == 'a':
                            syl.append(mul_pronounce_dic['gu'].split(',')[1])
                        else:
                            syl.append(mul_pronounce_dic['gu'].split(',')[0])
                        e+=1
                        continue
                    else:
                        syl.append(mul_pronounce_dic['gu'].split(',')[0])
                        e += 1
                        continue
                if ele[e] == 'g' and e < len(ele) - 1:
                    if ele[e + 1] == 'e' or ele[e + 1] == 'i':
                        syl.append(mul_pronounce_dic['g'].split(',')[1])
                    else:
                        syl.append(mul_pronounce_dic['g'].split(',')[0])
                    e += 1
                    continue
                if ele[e] == 'qu':
                    if e < len(ele) - 1:
                        if ele[e + 1] == 'e' or ele[e + 1] == 'i':
                            syl.append(mul_pronounce_dic['qu'].split(',')[0])
                        else:
                            syl.append(mul_pronounce_dic['qu'].split(',')[1])
                    else:
                        syl.append(mul_pronounce_dic['qu'].split(',')[0])
                    e += 1
                    continue
                if ele[e] == 'o':
                    if e<len(ele)-1:
                        if ele[e+1]=='m' or ele[e+1]=='n':
                            syl.append(one_pronounce_dic['om'].split(',')[0])
                            e += 2
                            continue
                        else:
                            if dot_flag != stress_flag:
                                syl.append(mul_pronounce_dic['o'].split(',')[0])
                            else:
                                syl.append(mul_pronounce_dic['o'].split(',')[1])
                            e += 1
                            continue
                    if e == len(ele) - 1:
                        syl.append(mul_pronounce_dic['o'].split(',')[0])
                        e+=1
                        continue
                if ele[e] == 'c':
                    if e < len(ele) - 1:
                        if ele[e + 1] == 'e' or ele[e + 1] == 'i':
                            syl.append(mul_pronounce_dic['c'].split(',')[1])
                            e+=1
                            continue
                        else:
                            syl.append(mul_pronounce_dic['c'].split(',')[0])
                            e+=1
                            continue
                if ele[e]=='l':
                    # 词尾
                   if e==len(ele)-1:
                      syl.append(mul_pronounce_dic['l'].split(',')[1])
                      e+=1
                      continue
                   # 音节结尾
                   elif e<len(ele)-1:
                     if ele[e + 1] == '.':
                        syl.append(mul_pronounce_dic['l'].split(',')[1])
                        e += 1
                        continue
                     else:
                         syl.append(mul_pronounce_dic['l'].split(',')[0])
                         e += 1
                         continue
                if ele[e] == 's':
                    if e==len(ele)-1:
                        syl.append(mul_pronounce_dic['s'].split(',')[2])
                        e += 1
                        continue
                    elif e < len(ele) - 1:
                        # 音节结尾处
                        if ele[e + 1] == '.':
                            syl.append(mul_pronounce_dic['s'].split(',')[2])
                            e += 1
                            continue
                        elif ele[e + 1] == 'm' or ele[e + 1] == 'n':
                            syl.append(mul_pronounce_dic['s'].split(',')[3])
                            e += 1
                            continue
                        else:
                            if 0<e:
                          # s在两个元音字母之间
                              if ele[e - 1] in vowel_syllable and ele[e + 1] in vowel_syllable:
                                syl.append(mul_pronounce_dic['s'].split(',')[0])
                              else:
                                    syl.append(mul_pronounce_dic['s'].split(',')[1])
                              e += 1
                              continue
                            else:
                                syl.append(mul_pronounce_dic['s'].split(',')[1])
                                e += 1
                                continue
                if ele[e] == 'x':
                    # x在词首
                    if e == 0:
                        syl.append(mul_pronounce_dic['x'].split(',')[0])
                    # x其他位置
                    else:
                        syl.append(mul_pronounce_dic['x'].split(',')[2])
                    e+=1
                    continue
                if ele[e] == 'z':
                    if e == len(ele) - 1:
                        syl.append(mul_pronounce_dic['z'].split(',')[0])
                    else:
                        syl.append(mul_pronounce_dic['z'].split(',')[1])
                    e+=1
                    continue
                if ele[e] == 'l':
                    # l在词尾
                    if e==len(ele)-1:
                        syl.append(mul_pronounce_dic['l'].split(',')[1])
                    else:
                        if ele[e+1]=='.':
                            syl.append(mul_pronounce_dic['l'].split(',')[1])
                        else:
                            syl.append(mul_pronounce_dic['l'].split(',')[0])
                    e+=1
                    continue
                if ele[e] == 'i':
                    if e < len(ele) - 1:
                        if ele[e + 1] == 'm' or ele[e + 1] == 'n':
                            syl.append(one_pronounce_dic['im'])
                            e+=1
                            continue
                        else:
                            syl.append(one_pronounce_dic['i'])
                            e += 1
                            continue
                    else:
                        syl.append(one_pronounce_dic['i'])
                        e += 1
                        continue
                if ele[e]=='u':
                    if e<len(ele)-1:
                        if ele[e+1]=='m' or ele[e+1]=='n':
                            syl.append(one_pronounce_dic['um'])
                            e += 2
                            continue
                if ele[e] in one_pronounce_dic:
                    syl.append(one_pronounce_dic[ele[e]])
                    e+=1
                    continue

                else:
                    if ele[e] not in dic:
                        dic[ele[e]]='0'
                    e+=1
                    continue
            if e == len(ele) and stress_flag == dot_flag:
                syl.append('1')
            if stress_flag==-2:
                syl.append('1')
            # print(' '.join(syl))
            final_syllable=re.sub('\s\d','1',' '.join(syl))
            word_syllable_line.append(final_syllable)
    return ' / '.join(word_syllable_line)
with open( '../葡语000001-012000.txt','r',encoding='utf-8') as r:
    lines=r.readlines()
with open('葡语000001-012000_转换v3.txt','a',encoding='utf-8') as w:
    for line in lines:
        syllable_line=get_line(line.split('\t')[1].strip())
        w.write(line+'\t'+syllable_line+' \n')
# word_line='311 Imagino que a minha festa de anos não tenha sido nada fácil para si.'
# syllable_line = get_line(word_line)
# print(syllable_line)






