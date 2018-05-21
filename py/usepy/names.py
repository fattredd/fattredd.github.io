import os

def check(x,output=False):
	names = []
	path = 'W:\\home\\{0}\\'.format(str(x))
	os.chdir(path)
	availLetters = os.listdir('.')
	for a in availLetters:
		if not os.path.isfile(a):
			new = os.listdir(a)
			names += new
			if output:
				print x, a, 'Completed', len(new)
	return names

def all(r=16,verb=False):
	out = []
	for x in range(r):
		new = check(x,verb)
		out += new
		print '** {0} Completed: {1} **'.format(x, len(new))
	return out

def listOut(l, save='V:\\accounts.txt'):
	l.sort()
	s = '\n'.join(l)
	f = open(save, 'w+')
	f.write(s)
	f.close()
	return True

def toEmail(l):
	out = []
	for name in l:
		name += '@psu.edu'
		out.append(name)
	return out

def pour(output=False):
	name=[]
	os.chdir('U:\\')
	lets1 = os.listdir('.')
	for let1 in lets1:
		if not os.path.isfile(let1):
			lets2 = os.listdir(let1)
			for let2 in lets2:
				name += os.listdir(let1+'\\'+let2)
	return names
 