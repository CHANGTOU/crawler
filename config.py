# coding: utf-8
import os

#爬取页数
PAGE_COUNT = 10

#设置请求头信息，更换自己的Cookie
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Cookie':'你的Cookie'
}

#爬取图片存储路径
DIR_PATH = os.path.join(os.path.abspath('.'), 'images')

#设置代理http 或者 socket
PROXIES = {
  "http": "http://127.0.0.1:7890",
  "https": "http://127.0.0.1:7890",
}
