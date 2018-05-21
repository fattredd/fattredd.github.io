# Create rediiculous amounts of nested folders for no reason at all
import os, sys, time

def makeFolders(amount, location='.', rep=100):
	amount = int(amount)
	os.chdir(location)
	start = os.path.abspath('.')
	startTime = time.time()
	lastTime = startTime
	for x in range(amount):
		try:
			os.mkdir(str(x))
			os.chdir(str(x))
			if x%rep == 0:
				sys.stdout.write('\nM - '+str(x)+' -- '+str(time.time()-lastTime))
				lastTime = time.time()
				sys.stdout.flush()
		except OSError:
			sys.stdout.write('\nError; '+ str(sys.exc_info()[0]))
			sys.stdout.write('\n\nError occured at folder '+
				str(x) + '. Stopping.\n')
			sys.stdout.flush()
			break
		except KeyboardInterrupt:
			sys.stdout.write('\nError;' + str(sys.exc_info()[0]))
			sys.stdout.write('\n\nCtrl+C pressed. Stopping at '+
				str(x) + ' folders.\n')
			sys.stdout.flush()
			break
	sys.stdout.write('\n\nTotal time:'+str(time.time()-startTime))
	sys.stdout.flush()
	os.chdir(start)


def rmFolders(location='.', debug=True):
	os.chdir(location)
	num = count('.', debug)
	if debug:
		sys.stdout.write('\nRunning down the tree:')
		sys.stdout.flush()
	for i in num:
		os.chdir(i)
		if debug:
			sys.stdout.write('\nT - '+str(i))
			sys.stdout.flush()
	os.chdir('..')
	if debug:
		sys.stdout.write('\nDeleting folders:')
		sys.stdout.flush()
	for i in range(num)[::-1]:
		os.rmdir(str(i))
		os.chdir('..')
		if debug:
			sys.stdout.write('\nD - '+str(i))
			sys.stdout.flush()
	start = os.path.abspath('.')

def rmdir(location='.', folder=0):
	start = os.path.abspath('.')
	os.chdir('location')
	cmd = 'rm -rf ' + str(folder)
	os.system(cmd)

def count(location, debug=False):
	os.chdir(location)
	start = os.path.abspath('.')
	num = 0
	os.chdir('0')
	if debug:
		sys.stdout.write('\nCounting Folders...')
		sys.stdout.flush()
	curdir = os.listdir('.')
	while not curdir == []:
		os.chdir(curdir[0])
		sys.stdout.write('\nC - '+curdir[0])
		curdir = os.listdir('.')
	final = os.path.abspath('.').split('/')
	os.chdir(start)
	return final
