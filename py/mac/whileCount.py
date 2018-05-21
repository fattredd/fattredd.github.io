# from whileCount import *
import time
from sys import stdout
def l2(num):
	return(len(str(num)))

def countTime(to,val='sec',show=False):
	s=time.time()
	i=0
	while i<to:
		i+=1
		if show:
			stdout.write(str(i)+'-')
	t=time.time()-s
	print '\n',int(t)/60,'minutes',round(t%60,5),'seconds'
	if val=='sec':
		return t
	elif val=='num':
		return to
	elif val=='l2':
		return l2(to)

'''
# num - l2(num) - time
a = [1*(10**x) for x in range(10)]
b = [l2(x) for x in a]
c = [countTime(x) for x in a]
l=''
s=[]
for i in range(len(a)-1):
	l='# '+str(a[i])+' - '+str(b[i])+' - '+str(d[i])
	s.append('\n'+l)
f=open('whileCount.py','a')
f.write('\n')
#f.write('\'\'\')
f.write('# num - l2(num) - time\n')
for x in s:
	f.write(x)
#f.write('\'\'\'')
f.close()
'''

# 1 - 1 - 2e-06
# 10 - 2 - 2e-06
# 100 - 3 - 1.5e-05
# 1000 - 4 - 0.000145
# 10000 - 5 - 0.001447
# 100000 - 6 - 0.011814
# 1000000 - 7 - 0.091163
# 10000000 - 8 - 0.897215
# 100000000 - 9 - 9.012319
