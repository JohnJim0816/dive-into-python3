##生成器引例2:斐波那契数列

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
    print(list(fib(1000)))