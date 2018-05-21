def unixFormat(fname):
	'''
	Remove all the stupid \\r newline things from files
	writen on a windows box
	'''
	import os
	f = open(fname)
	r = f.read().replace('\r','')
	f.close()
	os.remove(fname)
	f = open(fname, 'w+')
	f.write(r)
	f.close()

if __name__ == '__main__':
	import sys
	unixFormat(sys.argv[1])