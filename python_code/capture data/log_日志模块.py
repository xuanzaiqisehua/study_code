'''日志的作用有以下3点：
（1） 程序调试
（2）了解软件程序运行情况，是否正常
（3）软件程序运行故障分析与问题定位
参考：https://www.cnblogs.com/yyds/p/6901864.html
'''
#********************只有级别大于或等于日志记录器指定级别的日志记录才会被输出，小于该级别的日志记录将会被丢弃
'''这是因为logging模块提供的日志记录函数所使用的日志器设置的日志级别是WARNING，因此只有WARNING级别的日志记录以及大于它的ERROR和CRITICAL级别的日志记录被输出了，而小于它的DEBUG和INFO级别的日志记录被丢弃了'''
import  logging
'''logging.debug("This is a debug")
logging.info("This is a info log")
logging.warning("This is a warning log")
logging.error("This is a error log")
logging.critical("This is a critical log")'''
# 也可以这样写：
'''logging.basicConfig(level=logging.DEBUG)#如果添加这条语句，下面的内容都会输出到控制台
logging.log(logging.DEBUG,'This is a debug log')
logging.log(logging.INFO,"This is a info log")
logging.log(logging.WARNING,"This is a warning log")
logging.log(logging.ERROR,"This is a error log")
logging.log(logging.CRITICAL,"This is a critical log")'''
'''
输出为：logging模块提供的日志记录函数所使用的日志器设置的日志默认格式为BASIC_FORMAT, 值为“%(levelname)s:%(name)s:%(message)s”
WARNING:root:This is a warning log
ERROR:root:This is a error log
CRITICAL:root:This is a critical log
'''
#*******************如果将日志记录输出到文件中，而不是打印到控制台
#在我们调用上面这些日志记录函数之前，手动调用一下basicConfig()方法，把我们想设置的内容以参数的形式传递进去就可以了。
# logging.basicConfig(**kwarags)#用于为logging日志系统做一些基本的配置
# logging模块中定义好的可以用于format格式字符串中字段有哪些：asctime,levelname,created等,使用格式为%(asctime)s,%(created)f使用时查看资料
'''LOG_FORMAT = "%(asctime)s - %(levelname)s - %(user)s[%(ip)s] - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT)
logging.warning("Some one delete the log file.", exc_info=True, stack_info=True, extra={'user': 'Tom', 'ip':'47.98.53.222'})
'''
import logging
import logging.handlers
import datetime

logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
logger.addHandler(rf_handler)
logger.addHandler(f_handler)
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')

































