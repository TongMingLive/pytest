print('------------- Python 字典(哈希map：键值对，映射) --------------')

mydict = {
    '+' : lambda x,y:x+y ,
    '-' : lambda x,y:x-y ,
    '*' : lambda x,y:x*y ,
    "/" : lambda x,y:x/y
}

def res(x,o,y):
    try:
        return mydict.get(o)(x,y)
    except ZeroDivisionError as reason:
        return '除数不能为零，错误引发于：'+str(reason)


print(res(1,'/',0))

print('------------- 字典内置方法 --------------')
print('------------- 定义字典的几种方式 --------------')
print('------------- 常用定义 --------------')
mydict2 = {1:'a',2:'b',3:'c'}
print(mydict2)
print('------------- 函数定义1 --------------')
mydict3 = dict(((1,'a'),(2,'b'),(3,'c')))
print(mydict3)
print('------------- 函数定义2(此方法只允许字符串为键) --------------')
mydict4 = dict( a='a' ,b='b')
print(mydict4)
print('------------- 函数定义3 --------------')
mydict5 = {}
mydict5 = mydict5.fromkeys(range(0,3),'赞')
print(mydict5)

print('------------- for each 输出字典内容 --------------')
for dictEach in mydict5.keys():
    print("key:",dictEach)

for dictEach in mydict5.values():
    print("values:",dictEach)

for dictEach in mydict5.items():
    print("items:",dictEach)
print('------------- get 输出字典内容 --------------')
print(mydict5.get(3,'该键无值'))
print(mydict5.get(2,'该键无值'))

print('------------- 替换字典内容 --------------')
mydict2[1] = '1a'
print(mydict2)

print('------------- 添加字典内容（自动添加键值对） --------------')
mydict2[4] = 'd'
print(mydict2)

print('------------- 删除字典内容 --------------')
mydict2.clear()
print(mydict2)

print('------------- 复制字典内容(将会改变地址，直接复制将会赋予相同地址) --------------')
mydict2 = mydict3.copy()
print(mydict2)

# print('------------- 随机获取一个字典内容 --------------')
# print(mydict2.popitem())

print('------------- 更新字典内容（与替换类似） --------------')
print(mydict2)
tempDict = {1:'1a'}
mydict2.update(tempDict)
print(mydict2)