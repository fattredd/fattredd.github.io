# http://api.4chan.org/b/0.json
import urllib2
import json, pickle
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' }

def download(name, board='b'):
	url = 'http://i.4cdn.org/'+board+'/src/'
	url += str(name)
	try:
		#r = urllib2.Request(url, headers=headers)
		img = urllib2.urlopen(url).read()
		f = open(str(name),'wb+')
		f.write(img)
		f.close()
		print 'Downloaded', name
		return True
	except urllib2.HTTPError:
		print 'Trouble downloading', name
		return False

def findImg(num, board='b'):
	url = 'http://a.4cdn.org/'+board
	url += '/res/'+str(num)+'.json'
	try:
		w = urllib2.urlopen(url)
	except urllib2.HTTPError:
		print 'Welp. 404. Get fucked I guess.'
		print 'The id is probably old.\n'
		print 'python downloader.py [board] [id]'
		return False
	r = w.read()
	j = json.loads(r)
	thread = j['posts']
	for post in thread:
		if 'tim' in post.keys():
			name = str(post['tim'])
			ext = str(post['ext'])
			filename = name+ext
			if not checkLog(name, board):
				 if download(filename,board):
					addLog(name, board) #'''
	return True

def checkLog(num, board):
	f = open(board+'.txt','w+')
	current = f.readlines()
	if num in current:
		return True
	else:
		return False

def addLog(num, board):
	f = open(board+'.txt','a')
	f.write('\n'+str(num))
	f.close()

def addCurrent(num, board):
	f = open('current.txt','a')
	f.write('\n'+num+'|'+board)
	f.close()

def runCurrents():
	f = open('current.txt','w+')
	allCur = []
	for cur in f.readlines():
		allCur.append(cur.split('|'))
	for x in allCur:
		print x

if __name__ == '__main__':
	import sys
	try:
		q = sys.argv
		findImg(q[2],q[1])
	except:
		print 'python downloader.py [board] [id]'