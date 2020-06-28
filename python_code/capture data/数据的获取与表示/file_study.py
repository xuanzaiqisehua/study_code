# 创建一个文件Blowing in the wind.txt,填入内容
# def insert_line(lines):
#     lines.insert(0,'Blow in the wind\n')
#     lines.insert(1, 'Bob Dylan\n')
#     lines.append('1962 by Warner Bros.Inc.')
#     return ''.join(lines)
file_name='Blowing in the wind.txt'
with open(file_name,'r+') as f:
    result=f.readlines()
    result.insert(0, 'Blow in the wind\n')
    result.insert(1, 'Bob Dylan\n')
    result.append('1962 by Warner Bros.Inc.')
    f.seek(0)
    f.writelines(result)
    print(result)

