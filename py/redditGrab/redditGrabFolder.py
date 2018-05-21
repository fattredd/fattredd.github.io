# V1.0
# Grab the top 10 images on reddit
# Then puts it in a folder based on the subreddit
# Requires PRAW
# pip install praw
#
# Use from the command line by calling
# python redditGrab.py [number] [subreddit]
#
# 
import urllib2
import pickle, os
try: # Make sure praw is installed
	import praw
except ImportError:
	print 'You dont have praw installed.'
	print 'To run this script, install praw with'
	print 'pip install praw\n'

def login():
	'''Login and return the session variabe'''
	user_agent = ('redditGrab:awesomeGrab')
	r = praw.Reddit(user_agent=user_agent)
	r.login('awesomeGrab', 'supersecret')
	return r

def loadDone():
	'''Load list of previously downloaded posts'''
	if os.path.isfile('completedFolder.p'):
		return pickle.load(open('completedFolder.p'))
	else:
		return []

def delDone():
	'''Deletes the previously downloaded log'''
	if os.path.isfile('completedFolder.p'):
		os.remove('completedFolder.p')

def saveDone(l):
	'''Save a list of downloaded posts'''
	pickle.dump(l,open('completedFolder.p','w+'))

def getPosts(lim=10, subreddit='funny', resetCompleted=False):
	'''getPosts([lim]=10, [subreddit]='funny')
	Download the top [lim] images from [subreddit]'''
	r = login()
	if resetCompleted:
		delDone()
	already_done = loadDone()
	top = r.get_subreddit(subreddit)
	if not os.path.isdir(subreddit):
		os.mkdir(subreddit)
	os.chdir(subreddit)
	print 'Scanning the first', lim, 'posts in', subreddit, 'for new images.'
	for num, entry in enumerate(top.get_hot(limit=lim)):
		if not entry.is_self and not entry.id in already_done:
			already_done.append(entry.id)
			if 'i.imgur' in entry.url:
				if '.jpg' in entry.url:
					ext = '.jpg'
				elif '.png' in entry.url:
					ext = '.png'
				elif '.gif' in entry.url:
					ext = '.gif'
				img = urllib2.urlopen(entry.url).read()
				f = open(str(entry.id)+ext, 'wb+')
				f.write(img)
				f.close()
				print 'Saved image #', num, '|| '+str(entry.id)+ext
	os.chdir('..')
	saveDone(already_done)

if __name__ == '__main__':
	import sys
	if len(sys.argv)>2:
		try:
			int(sys.argv[1])
			num = int(sys.argv[1])
			paramnum = 1
		except ValueError:
			try:
				int(sys.argv[2])
				num = int(sys.argv[2])
				paramnum = 2
			except ValueError:
				print '\nNeither of the arguments are numbers'
		if paramnum == 1:
			subreddit = sys.argv[2]
		else:
			subreddit = sys.argv[1]
		if '-r' in sys.argv:
			# To reset the download record, add -r
			reset = True
		else:
			reset = False
		if '-t' in sys.argv:
			# To keep checking every 30 seconds, add -t
			import time
			start = time.time()
			print 'Press Ctrl+C to stop'
			while True:
				getPosts(num, subreddit, reset)
				print 'Done. Waiting...'
				time.sleep(30)
				passed = round(time.time()-start,2)
				print 'Time passed:', passed, 'sec'
				reset = False
		else:
			getPosts(num, subreddit)
	else:
		getPosts()