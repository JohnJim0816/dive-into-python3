## 我们想要替换掉ROAD
s = '100 NORTH MAIN ROAD'
s.replace('ROAD', 'RD.')

## 但是遇到如下情况，也会替换掉BROAD中的ROAD，这不符合初衷
s = '100 NORTH BROAD ROAD'
s.replace('ROAD', 'RD.')

## 可以用如下方式只替换最后4个字符，但是如果ROAD不在末尾这个方法就不行了
s = s[:-4] + s[-4:].replace('ROAD', 'RD.')

## 这时候就要转向正则表达式了，所有正则表达式都在re模块中

import re
s = re.sub('ROAD$', 'RD.', s)

##但是想要真正的ROAD，就必须匹配到字符串末尾，而且必须是独立的词
##在在正则表达式中，可以用\b表示独立的词，但是比较复杂的是在python中字符\可能需要转义，
s = re.sub('\\bROAD$', 'RD.', s)

## 可以在前面加r，'\t'是制表符，而r'\t'就只是符号\和t
s = re.sub(r'\bROAD$', 'RD.', s) 

## 对于字符串ROAD不在结尾的情况，需要把$改为\b
s = '100 BROAD ROAD APT. 3'
s = re.sub(r'\bROAD\b', 'RD.', s) 
print(s)