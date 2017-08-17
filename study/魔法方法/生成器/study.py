# 所谓的协同程序就是可以运行的独立函数调用，函数可以暂停或者挂起，并在需要的时候从程序离开的地方继续或者重新开始

def myGen():
    print("生成器被执行")
    yield 1
    yield 2


myG = myGen()
for gen in myG:
    print(gen)

print('------- 斐波那契数列 -------')


def libs():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


for each in libs():
    if each > 100:
        break
    print(each, end='\t')

print('\n------- 列表推导式 -------')
a = [i for i in range(100) if not (i % 2) and (i % 3)]
print(a)

print('------- 字典推导式 -------')
b = {i:i %2 == 0 for i in range(10)}
print(b)

print('------- 函数推导式 -------')
print(sum(i for i in range(100)))
