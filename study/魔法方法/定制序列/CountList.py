# 自定义容器，计算每个属性被调用的次数

class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, item):
        self.count[item] += 1
        return self.values[item]

class Main:
    c = CountList('A','B','C','D')
    print(c[1],c[1],c[1],c[1])
    print(c.count)