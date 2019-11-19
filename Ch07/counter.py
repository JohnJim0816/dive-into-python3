## 生成器引例1:计数
'''
counter_list = [x*x for x in range(5)]
for i in counter_list:
    print(i) 
'''

def make_counter(x):
    print('entering make_counter')
    while True:
        yield x*x
        print('incrementing x')
        x=x+1

counter = make_counter(0)

print(next(counter))
print(next(counter))

#print(counter) 
#print(next(counter))

#next(counter)