# 类的具体化就是对象，对象可以抽象成类
'''class  ClassName(object): # 定义一个类，括号当中是父类，如果没有定义父类，将其继承为object，object为万类之源
    'define ClassName class'
    clsaa_suite # 类体代码，包括这类的数据和数据的操作
#新式类可以去掉括号和object
#定义一个空类,类仅作为名称空间，此种情况中的类没有什么实际的作用
class MyDate(object):# 名称空间也成为命名空间，可以看做是一个容器或者域
    pass
# 将共性的数据或行为放在类型中，类当中的属性定义了抽象后的数据，而共性的行为抽象后就是类定义中的方法
# 比如下例
class Dog(object):
    def greet(self):# 类中的每一个方法中第一个参数都是self，表示调用这个方法的对象自身，调用时不需要传入实参
        print('Hi')'''
'''实例的创建---- 通过调用对象
(1)定义类——Dog
(2)创建一个实例——dog
(3)通过实例使用属性或方法——dog.greet'''
'''class Dog(object):
    "define Dog class"
    def setName(self,name):
        self.name=name
    def greet(self):
        # print('Hi,I am called {}.'%self.name)
        print('Hi,I am called {}.'.format(self.name))
if __name__=='__main__':
    dog=Dog()
    dog.setName('Paul')
    dog.greet()'''
''''对象的初始化方法__init__(), 当类被调用后，Python将创建实例对象，创建完对象以后，Python自动调用的第一个方法为__init__()
实例对象作为方法的第一个参数(self)   被传递进去，调用类创建实例对象时的参数都传给__init__()
比如创建每个小狗时都会给小狗取名字，此时可以将设置名字的方法放到__init__()中，比如
class Dog(object):
  def __init__(self,name):# 创建好对象后会自动调用这个方法
    self.name=name
  def greet(self):
   print('Hi,I am called %s'%self.name)
if  __name__=='__main__':
 dog=Dog('Sara')
 dog.greet()
总结：Python创建实例时需要做两件事：（1）分配内存（2）调用__init__()方法；init方法类似于其他语言中的“构造器”
#*******************类属性******************
类的数据属性（静态成员）:  仅仅是所定义的类的变量
在类被创建后被使用
可以由类中的方法来更新，也可以在主程序中更新
类属性与实例无关，修改类属性需要使用类名
count为类属性
class Dog(object):
 counter=0
 def __init__(self,name):# 创建好对象后会自动调用这个方法
    self.name=name
    Dog.counter+=1
  def greet(self):
   print('Hi,I am called %s'%(self.name,Dog.counter)
   )
if  __name__=='__main__':
 dog=Dog('Sara')
 dog.greet()

class roster :
    teacher=''
    students=[]
    def __init__(self,tn='Niuyun'):
        self.teacher=tn
    def add(self,sn):
        self.students.append(sn)
    def remove(self,sn):
        self.students.remove(sn)
    def print_all(self):
        print('Teacher:',self.teacher)
        print('Student:',self.students)
if  __name__=='__main__':
    techer=roster()
    techer.add('niulan')
    # techer.remove('Niuyun')
    techer.print_all()'''
#*********************** 继承***********************
'''继承：面向对象程序设计中，在一种抽象基础上进行扩展、细化和修改从而形成一种新的抽象，父类（基类），子类（派生类）
继承包括单继承和多继承，只有一个父类或者多个父类'''
'''class Dog(object):
 counter=0
 def __init__(self,name):# 创建好对象后会自动调用这个方法
    self.name=name
    Dog.counter+=1#  统计创建了几个对象
    def greet(self):
      print('Hi,I am called %s'%(self.name,Dog.counter)
   )
class BarkingDog(Dog):#   子类继承了父类所有的方法，子类可以对父类中的方法进行改写
    def greet(self):
        print('Woof! I am %s,my number is %d'%(self.name,Dog.counter))
        # 如果子类重写了父类的初始化方法__init__(),那么父类中的初始化方法就不会被自动调用
    def __init__(self,name):
        super().__init__(name)=name# 重写父类初始化方法应该这样写
        print('My name is',self.name)
if __name__=='__main__':
    dog=BarkingDog('Zoe')
    dog.greet()'''
#******************************BMI计算小例*************************
class BMI:
    def __init__(self,height,weight):
        self.bmi=weight/height**2
    def print_BMI(self):
        print('Your BMI index is {0:.1f}'.format(self.bmi))
class ChianaBMI(BMI):
    def print_BMI(self):
        print('Your BMI index is {0:.1f}'.format(self.bmi))
        if self.bmi<18.5:
            print('偏瘦','相关疾病发病的危险性：底（但其他疾病危险性增加）')
        elif 18.5<=self.bmi<=23.9:
            print('BMI分类： 正常','相关疾病发病的危险性：平均水平')
        elif 24<=self.bmi<=26.9:
            print('BMI分类：偏胖', '相关疾病发病的危险性：增加')
        elif 27<=self.bmi<=29.9:
            print('BMI分类：肥胖', '相关疾病发病的危险性：中度增加')
        else :
            print('BMI分类：肥胖', '相关疾病发病的危险性：严重增加')
if __name__=='__main__':
    h=float(input('Please enter your height(m):'))
    w=float(input('Please enter your weight(kg):'))
    x=ChianaBMI(h,w)
    x.print_BMI()
