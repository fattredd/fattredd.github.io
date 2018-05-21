# Catalogue all entries on a camera site
import requests
from bs4 import BeautifulSoup as bs
from collections import defaultdict
import pickle

mainDict = defaultdict(list)

def getPage(num):
	return 'http://www.insecam.org/en/bycountry/US/?page='+str(num)

def getContent(num):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
	}
	response = requests.get(getPage(num), headers=headers)
	return bs(response.text, 'html.parser')

def getIP(subPage):
	headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0'
	}
	r = requests.get('http://insecam.org'+subPage, headers=headers)
	content = r.text.encode('utf-8')
	soup = bs(content, 'html.parser')
	#print(content)
	print('\t  Finding IP at', subPage)
	try:
		ip = soup.find('img', class_='thumbnailimgfullsize').parent['href']
	except AttributeError:
		try:
			import re
			js = soup.find_all('div',class_='detailcenter')[1].script.text
			m = re.search('(?<=href=\\\')[a-zA-Z0-9\:\@\.\/]+(?=\\\')', js)
			ip = m.group(0)
		except AttributeError:
			return None
	return ip

def parsePage(num):
	page = getContent(num)
	cameras = list(page.find_all('div', class_='thumbnail'))
	print(len(cameras), 'cameras found on page', num)
	d1 = defaultdict(list)
	for cam in cameras:
		name = cam.a['title'].split(', ')[1]
		ip = getIP(cam.a['href'])
		d1[name].append(ip)
		print('\t',name,'processed')
	return d1

def doThings(num=940):
	for i in range(num):
		mainDict.update(parsePage(i))
		print('Finished', i)
		if i%10 == 0:
			f=open('output.txt','w+')
			pickle.dump(mainDict,f)
			f.close()

doThings()