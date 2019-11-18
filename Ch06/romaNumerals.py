import re

## 匹配千位数
pattern = '^M?M?M?$' # 设置匹配模式，?表示匹配是可选的
print(re.search(pattern, 'M'))
print(re.search(pattern, 'MM'))
print(re.search(pattern, 'MMM'))
print(re.search(pattern, 'MMMM'))
print(re.search(pattern, ''))
print('\n')

##匹配百位数
pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
print(re.search(pattern, 'MCM'))

## 未写完待续