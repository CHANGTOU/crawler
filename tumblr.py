# coding: utf-8
from hashlib import md5
from config import *
from bs4 import BeautifulSoup
import re, os, time
import json
import requests
import threading

#第一个页面
first_page_link = 'https://www.tumblr.com'
#下一个页面
next_page_link = '/dashboard/0'

#存储图片
def save_image(content, url):
	file_path = '{}/{}{}'.format(DIR_PATH, md5(content).hexdigest(), '.'+url.split('.')[-1])
	if not os.path.exists(file_path):
		with open(file_path, 'wb') as file:
			file.write(content)
			
#下载图片
def download_image(url):
	try:
		requests.adapters.DEFAULT_RETRIES = 5
		respones = requests.get(url ,timeout = 20 ,proxies=PROXIES)
		if respones.status_code == 200:
			print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '\n图片下载成功-->',url)
			#存图片
			save_image(respones.content ,url)
		else:
			print('图片下载失败')
	except requests.exceptions.ConnectionError as error:
		print('图片失败：' + str(error))
		
#获取筛选数据
def get_page_image(url):
	print(url)
	try:
		r = requests.get(url, headers = HEADERS ,proxies=PROXIES)
		if r.status_code == 200:
			try:
				soup = BeautifulSoup(r.text, "lxml")
				# 下一页链接
				next_page = soup.select_one('#next_page_link')
				global next_page_link
				next_page_link = next_page['href']
				# 单张图片
				photo = soup.select('.post_media_photo')
				photo_urls = [item['src'] for item in photo]
				# 集合图片
				photoSet = soup.select(".photoset_photo rapid-noclick-resp")
				photoSet_urls = [item['href'] for item in photoSet]
				for url in photo_urls + photoSet_urls:
					#多线程下载图片
					t = threading.Thread(target=download_image, args=(url,))
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

	for page in list(range(page)):
		print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), '\n下载第{}页图片'.format(page))
		get_page_image(first_page_link + next_page_link)

	end_time = time.time()
	end_file_count = len([x for x in os.listdir(DIR_PATH)])
	
	print('结束--------->>','耗时{}s'.format(int(end_time - start_time)),'保存{}个'.format(end_file_count-start_file_count),'总共{}个'.format(end_file_count))
	
if __name__ == '__main__':
	start(PAGE_COUNT)

