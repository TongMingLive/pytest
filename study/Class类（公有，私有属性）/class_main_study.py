class Study:
    _type = "普通用户"

    # 构造方法
    def __init__(self,name):
        self.name = name

    # get set 方法
    def setName(self,name):
        self.name = name
    def getName(self):
        print('我叫'+self.name)

    # 私有属性 get set del 方法
    def setType(self,type):
        self._type = type
    def getType(self):
        return self._type
    def delType(self):
        del self._type
        
    # 公有属性property，自动调用方法
    defType = property(getType,setType,delType)


# 普通调用
a = Study("")
a.setName('张三')
a.getName()

# 构造调用
b = Study('李四')
b.getName()

# 私有调用 规范方式
c = Study('')
c.setType('管理员')
print(c.getType())

# 私有调用 漏洞方式
# d = Study('')
# print(d._Study_type)

# property调用
e = Study('王五')
e.defType = '管理员'
print(e.defType)
del e.defType
