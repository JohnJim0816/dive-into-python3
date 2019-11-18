## 知识点：\d匹配所有0-9的数字，\D匹配除了数字外所有的字符
## 目的：匹配不同输入格式的电话号码，格式列举如下
# 800-555-1212
# 800 555 1212
# 800.555.1212
# (800) 555-1212
# 1-800-555-1212
# 800-555-1212-1234
# 800-555-1212x1234
# 800-555-1212 ext. 1234
# work 1-(800) 555.1212 #1234

import re

# 模式1
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$') #\d表示匹配数字0-9，{3}表示匹配三位数字
# 调用group方法将返回结果生成元组
print(phonePattern.search('800-555-1212').groups())
# 这种模式不适用以下情况，会返回错误
# print(phonePattern.search('800-555-1212-1234').groups())
print('\n')

# 改进模式2，\d+表示匹配一个或者多个数字
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$') 
print(phonePattern.search('800-555-1212-1234').groups())
# 但是这种模式反而不能匹配原来的了，会返回错误
#print(phonePattern.search('800-555-1212').groups())
print('\n')

# 改进模式3，\D+表示匹配一个或者以上的字符
phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
print(phonePattern.search('800 555 1212 1234').groups())
print(phonePattern.search('800-555-1212-1234').groups())
# 但是还是不能匹配以下情况，会返回None
print(phonePattern.search('80055512121234'))
print(phonePattern.search('800-555-1212'))
print('\n')

# 改进模式4，与模式3的区别就是把所有+改成*，这样就能解析没有分隔符的情况
phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
# 能够适配四种了
print(phonePattern.search('80055512121234').groups())
print(phonePattern.search('800.555.1212 x1234').groups())
# 如果最后一个分机号不存在，那么可以返回一个空元素
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('800-555-1212-1234').groups())
print('\n')

# 改进模式5,开头加了\D*适配前面的(
phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print(phonePattern.search('(800)5551212 ext. 1234').groups())
print(phonePattern.search('800-555-1212').groups())
print(phonePattern.search('800-555-1212-1234').groups())
print(phonePattern.search('800.555.1212 x1234').groups())
print(phonePattern.search('80055512121234').groups())
print('\n')

# 改进模式6，去掉模式5开头的^和\D*，直接加了括号，表示不会从开头匹配，这样就可以忽略开头不必要的数字或字符
phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$') 
print(phonePattern.search('work 1-(800) 555.1212 #1234').groups())
print(phonePattern.search('(800)5551212 ext. 1234').groups())

# 改进模式7，改为松散正则表达式(verbose regular expression)，增强可读性
phonePattern = re.compile(r'''
# don't match beginning of string, number can start anywhere
(\d{3}) # area code is 3 digits (e.g. '800')
\D* # optional separator is any number of non-digits (\d{3}) # trunk is 3 digits (e.g. '555')
\D* # optional separator
(\d{4}) # rest of number is 4 digits (e.g. '1212')
\D* # optional separator
(\d*) # extension is optional and can be any number of digits $ # end of string
''', re.VERBOSE)

## 常用正则表达式
# ^ 匹配字符串开始位置
# $ 匹配字符串结束位置
# \b 匹配一个单词边界
# \d 匹配一个数字
# \D 匹配一个任意的非数字字符
# x? 匹配可选的x字符，即0个或者1个x字符
# x* 匹配0个或者多个x
# x+ 匹配一个或者多个x
# x{n,m} 匹配n个到m个x
# (a|b|c) 匹配单独的任意一个a或者b或者c
# (x) 这是一个组，它会记忆它匹配到的字符串。你可以用re.search返回的匹配对象的groups函数来获取匹配到的值