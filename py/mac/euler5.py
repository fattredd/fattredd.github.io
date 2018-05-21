#'''
def magicUp(i=232792560,show=10,to=20):
	out=0
	vals=[11,12,13,14,15,16,17,18,19,20]
	while True:
		i+=1
		curr=[]
		num=True
		for x in range(2,to+1):
			if not i%x==0:
				num = False
				break
			else:
				curr.append(x)
		if num == True:
			out=i
			print i,len(str(i)),len(dispNums(curr)),dispNums(curr)
			break
		res = dispNums(curr)
		if len(res)>show:
			print i,len(str(i)),len(res),res
	return out #'''

#'''
i=89369280
def magicDown(i,show=10,to=20):
	vals = [11,12,13,14,15,16,17,18,19,20]
	out=0
	while True:
		i-=1
		curr=[]
		num=True
		for x in range(2,to+1):
			if not i%x==0:
				num = False
				break
			else:
				curr.append(x)
		if num == True:
			out=i
			print i,len(str(i)),len(dispNums(curr)),dispNums(curr)
			break
		if len(dispNums(curr))>show:
			print i,len(str(i)),len(dispNums(curr)),dispNums(curr)
	return out #'''

from collections import defaultdict
from pprint import pprint
def n(i):
	out=[]
	for x in range(2,i):
		if i%x==0:
			out.append(x)
	out.append(i)
	return out

def Cdict():
	out=defaultdict(list)
	for x in range(21):
		curr=n(x)
		#print x,curr
		for i in curr:
			out[str(x)].append(i)
	return dict(out)

def dispNums(L):
	d=Cdict()
	out=[]
	for x in L: #Numbers given to me
		for i in d[str(x)]: #Derived numbers
			if not i in out:
				out.append(i)
	out.sort()
	return out

def LtoS(L):
	return ', '.join(str(x) for x in L)

def takeT(i=89369280,show=10,to=20):
	ti=time.time()
	try:
		e=magicUp(i,show,to)
	except:
		e=[]
		tTime = str(int(time.time()-ti)/60)
		print tTime+' mintutes'
	tTime = str(int(time.time()-ti)/60)
	print tTime+' minutes'
	return e

def anotherTrick(i=89369280):
	pass


