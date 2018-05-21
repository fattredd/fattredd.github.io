
#############################################################
#############		intGen.py by fattredd		#############
#############################################################
#  Usage: python intGen.py [amount] [lowRange] [highRange]  #
#     amount : the number of integers to output.			#
#				May be an expression.						#
#				D:100										#
#   lowRange : the lowest possible output.					#
#				D:0											#
#  highRange : the highest possible output.					#
#				D:0											#
#															#
#  To save the output to a file:							#
#		python intGen.py [100] [0] [9] > output.txt			#
#############################################################

from sys import stdout
from sys import argv
from random import randint
def isInt(s):
	try: 
		int(s)
		return True
	except ValueError:
		return False

def sudo(val='100',mi=0,ma=9):
	i=0
	if isInt(val):
		val = 'i<'+str(val)
	if not isInt(mi):
		mi=0
	else:
		mi=int(mi)
	if not isInt(mi):
		ma=9
	else:
		ma=int(ma)
	while (eval(val)):
		i+=1
		out=str(randint(mi,ma))
		stdout.write(out)

s=[]
for arg in argv:
	s.append(arg)
try:
	r=str(s[1])
except:
	r='100'
try:
	mi=int(s[2])
except:
	mi=0
try:
	ma=int(s[3])
except:
	ma=9
if r=='help' or r=='-help' or r=='-h' or r=='-?' or r=='?':
	print '\nUsage: python intGen.py [amount] [lowRange] [highRange]\n\
     amount : the number of integers to output. May be an expression. D:100\n\
   lowRange : the lowest possible output. D:0\n\
  highRange : the highest possible output. D:0\n\n\
To save the output to a file:\n\
\tpython intGen.py [100] [0] [9] > output.txt\n'
else:
	if isInt(r):
		sudo(int(r),mi,ma)
	if isInt(eval(r)):
		sudo(eval(r),mi,ma)
	else:
		sudo(100,mi,ma)

