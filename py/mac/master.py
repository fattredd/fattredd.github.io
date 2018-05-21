import pickle, sys
s = []
for arg in sys.argv:
	s.append(arg)
f=open(s[1],'r')
r=f.read()
f.close()
lex=r.split('\n')
master=[]

for li in lex:
	line=[]
	curChar=' '
	buffL=[curChar,0]
	for char in li:
		if char == curChar:
			buffL[1] += 1
		else:
			line.append((buffL[0],buffL[1]))
			curChar = char
			buffL = [curChar, 1]
	line.append((buffL[0],buffL[1]))
	master.append(line)

q=pickle.dumps(master)
sys.stdout.write(q)
