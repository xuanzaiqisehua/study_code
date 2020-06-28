''''#将字符串中的数字转换为数字
#方法一
string1='My moral standing is:0.98765'
lindex=string1.index(':',0,len(string1))
rindex=len(string1)
number=string1[lindex+1:rindex]
print(float(number))
#方法二
lindex=string1.find(":")#find找到后返回下标
number1=string1[lindex+1:len(string1)]
print(number1)
#方法三
string1='My moral standing is:0.98765'
new_str=string1.split(':')[1]#split按:(符号)分割将字符串分为两部分，取第二部分
print(new_str)'''
# 找出列表中不包含元音字母（包括大写）和数字的所有单词并按原始先后顺序输出
# word=['HELLO', 'PH', 'Hi', 'read', 'tmp123', 'Our', 'vmr']
# for item in word:
#     item_temp = item.lower()
#     for i in item_temp:
#         if i in 'aeiou'or i in '0123456789':
#             break
#     else:
#         print(item)
# 2 从键盘输入若干个以空格间隔的单词，将所有单词倒过来排列并输出，保持单词内顺序不变。
# word=input("input a string: ").split(" ")
# word.reverse()
# result=' '.join(word)
# print(result)
'''自定义函数move_substr(s, flag, n)，将传入的字符串s按照flag（1代表循环左移，2代表循环右移）
的要求左移或右移n位（例如对于字符串abcde12345，循环左移两位后的结果为cde12345ab，
循环右移两位后的结果为45abcde123），结果返回移动后的字符串，
若n超过字符串长度则结果返回-1。__main__模块中从键盘输入字符串、左移和右移标记以及移动的位数，
调用move_substr()函数若移动位数合理则将移动后的字符串输出，否则输出“the n is too large”。'''
# def movesubstr(s,flag,n):
#     if len(s)<n:
#         return -1
#     else:
#         if flag==1:
#           return s[n:]+s[:n]
#         else:
#             return s[-n:]+s[:-n]
# if __name__=='__main__':
#     s, flag, n=input().split(',')
#     result=movesubstr(s, int(flag), int(n))
#     if result!=-1:
#         print(result)
#     else:
#         print('the n is too large')











