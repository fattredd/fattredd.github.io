
def getMap(fname='map.m'):
	f = open(fname,'r')
	r = f.read().split('\n')
	f.close()
	out = []
	for line in r:
		out.append(list(line.ljust(len(r),' ')))
	return out

def simSand(inmap):
	smap = inmap[:]
	maxr = len(smap)
	for y, row in enumerate(smap):
		for x, col in enumerate(row):
			if col == '.' and y < maxr-1:
				if smap[y+1][x] == ' ':
					smap[y+1][x] = '.'
					smap[y][x] = ' '
	return smap

def showMap(inmap):
	for line in inmap:
		print ''.join(line)

if __name__ == '__main__':
	smap = getMap()
	for x in range(10):
		simSand(smap)
	showMap(smap)