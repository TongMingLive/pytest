import sys

import easygui as e

e.msgbox('欢迎进入easyui',ok_button='加油！')

while 1:
    msg = '单选框'
    title = '请选择一个项目'
    choices = ['A','B','C','D']

    choice = e.choicebox(msg,title,choices)

    e.msgbox('你的选择是：'+str(choice),ok_button='确定')

    msg = '你希望重新开始选择吗？'
    title = '请选择'

    if e.ccbox(msg,title,choices=('确定','取消')):
        pass
    else:
        sys.exit(0)


