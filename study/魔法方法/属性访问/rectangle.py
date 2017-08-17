class Rectangle:
    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height

    def __setattr__(self, key, value):
        if key == 'square':
            self.width = value
            self.height = value
        else:
            super().__setattr__(key,value)

    def getArea(self):
        return self.width * self.height


class Main:
    r = Rectangle(4,5)
    print('长为：',r.width)
    print('高为：', r.height)
    print('面积为：',r.getArea())

    print('')

    r.square = 10
    print('长为：', r.width)
    print('高为：', r.height)
    print('面积为：', r.getArea())