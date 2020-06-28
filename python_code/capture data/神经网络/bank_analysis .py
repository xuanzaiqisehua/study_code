import os
'''log信息共有四个等级，按重要性递增为：
INFO（通知）<WARNING（警告）<ERROR（错误）<FATAL（致命的）:0,1,2,3
0:默认值，输出所有信息
1：屏蔽通知信息
2：屏蔽通知和警告信息
3：屏蔽通知信息、警告信息和报错信息
'''
os.environ["TF_CPP_MIN_LOG_LEVEL"]='2'# 设置log输出信息，也就是程序运行时系统打印的信息
