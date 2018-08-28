import os

#请求代理
PROXIES = {
    'http': 'socks5://127.0.0.1:1086',
    'https': 'socks5://127.0.0.1:1086'
}
#请求头
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Cookie':'xxx'
}

#存储图片路径
DIR_PATH = os.path.join(os.path.abspath('.'), 'images')

#请求页数范围（0....n)
PAGE_RANG = range(0, 50)
