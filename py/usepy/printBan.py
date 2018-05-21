import sys, pickle

def pBan(data):
	for line in data:
		for char, count in line:
			sys.stdout.write(char * count)
		sys.stdout.write('\n')

def pLoad(name):
	f = open(name)
	out = pickle.loads(f.read())
	f.close()
	return out

if __name__ == '__main__':
	pBan(pLoad(sys.argv[1]))