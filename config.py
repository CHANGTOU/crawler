import os

#请求代理
PROXIES = {
    'http': 'socks5://127.0.0.1:1086',
    'https': 'socks5://127.0.0.1:1086'
}
#请求头
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Cookie':'_ga=GA1.2.130903612.1524213531; rxx=33ovhav8kcs.13fes53n&v=1; __unam=b3ca5e5-162e234fed3-532955b8-2; yx=5zewc25q7yshg%26o%3D3%26f%3D78; __utmc=189990958; nts=false; capture=GM9WbaurZ9GpagyMInEYgOqukg; __utmz=189990958.1533880678.7.6.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); tmgioct=5b73963143b6530237443910; _gid=GA1.2.1499411357.1534497445; devicePixelRatio=2; documentWidth=1280; __gads=ID=c00dae29106b9b74:T=1534497446:S=ALNI_MZStqQVb3ayqkLRQI2SeJBI0qAmYQ; __utma=189990958.130903612.1524213531.1534497445.1534500169.12; __utmb=189990958.0.10.1534500169; pfl=ZDc5Zjk1NDA1ZjVjMWM0MzNmZTYyYjgyZGFhZGQyMjg0ZTcxMmQwOTkxOWQwNjc2MWJlOTQ5MTliZDg1ZTcwOSxuMnozODZoODR2YzJjOWFodXhlOHc1bXQyNjJzYzZrYSwxNTM0NTAwMTgw; pfp=dgrRXBqhvGG1RQianriVfblXIVPw2zch6QVo2HVE; pfs=adWBNOTdf480x49hVTNaoS5V2XU; pfe=1542276193; pfu=336713838; pfx=b8ed0ba100fb784e301dc2d1b4e384526b648f030a1a2d5bbf11abb09b94b9c2%230%233029088130; language=%2Czh_CN; logged_in=1; pfg=1456f80aee37ca180d41d5ff9384fa1952c7c04875b50693f3ddb6109663b2d9%23%7B%22gdpr_is_acceptable_age%22%3A1%2C%22exp%22%3A1566036205%2C%22vc%22%3A%22%22%7D%230655655001'
}

#存储图片路径
DIR_PATH = os.path.join(os.path.abspath('.'), 'images')

#请求页数范围（0....n)
PAGE_RANG = range(0, 50)
