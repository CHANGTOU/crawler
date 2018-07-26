
from multiprocessing import pool
from hashlib import md5
from config import *
from bs4 import BeautifulSoup
import re, os, time
import json
import requests


#存储图片
def save_image(content, url):
    file_path = '{}/{}{}'.format(DIR_PATH, md5(content).hexdigest(), '.'+url.split('.')[-1])
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as file:
            file.write(content)

#下载图片
def download_image(url):
    time.sleep(0.1)
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '下载成功-->',url)
    try:
        requests.adapters.DEFAULT_RETRIES = 5
        respones = requests.get(url ,timeout = 20 ,proxies=PROXIES)
        if respones.status_code == 200:
            #存图片
            save_image(respones.content ,url)
            return respones.content
        else:
            print('图片下载失败')
            return None
    except requests.exceptions.ConnectionError:
        print('图片下载失败')
        return None

#获取筛选数据
def get_home(page):
    time.sleep(0.2)
    url = 'https://www.tumblr.com/dashboard/'+str(page)
    try:
        r = requests.get(url, headers = HEADERS ,proxies=PROXIES)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text ,'lxml')
            photo = soup.select('.post_media_photo')
            photoUrl = [item['src'] for item in photo]
            photoSet = soup.select('.photoset_photo')
            photoSetUrl = [item['href'] for item in photoSet] 
            
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '正在下载第{}页'.format(page))
            for imgUrl in photoSetUrl+photoUrl:
                #下载图片
                download_image(imgUrl)
                #存数据
                #save_to_mongo({'url':imgUrl})
            return photoSetUrl+photoUrl
        return None
    except requests.exceptions.ConnectionError:
        print('列表请求失败')
        return None

def main(page):
    get_home(page)

if __name__ == '__main__':
    print('开始--------->>')
    #存储图片路径
    DIR_PATH = os.path.join(os.path.abspath('.'), 'images')
    if not os.path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)
    start_time = time.time()
    start_file_count = len([x for x in os.listdir(DIR_PATH)])
    #多进程
    p = pool.Pool()
    p.map(main ,list(PAGE_RANG))
    p.close()
    p.join()
    end_time = time.time()
    end_file_count = len([x for x in os.listdir(DIR_PATH)])
    print('结束--------->>','耗时{}s'.format(int(end_time - start_time)),'保存{}个'.format(end_file_count-start_file_count),'总共{}个'.format(end_file_count))
