# 练习要求：
# 1、先定义一个温度类，然后定义两个描述符类用于描述摄氏度和华氏度两个属性
# 2、要求两个属性会自动进行转换，也就是说你可以给摄氏度这个属性赋值，然后打印的华氏度属性是自动转换后的结果

class Celsius:
    def __init__(self, value=25.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8

class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

class Main:
    temp = Temperature()
    print('初始摄氏度为：',temp.cel)
    print('转换后华氏度为：', temp.fah)

    print('---------------------------------')

    temp.cel = 30
    print('设置摄氏度为：',30)
    print('转换后华氏度为：',temp.fah)

    print('---------------------------------')

    temp.fah = 75
    print('设置华氏度为：', 75)
    print('转换后摄氏度为：', temp.cel)
