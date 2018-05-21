# Word Snake
ip = "SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE"

def verify(s):
	l=s.split(" ")
	buf = l[0][0]
	for item in l:
		#print item
		#print "\t",buf, item[0]
		if buf != item[0]:
			return False
		buf=item[::-1][0]
		#print "\tSetting buf to:",buf
	return True

if verify(ip):
	for item in ip