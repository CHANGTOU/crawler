# Tumblr-Spider

1.在config.py文件中设置Soket5代理(梯子)  
2.在config.py文件中设置Cookie（在浏览器中登陆tumblr，查看Cookie）   
3.默认在当前文件夹下生成images文件夹，存储图片，并过滤掉重复图片

```
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
#请求页数范围（0....n)
PAGE_RANG = range(0, 1)
```
