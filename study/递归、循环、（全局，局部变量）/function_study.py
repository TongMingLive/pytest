print('--------------- 函数的学习 ---------------')

print('\n--------------- 定义函数 ---------------')
def pr():
    print('此处为函数体')

# 调用函数
pr()

print('定义有参函数')
def prt(page):
    print(page)

prt('此为带参函数')

print('\n--------------- return方法 ---------------')
def re(num1,num2):
    return num1+num2

print(re(1,2))

print('\n--------------- 变量作用域 ---------------')

count = 5
print("初始变量",count)

print('--------------- 局部作用域 ---------------')

def changCount():
    count = 10
    print("修改的全局变量",count)

changCount()
print("全局变量值:",count)

print('--------------- 全局作用域 ---------------')

def changCount():
    global count    #将变量修改为全局
    count = 10
    print("修改的全局变量",count)

changCount()
print("全局变量值:",count)

print('--------------- 闭包全局作用域 ---------------')

def fun1():
    x = 5
    def fun2():
        nonlocal x
        x *= x
        return x
    return fun2()

print(fun1())

print('ps:其中global是定义为全局变量的，nonlocal是定义函数内部变量的')

print('\n--------------- lambda声明函数 ---------------')

def ds(x):
    return 2 * x +1
print(ds(5))

print('--------------- 等同于 ---------------')

g = lambda x : 2 * x +1
print(g(5))

print('\n--------------- bif内置函数 ---------------')

print('--------------- filter()函数,过滤掉函数中所有false ---------------')

print(list(filter(lambda x : x % 2 ,range(10))))

print('--------------- map()映射函数 ---------------')

print(list(map(lambda x : x * 2 , range(10))))

print('\n--------------- 递归函数 ---------------')
print('--------------- 使用循环实现阶层计算 ---------------')

def jiecen(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

print(jiecen(5))

print('--------------- 使用递归实现阶层计算 ---------------')

def digui(n):
    if n == 1:
        return 1
    else :
        return n * digui(n - 1)

print(digui(5))