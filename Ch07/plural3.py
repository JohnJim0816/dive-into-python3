## 匹配模式列表

import re

## 在plural2.py的基础上，把模式pattern、匹配search和应用replace融到一个函数中
def build_match_and_apply_functions(pattern, search, replace):
    def matches_rule(word):
        return re.search(pattern, word)
    def apply_rule(word):
        return re.sub(search, replace, word)
    return (matches_rule, apply_rule)

patterns = \
(
    ('[sxz]$', '$', 'es'),
    ('[^aeioudgkprt]h$', '$', 'es'),
    ('(qu|[^aeiou])y$', 'y$', 'ies'),
    ('$', '$', 's') 
)

## 用pattern, search, replace这三个字符串作为实参，
## 用build_match_and_apply_functions()返回一个元组列表，每个元组都是一对函数
## 这跟"plural2.py"中的rules是等价的
rules = [build_match_and_apply_functions(pattern, search, replace)
         for (pattern, search, replace) in patterns]

def plural(noun):
    for matches_rule, apply_rule in rules:
        if matches_rule(noun):
            return apply_rule(noun)

## 测试
if __name__ == '__main__':
    noun='apple'
    print(plural(noun))