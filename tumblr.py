from multiprocessing import pool
from hashlib import md5
from config import *
from bs4 import BeautifulSoup
import re, os, time
import json
import requests
import threading

#存储图片
def save_image(content, url):
    file_path = '{}/{}{}'.format(DIR_PATH, md5(content).hexdigest(), '.'+url.split('.')[-1])
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as file:
            file.write(content)

#下载图片
def download_image(url):
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '下载成功-->',url)
    try:
        requests.adapters.DEFAULT_RETRIES = 5
        respones = requests.get(url ,timeout = 20 ,proxies=PROXIES)
        if respones.status_code == 200:
            #存图片
            save_image(respones.content ,url)
        else:
            print('图片下载失败')
    except requests.exceptions.ConnectionError as error:
        print('图片失败：' + str(error))

#获取筛选数据
def get_home(page):
    url = 'https://www.tumblr.com/dashboard/'+str(page)
    try:
        r = requests.get(url, headers = HEADERS ,proxies=PROXIES)
        if r.status_code == 200:
            try:
                soup = BeautifulSoup(r.text ,'lxml')
                photo = soup.select('.post_media_photo')
                photoUrl = [item['src'] for item in photo]
                photoSet = soup.select('.photoset_photo')
                photoSetUrl = [item['href'] for item in photoSet]
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '正在下载第{}页'.format(page))
                for imgUrl in photoSetUrl+photoUrl:
                    #多线程下载图片
                    t = threading.Thread(target=download_image, args=(imgUrl,))
                    t.start()
            except BaseException as e:
                print('解析错误：' + str(e))
        else:
            print('列表请求失败')
    except requests.exceptions.ConnectionError as error:
        print('列表失败：' + str(error))

def start(page):
    print('开始--------->>')

    if not os.path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)
    start_time = time.time()
    start_file_count = len([x for x in os.listdir(DIR_PATH)])
    #多进程
    p = pool.Pool()
    p.map(get_home ,list(PAGE_RANG))
    p.close()
    p.join()
    end_time = time.time()
    end_file_count = len([x for x in os.listdir(DIR_PATH)])

    print('结束--------->>','耗时{}s'.format(int(end_time - start_time)),'保存{}个'.format(end_file_count-start_file_count),'总共{}个'.format(end_file_count))

if __name__ == '__main__':
    start(PAGE_RANG)