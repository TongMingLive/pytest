import urllib.request
import urllib.parse
import json
import time

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
print('提供服务的网站url：', url)

# 添加头部信息伪装浏览器防止被服务器屏蔽爬虫
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'

# 浏览器审查元素的Network  ->  FORM DATA
data = {}
data['type'] = 'AUTO'
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'utf-8'
data['typoResult'] = 'true'

while True:
    i = str(input('请输入需要翻译的内容(输入"q!"退出程序)：'))
    if i == 'q!':
        print('感谢您的使用！')
        break

    data['i'] = i

    # 将字典转化为网页编码格式 即网页头部url
    data = urllib.parse.urlencode(data).encode('utf-8')
    print('发送给网页的data对象：', data)

    # 将post请求发送到远程服务器并获取request对象
    req = urllib.request.Request(url, data, headers)
    print('头部信息：',req.headers)
    response = urllib.request.urlopen(req)
    # 读取就收到的json内容
    html = response.read().decode('utf-8')
    print('获取到的json内容：', html.strip())

    if (str(html).find('"errorCode":50') > 0):
        print('您已被服务器屏蔽')
    else:
        # 将json数据转化为字典格式
        target = json.loads(html)
        print('转化后的字典内容：', target)

        # 从字典中获取翻译内容
        print('用户需要得到的数据：', target['translateResult'])
        print('需要翻译的内容：', target['translateResult'][0][0]['src'])
        print('翻译过后的内容：', target['translateResult'][0][0]['tgt'])

    print('请等待5秒')
    time.sleep(5)