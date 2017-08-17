class C:
    # 定义当该类属性被访问时调用
    def __getattribute__(self, item):
        print('getattribute')
        return super().__getattribute__(item)

    # 定义当用户试图访问一个不存在的属性时调用
    def __getattr__(self, item):
        print('getattr')

    # 定义当一个属性被设置时调用
    def __setattr__(self, key, value):
        print('setattr')
        super().__setattr__(key,value)

    # 定义一个属性被删除时调用
    def __delattr__(self, item):
        print('delattr')
        super().__delattr__(item)


class Main():
    c = C()
    print(c.x)

    print('')

    c.x = 1
    print(c.x)