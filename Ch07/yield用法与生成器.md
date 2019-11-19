[参考链接1](https://blog.csdn.net/libbyandhelen/article/details/78957369)
参考资料: 《dive into python3》

## 基本用法

### 可迭代对象

当你用列表生成式来建立列表时就生成了一个可迭代对象，如下，counter_list就是一个可迭代对象，

```python
counter_list = [x*x for x in range(5)]
for i in counter_list:
    print(i) 
```

这里所有的值都存在内存当中，所以并不适合大量数据

### 生成器(generator)

对此较好的解决方法就是生成器，它具有以下特点：

* 可迭代

* 只能读取一次

* 实时读取数据，不全存在内存中

这样一来生成器的一大好处就是节省内存^_^。


### yield关键字

yield是一个类似于return的关键字，但是返回的只是上面所讲的生成器

```python
def make_counter(x):
    print('entering make_counter')
    while True:
        yield x*x
        print('incrementing x')
        x=x+1

counter = make_counter(0)

print(counter) 
```

如上，最后输出结果如下

```bash
<generator object make_counter at 0x108627c50>
```

### next()函数

next()函数以一个生成器对象为参数，并返回其下一个值。
```python
def make_counter(x):
    print('entering make_counter')
    while True:
        yield x*x
        print('incrementing x')
        x=x+1

counter = make_counter(0)

print(next(counter))
```

如上，对counter生成器第一次调用next()，它将针对第一条yield语句执行make_counter()中的代码，并返回x*x这个值，并且到此为止，最后输出结果如下

```bash
entering make_counter
0
```

对同一生成器反复调用会从上次开始的位置继续，直到下一条yield语句，如下

```python
def make_counter(x):
    print('entering make_counter')
    while True:
        yield x*x
        print('incrementing x')
        x=x+1

counter = make_counter(0)

print(next(counter))
print(next(counter))
```

注意是返回到循环语句中开始，相对于只是将循环语句独立出来分步进行，输出结果如下：

```bash
entering make_counter
0
incrementing x
1
```

### for循环输出

for循环能够连续输出，注意要设定一个终止条件flag，例如这里的max，如下斐波那契数列：

```python
def fib(max):
    a,b=0,1
    while a < max:
        yield a  # 跟return类似，详见yield用法笔记
        a,b=b,a+b

## 测试
if __name__ == '__main__':
    for n in fib(1000):
        print(n,end=' ')
    print('\n')
```

### list()函数输出

将生成器传给list函数，它将遍历整个生成器(就像上面的for循环)并返回包含所有数值的列表，如下

```python
def fib(max):
    a,b=0,1
    while a < max:
        yield a  # 跟return类似，详见yield用法笔记
        a,b=b,a+b

## 测试
if __name__ == '__main__':
    print(list(fib(1000)))
```




## 与return的区别

yield用法跟return类似，都会返回值，但是会有以下几点区别

* return语句象征着函数的结束
```python
def call(i):
    return 2*i
# 从这一行开始不属于函数call部分
    i=i+1
    print(i)
    return 2*i
print(call(4))
```

