## 复数规则迭代器
## A plural rule iterator
import re

def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

class LazyRules:
    rules_filename='plural6-rules.txt' # 这是类变量，LazyRules类的所有实例共享该变量 this is 'class variable', which is shared across all the instances of the LazyRules class
    def __init__(self):
        self.pattern_file = open(self.rules_filename,encoding = 'utf-8') # 打开模式pattern文件 open the pattern file
        self.cache=[]  # 初始化缓存 initialize the cache
    def __iter__(self): 
        self.cache_index = 0
        return self
    def __next__(self):
        self.cache_index += 1
        if len(self.cache) >= self.cache_index:
            return self.cache_index[self.cache_index-1]
        if self.pattern_file.closed:
            raise StopIteration
        line = self.pattern_file.readline()
        if not line:
            self.pattern_file.close()
            raise StopIteration
        pattern, search, replace = line.split(None, 3)
        funcs = build_match_and_apply_functions(pattern, search, replace)
        self.cache.append(funcs)
        return funcs

## 创建两个实例
## create two instances
r1 = LazyRules()
r2 = LazyRules()

## 以下表明LazyRules类的所有实例共享其中的类变量rules_filename
## the following indicates that all instances of "LazyRules" share the class variable rules_filename
## 换句话说，类的每个实例继承了'rules_filename'属性及它在类中定义的值
## in other words, each instance of the class inherits the 'rules_filename' atribute with the value defined by the class
print(r1.rules_filename)
print(r2.rules_filename)
print('\n')

## 可以使用__class__属性来访问类属性
## you can access the class attribute by using '__class__'
print(r2.__class__.rules_filename)
print('\n')

## 修改其中一个实例的属性不会影响其他实例
## changing the attribute's value in one instance does not affect other instances
r2.rules_filename = 'abc.txt'
print(r1.rules_filename)
print(r2.rules_filename)
print('\n')

## 如果修改类属性，所有仍然继承该值的实例会受到影响(这里的r1)
## if you change the class attribute, all instances that are still inheriting that value (like r1) will be affected
r2.__class__.rules_filename = 'abc.txt'
print(r1.rules_filename)
print(r2.rules_filename)