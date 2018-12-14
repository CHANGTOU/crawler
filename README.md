# tumblr

1.在 `config.py` 文件中设置代理  
2.在 `config.py` 文件中设置Cookie（在浏览器中登陆tumblr，查看Cookie）     
3.默认在当前文件夹下生成images文件夹，存储图片，并过滤掉重复图片

```Python
#爬取页数范围（0....n)
PAGE_RANG = range(0, 100)

#设置请求头信息，更换自己的Cookie
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Cookie':'自己的Cookie'
}

#爬取图片存储路径
DIR_PATH = os.path.join(os.path.abspath('.'), 'images')

#设置代理http 或者 socket
PROXIES = {
  "http": "http://127.0.0.1:1087",
  "https": "http://127.0.0.1:1087",
}

```

如图
![控制台输出](https://github.com/yichahucha/tumblr_spider/blob/master/83F7D630-5733-4EA8-8C75-5B7BE3643D75.png?raw=true)

