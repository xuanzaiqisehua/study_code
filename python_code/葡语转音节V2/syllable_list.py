import syllable_one_hot
import re

# str='Ao entrar em casa, a sala de estar é a primeira divisão com que nos deparamos.'


def get_syllable(elemento_one_hot):
         add_local=[]
         # syllable_list=[]#音节列表
         syllable_dic={}
         n=0
         flag1=1
         flag2=1
         for i in range(n,len(elemento_one_hot[1])):
             if i ==0:  # 开始的位置
                 if elemento_one_hot[1][i] == 0:
                     flag1 = 0 # 一开始为元音
                     continue
                 else:
                     flag2=0
             # 一开始为元音
             if flag1==0:
                 if elemento_one_hot[1][i]==0:
                     loc = i # 两个元音连在一起添加标记
                     if loc != 0:
                         add_local.append(loc)  # 在i的位置添加标记
                     continue
                 else:
                     flag1=1 #出现一个辅音
                     continue
             if flag1!=0:# 出现辅音后再出现元音
                 if elemento_one_hot[1][i]==0:
                     loc=i-1
                     if loc!=0:
                         add_local.append(loc)  # 在i的位置添加标记
                     flag1=0
                     n=i-1
                     continue
             if flag2==0:# 第一个为辅音，继续再次判断元音还是辅音
                 if elemento_one_hot[1][i]==1:
                     continue
         # 添加分隔位置标记
         l=0
         for loc in add_local:
             elemento_one_hot[0].insert(loc+l,'.')
             l+=1
         syllable_dic[re.sub('\.','',''.join(elemento_one_hot[0]))] = elemento_one_hot[0]
         return syllable_dic
if __name__=='__main__':
    # str = 'Imagino que a minha festa de anos não tenha sido nada fácil para si.'
    # str='É importante consumir o vinho Torre de Ferro a pelo menos 18 graus passo.'
    # str='Ainda há tempo para dizeres o que preciso de saber para evitar esta loucura.'
    str='A, roupa que a Rita levou na terça-feira para a escola era muito engraçada.'
    syllable_one_hot_list = syllable_one_hot.get_elemento_one_hot(str)
    for elemento_one_hot in syllable_one_hot_list:
        Syllable=get_syllable(elemento_one_hot)
        print(Syllable)




