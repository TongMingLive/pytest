# 从网络爬取照片并下载
import urllib.request

response = urllib.request.urlopen('http://placekitten.com/g/500/600')
cat_img = response.read()

with open('../../../filetest/cat_img_file.jpg','wb') as cat_img_file:
    cat_img_file.write(cat_img)