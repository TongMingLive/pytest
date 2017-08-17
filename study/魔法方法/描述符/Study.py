class C:
    # 用于访问属性，它返回属性的值
    def __get__(self, instance, owner):
        print('getting..',self,instance,owner)

    # 将在属性分配操作中调用，不反回任何内容
    def __set__(self, instance, value):
        print('setting...',self,instance,value)

    # 控制删除操作，不返回任何操作
    def __delete__(self, instance):
        print('deleting...',self,instance)


class Test:
    x = C()

class Main:
    test = Test()
    test.x
    print(test)
    print(Test)
    test.x = 'X-man'
    del test.x