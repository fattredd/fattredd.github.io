def isprime(num):
	if num <= 1:
		return False
	for x in range(1,num-1):
		#print num%(num-x),x
		if num%(num-x)==0:
			return False
	return True

def countEm(max=2000000,start=0):
	out=[]
	fact=2
	for x in xrange(start,max):
		if x%100==0:
			print 'Checking...',str(int((x*100)/max))+'%',x,len(out)
		if len(Prime(x))==1:
			out.append(x)
	return out

def addEm(L):
	sum=0
	for x in L:
		sum += x
	return sum

def Prime(max=2000000):
	num=max
	fact=2
	out=[]
	while (num>1):
		while(num%fact == 0):
			#print(fact)
			out.append(fact)
			if len(out)>1:
				break
			num = num/fact
		fact += 1
		if len(out)>1:
			break
	return out


