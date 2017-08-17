import os
import urllib.request

def url_open(url):
    request = urllib.request.Request(url)
    request.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_page(url):
    html = str(url_open(url).decode('utf-8'))
    a = html.find('current-comment-page')+23
    b = html.find(']',a)
    return html[a:b]

def find_imgs(page_url):
    html = str(url_open(page_url).decode('utf-8'))
    img_addrs = []
    a = html.find('img src=')
    while a!=-1:
        b = html.find('.jpg',a,a+255)
        if b!=-1:
            img_addrs.append('http:'+html[a+9:b+4])
        else:
            b=a+9
        a = html.find('img src=',b)

    for each in img_addrs:
        print(each)

    return img_addrs


def save_imgs(float, img_addrs):
    for each in img_addrs:
        filename = str(each).split('/')[-1]
        with open(filename,'wb') as file:
            img = url_open(each)
            file.write(img)


def download_mz(folder='OOXX', pages=2):
    os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(float,img_addrs)

    print('下载完成')

if __name__ == "__main__":
    download_mz(2)