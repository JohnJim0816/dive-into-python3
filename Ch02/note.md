# 2 第一个python程序

## 可选的参数

对于函数声明”def approximate_size(size, a_kilobyte_is_1024_bytes=True):“，􏱆􏶙􏲤􏵛􏱭􏱆􏶙􏲤􏵛􏱭第二个参数a_kilobyte_is_1024_bytes指定了一个默认值True，表明这个参数可选(optional)，即可以在调用的时候不指定它而默认为True

## import 搜索路径

import一个模块时例如import sys，可打印sys.path来知道该模块所在路径

## 一切都是对象

在python里面所有东西都是对象，字符串、列表、函数、类、类的实例(instance)甚至模块都是对象

## 代码缩进(INDENTING CODE)

* 代码块(Code blocks)就是通过缩进定义的，代码块是指if、for、while循环，缩进表示一个代码块开始，非缩进表示结束
* 这不是函数结尾，完全空白的一行不算
## 处理异常(EXCEPTIONS)
如下，raise语句在创建一个ValueError类的实例并传递一个字符串‘number must be non-negative'到它的初始化方法里面
```python
if size < 0:
raise ValueError('number must be non􏳸negative')
```
## UNBOUND 􏰡􏷇变量
python可以不声明这个变量直接赋值，但不支持引用变量却从不赋值
## 所有名称区分大小写
