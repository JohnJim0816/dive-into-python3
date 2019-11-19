import re

## 将名词noun变成复数，例如apple变为apples

def plural(noun):
    if re.search('[sxz]$', noun): # 判断noun是否以s,x或z结尾
        return re.sub('$', 'es', noun)  # 如果是，后面加es
    elif re.search('[^aeioudgkprt]h$', noun): # 判断noun是否以aeioudgkprt开头，以h结尾
        return re.sub('$', 'es', noun) 
    elif re.search('[^aeiou]y$', noun): #判断noun是否以aeiou任意一个开头以y结尾
        return re.sub('y$', 'ies', noun) # 如果是，去y加ies
    else:
        return noun + 's'

## 关于re.xub()函数
# 将mark中a，b，c换成o
print(re.sub('[abc]', 'o', 'Mark'))
print(re.sub('[abc]', 'o', 'rock'))

## 测试
if __name__ == '__main__':
    noun='apple'
    print(plural(noun))