import re

print(re.search(r'FishC','I Love FishC.com! 666'))

# 通配符：'.'(除换行外的任何单个字符)
print(re.search(r'.','I Love FishC.com! 666'))

# 消除某字符串的特殊功能：'\'将一个字符匹配为普通字符
print(re.search(r'\.','I Love FishC.com! 666'))

# 匹配单个数字：'\d'
print(re.search(r'\d','I Love FishC.com! 666'))

# 创建字符类：'[]'('-'代表范围)
print(re.search(r'[aeiouAEIOU]','I Love FishC.com! 666'))
print(re.search(r'[a-z]','I Love FishC.com! 666'))
print(re.search(r'[0-9]','I Love FishC.com! 666'))

# 重复次数：'{}'(','分割表示范围)
print(re.search(r'[6{3}]','I Love FishC.com! 666'))
print(re.search(r'[6{0,9}]','I Love FishC.com! 666'))

# 或者判断符：'A|B'表示匹配正则表达式A或者B
print(re.search(r'(([01]\d\d|2[0-4]\d|25[0-5])\.)(([01]\d\d|2[0-4]\d|25[0-5]|\d\d|\d)\.){2}([01]\d\d|2[0-4]\d|25[0-5]|\d\d|\d)','192.168.0.111'))

#匹配字符串的开始位置：'^'
print(re.search(r'^I','I Love FishC.com! 666'))

#匹配字符串的结束位置：'$'
print(re.search(r'\.com$','I Love FishC.com'))

# 匹配前面的子表达式零次或多次，等价于{0,}：'*'
# 匹配前面的子表达式一次或多次，等价于{1,}：'+'
# 匹配前面的子表达式零次或一次，等价于{0,1}：'?'

# 贪婪模式与非贪婪模式
s = '<html><head><title>测试</title></head><body></body></html>'
print(re.search(r'<.+>',s))#贪婪模式（默认）
print(re.search(r'<.+?>',s))#非贪婪模式