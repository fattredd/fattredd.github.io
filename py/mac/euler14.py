def iterate(num,a=1):
	#print a,num
	if num == 1:
		return a
	if num%2==0:	#even
		next = num/2
	else:
		next = (3*num)+1
	return iterate(next,a+1)

def bigGuy(num):
	l=okay(num)
	k=l
	k.sort()
	max = k[-1]
	print 'max',max
	return l

def okay(num):
	l=[0]*num
	for x in range(num-1):
		print num-x, iterate(num-x)
		l[x] = iterate(num-x)
	return l