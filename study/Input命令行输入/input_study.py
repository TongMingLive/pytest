import random

secret = random.randint(0,10)
i = 0
string = '请输入我心中所想的数字：'
while(i<3):
    guess = int(input(string))
    if guess == secret:
        print('回答正确')
        break
    else:
        if guess < secret:
            print('小了')
        else:
            print('大了')
        string = '请重新输入：'
    i += 1
print('游戏结束')