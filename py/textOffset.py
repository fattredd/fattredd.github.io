import msvcrt as m
import time
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def wait():
	key = m.getch()

def offsetStr(string, num=1):
	out = '' #23
	for x in string:
		if x in alpha:
			newNum = ord(x)-65+num
			if newNum > 25:
				newNum = newNum%26
			elif newNum < 0:
				newNum += 26
			out += chr(newNum+65)
		else:
			out += x
	return out

def fileR(name='gf.txt'):
	f = open(name,'r')
	out = f.read().split('\n')
	f.close()
	return out

def fileW(textL, name='gf2.txt'):
	f = open(name, 'w+')
	f.write('\n'.join(textL))
	f.close()

def tryRange(string, num, inum=0):
	for i in range(inum,num):
		print i, offsetStr(string, i)
		wait()

def doAll(L,off):
	out = []
	for x in L:
		out.append(offsetStr(x,off))
	fileW(out)