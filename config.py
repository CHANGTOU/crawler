#请求代理
PROXIES = {
    'http': 'socks5://127.0.0.1:1086',
    'https': 'socks5://127.0.0.1:1086'
}
#请求头
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Cookie':'tmgioct=5ad9a719469b140884535280; _ga=GA1.2.130903612.1524213531; rxx=33ovhav8kcs.13fes53n&v=1; __unam=b3ca5e5-162e234fed3-532955b8-2; _gid=GA1.2.2134415428.1532592399; yx=5zewc25q7yshg%26o%3D3%26f%3D78; devicePixelRatio=2; documentWidth=1280; __utma=189990958.130903612.1524213531.1525314114.1532592402.4; __utmb=189990958.0.10.1532592402; __utmc=189990958; __utmz=189990958.1532592402.4.3.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); pfl=M2QzMjc0MjVmN2IyZTNhZjg0YjAyMWI3YThhYzc2ZTFhNDBmNmQ2YzhlNzMwNzc0NGYxNDgwNWE0N2NmYmM2MyxlbWhhazQ1OXZ3NTljYnI4eGhjdmZtdjdkNXZzZmJ4MiwxNTMyNTkyNDM3; pfp=MJh93o0ZpP0XDwC0f0iDJ7P6KJzHAM6bquvXqJao; pfs=XMwyuN8nn9WYQrDCA3Canw6HbI; pfe=1540368444; pfu=181925792; pfx=50135c2a558a49709d215c546261b1569efc18a55102bb7b879e0e8130992bef%230%233074412346; language=%2Czh_CN; logged_in=1; nts=false; pfg=4ee2a302f8c1d3731354f8ad3a3ed05c839d3b4d8e99724ce2ac15f8d16490aa%23%7B%22gdpr_is_acceptable_age%22%3A1%2C%22exp%22%3A1564128477%2C%22vc%22%3A%22%22%7D%234094941845; capture=GM9WbaurZ9GpagyMInEYgOqukg'
}
#请求页数范围（0....n)
PAGE_RANG = range(0, 3)
