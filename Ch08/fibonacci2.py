# -*- coding: utf-8 -*-
class Fib: # 类名通常大写字母分隔
    '''生成斐波那契数列的迭代器''' # 与模块和方法一样，类应该具有docstring，且可以通过print(fib.__doc__)打印出
    def __init__(self,max): # __init__方法，跟c++中的构造函数不同，调用该方法时，对象已经创建了
        self.max=max # 每个方法的第一个参数，包括__init()__方法，永远指向当前的类对象，该参数叫self，跟c++中的this一样
    def __iter__(self):
        self.a=0
        self.b=1
        return self        
    def __next__(self):
        fib=self.a
        if fib > self.max: # 这个self.max跟__init__()方法中的max完全是两回事，self.max是实例内"全局"的，可以在其他方法中访问
            raise StopIteration # 迭代到最大值时，唤醒StopIteration异常
        self.a,self.b=self.b,self.a+self.b
        return fib

fib=Fib(100) # 创建类的实例
print(fib.__class__) # 类实例的内建属性__class__
print(fib.__doc__) # 打印出类的docstring

fib1=Fib(200) # 创建第二个类的实例

## 使用迭代器 
## for循环调用Fib(1000)，这返回Fib类的实例，暂且称为fib_inst \
## for循环再调用iter(fib_inst)，它返回迭代器(renturn self)，称之fib_iter，\
## 本例中，fib_iter==fib_inst，因为__iter__()方法返回self \
## for循环调用next(fib_iter)，它又调用fib_iter对象中的__next__()方法，产生下一个斐波那契计算并返回值 \
## for拿到该值并赋给n，然后执行n值的for循环 \
## 当next(fib_iter)唤醒StopIteration异常时，for循环将吞下(swallow)该异常并退出
for n in Fib(1000):
    print(n,end=' ')

