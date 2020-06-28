import argparse # 导入模块
# parsser=argparse.ArgumentParser(description='My script description')# 创建一个解析对象
# parsser.add_argument()#向该对象中添加你要关注的命令行参数和选项
# parsser.parse_args()#进行解析
#*************************位置参数和选项参数结合使用*********************
'''import argparse
parser = argparse.ArgumentParser(description='My script description')

parser.add_argument("square", type=int,
                    help="display a square of a given number")
#短选项参数和长选项参数,如果选项参数被调用但是不被赋值的话将会报错，将action设置为action='store_true'的意思是如果选项参数被调用（不赋值），agrs.verbose就被赋予True
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:#如果选项参数被调用但没有被赋值，则为True
    print("the square of {} equals {}".format(args.square, answer))
else:# 如果选项参数不赋值，不调用则为None
    print(answer)
'''
# cmd 进入到这个目录下运行：python argparse_study.py 4，如果直接运行 python argparse_study.py 程序会报错，因为位置参数没有被赋值
#*****************小例子************************
'''import argparse

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))'''
#*************************例子*********************
import argparse
parser = argparse.ArgumentParser(description='My script description')
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
parser.add_argument("-v", "--verbosity", action="count", default=0)#action="count"意思是数flag（调用选项参数）的次数
args = parser.parse_args()
answer = args.x**args.y
if args.verbosity >= 2:#所以flag两次—“-vv”我们就执行第一个print
    print("Running '{}'".format(__file__))
if args.verbosity >= 1:
    print("{}^{} == ".format(args.x, args.y), end="")
print(answer)
'''$ python3 prog.py 4 2
16
$ python3 prog.py 4 2 -v
4^2 == 16
$ python3 prog.py 4 2 -vv
Running 'prog.py'
4^2 == 16'''



























