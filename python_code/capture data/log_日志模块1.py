# 参考:https://www.cnblogs.com/xianyulouie/p/11041777.html
'''
format常用格式说明
%(levelno)s: 打印日志级别的数值
%(levelname)s: 打印日志级别名称
%(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
%(filename)s: 打印当前执行程序名
%(funcName)s: 打印日志的当前函数
%(lineno)d: 打印日志的当前行号
%(asctime)s: 打印日志的时间
%(thread)d: 打印线程ID
%(threadName)s: 打印线程名称
%(process)d: 打印进程ID
%(message)s: 打印日志信息'''


import logging
import os.path
import time
#***************************将日志保存到文件中（1）
#创建一个logger
logger=logging.getLogger()
logger.setLevel(logging.INFO)#设置级别
#第二步，创建一个handler，用于写入日志
rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time())) #Python time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
# os.getcwd()获得当前路径,os.path.dirname()返回文件路径，这条语句是在当前路径下建一个Logs文件夹
# log_path=os.path.dirname(os.getcwd())+'/Logs/'
log_path=os.getcwd()+'/Logs/'
# print(os.getcwd())
# exit()
log_name=log_path+rq+'.log'
logfile=log_name
fh=logging.FileHandler(logfile,mode='w')
fh.setLevel(logging.DEBUG)#输出到file的log等级开关
#第三步，定义handler的输出格式
formatter=logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
#第四步，将logger添加到handler里面
logger.addHandler(fh)
# 日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')
#*******************************将日志输出到控制台（2）
'''#创建一个logger
logger=logging.getLogger()
logger.setLevel(logging.INFO)#设置级别
#第二步，创建一个handler，用于写入日志
rq=time.strftime('%Y%m%d%H%M',time.localtime(time.time())) #Python time strftime() 函数接收以时间元组，并返回以可读字符串表示的当地时间，格式由参数format决定。
# os.getcwd()获得当前路径,os.path.dirname()返回文件路径，这条语句是在当前路径下建一个Logs文件夹
# log_path=os.path.dirname(os.getcwd())+'/Logs/'
log_path=os.getcwd()+'/Logs/'
# print(os.getcwd())
# exit()
log_name=log_path+rq+'.log'
logfile=log_name
fh=logging.FileHandler(logfile,mode='w')
fh.setLevel(logging.DEBUG)#输出到file的log等级开关
#在输出文件的代码中（1）新加入下面两条语句
ch=logging.StreamHandler()
ch.setLevel(logging.WARNING)#输出到控制台的等级开关
#第三步，定义handler的输出格式
formatter=logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
#在输出文件的代码中（1）新加入下面两条语句
ch=logging.StreamHandler()
ch.setLevel(logging.WARNING)#输出到控制台的等级开关

#第四步，将logger添加到handler里面
logger.addHandler(fh)
#在输出文件的代码中（1）新加入下面两条语句
ch.setFormatter(formatter)
logger.addHandler(ch)
# 日志
logger.debug('this is a logger debug message')
logger.info('this is a logger info message')
logger.warning('this is a logger warning message')
logger.error('this is a logger error message')
logger.critical('this is a logger critical message')'''
#****************************************捕捉异常,用traceback记录******************************
'''import os.path
import time
import logging
# 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 创建一个handler，用于写入日志文件
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = os.path.dirname(os.getcwd()) + '/Logs/'
log_name = log_path + rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile, mode='w')
fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
# 定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)
# 使用logger.XX来记录错误,这里的"error"可以根据所需要的级别进行修改
try:
    open('/path/to/does/not/exist', 'rb')
except (SystemExit, KeyboardInterrupt):
    raise
except Exception as e:
    logger.error('Failed to open file', exc_info=True)'''