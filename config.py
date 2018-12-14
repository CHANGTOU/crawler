import os

#爬取页数范围（0....n)
PAGE_RANG = range(0, 100)

#设置请求头信息，更换自己的Cookie
HEADERS = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
    'Cookie':'_ga=GA1.2.130903612.1524213531; rxx=33ovhav8kcs.13fes53n&v=1; __unam=b3ca5e5-162e234fed3-532955b8-2; yx=5zewc25q7yshg%26o%3D3%26f%3D78; __gads=ID=c00dae29106b9b74:T=1534497446:S=ALNI_MZStqQVb3ayqkLRQI2SeJBI0qAmYQ; tmgioct=5b84eb0fb27b890852657300; nts=false; devicePixelRatio=2; documentWidth=1280; __utma=189990958.130903612.1524213531.1543803542.1544760424.21; __utmb=189990958.0.10.1544760424; __utmc=189990958; __utmz=189990958.1544760424.21.12.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _gid=GA1.2.1707704894.1544760424; capture=hEWK8pTfE0XW5EIhWIiDEe6Fqk; pfl=ZTA1NTEwNzJhOGY5ODEzMzVjYjViZWEyMGJiZmI4M2YwYmZlYTZlNTNkZmUwMDdiZjI3ZjhlOTdhMDRiMGM2MCw2NTRtdnQ5eGJodGZ0ZnM0d3VjNm02dXVkbng3YWZ4ZCwxNTQ0NzYxMTU0; pfp=aJHBoN0kQDLTdAdPvQ5KZdNZqziVN2mG2NocM9N3; pfs=mmmSx3OmYG2q53R4QoWW2DplMcg; pfe=1552537164; pfu=181925792; language=%2Czh_CN; logged_in=1; pfx=46454f6393e0613e588df91429dd50d4b463413a774f15b6e091b13aaa014801%230%238506661333; pfg=b09235fb40dfdf9abe37d614553c19be36af71329bc2d2e24189f36e513b888b%23%7B%22gdpr_is_acceptable_age%22%3A1%2C%22exp%22%3A1576297189%2C%22vc%22%3A%22%22%7D%234785327194'
}

#爬取图片存储路径
DIR_PATH = os.path.join(os.path.abspath('.'), 'images')

#设置代理http 或者 socket
PROXIES = {
  "http": "http://127.0.0.1:1087",
  "https": "http://127.0.0.1:1087",
}
