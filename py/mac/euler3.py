def factors(x,max=0):
	if max==0:
		max=x/100000
	out=[]
	for y in xrange(1,max):
		i = x-y
		if i%100==0:
			print 'Factoring...',str(round((float(y)/max)*100,3))+'%',i
		if x%i==0:
			out.append(i)
			print 'Solution 1:',i
	return out

def isprime(num):
	for x in range(1,num-1):
		#print num%(num-x),x
		if num%(num-x)==0:
			return False
	return True

def both(num=600851475143):
	out=[]
	f = factors(num)
	f.sort()
	prime=[]
	for factor in f:
		print 'Checking factors:',f
		if isPrime(factor):
			out.append(factor)
			print 'Prime factor found',factor
	out.sort()
	return out