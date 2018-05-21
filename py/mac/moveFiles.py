import os

def countFiles(dir='.',getList=False):
	a=os.listdir(dir)
	if getList:
		return a
	else:
		return len(a)

def getAmount(num=1,dir='.',prefix='Renamed PN Pictures-'):
	out=[]
	for x in range(num):
		try:
			os.chdir(prefix+str(num))
		except:
			break
		out.append(countFiles())
		os.chdir('..')
	return out
