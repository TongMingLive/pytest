import urllib.request
# 使用代理防止服务器屏蔽：
#   1、参数是一个字典{ '类型' : '代理ip:端口号' }
#proxy_support = urllib.request.ProxyHandler()
#   2、定制、创建一个opener
#opener = urllib.request.build_opener(proxy_support)
# #   3a、安装opener
# urllib.request.install_opener(opener)
# #   3b、调用opener
# opener.open(url)



# proxy_support = urllib.request.ProxyHandler({'http':'121.9.221.188:80'})
# opener = urllib.request.build_opener(proxy_support)
# urllib.request.install_opener(opener)

# opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')]

response = urllib.request.urlopen("http://ip.xpcha.com/")
html = str(response.read().decode('utf-8'))
print(html)
