## 函数列表

import re

## 同plural1.py比较，增加了抽象层次的内容，定义了一系列规则
## 每条匹配规则都有自己的函数re.search，每条应用规则也有自己的函数re.sub
def match_sxz(noun):
    return re.search('[sxz]$', noun)
def apply_sxz(noun):
    return re.sub('$', 'es', noun)
def match_h(noun):
    return re.search('[^aeioudgkprt]h$', noun)
def apply_h(noun):
    return re.sub('$', 'es', noun)
def match_y(noun):
    return re.search('[^aeiou]y$', noun)
def apply_y(noun):
    return re.sub('y$', 'ies', noun)
def match_default(noun):
    return True
def apply_default(noun): 
    return noun + 's'

## 定义rules数据结构，即一个函数对的序列
## 这样在plural函数中可以使用for循环，从而减少几行代码
## 该技术能够运用成功的原因是python中一切都是对象，包括了函数
rules = ((match_sxz, apply_sxz), (match_h, apply_h), (match_y, apply_y),
         (match_default, apply_default)
         )

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

## 测试
if __name__ == '__main__':
    noun='apple'
    print(plural(noun))