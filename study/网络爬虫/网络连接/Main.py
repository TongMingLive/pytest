import urllib.request

# 获取网页的对象
response = urllib.request.urlopen("https://www.baidu.com")
# 从网页对象读取网页内容
html = response.read()
# 设置网页内容的编码格式
html = html.decode('utf-8')
print(html)
# 获取网页对象的url地址
print("\n",response.geturl())
# 获取网页HTTPMessage对象 可以返回服务器信息
print('\n',response.info())
# 获取网站响应码
print(response.getcode())