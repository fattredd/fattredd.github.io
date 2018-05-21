import pickle

f = open(sys.argv[1],'r')
r = f.read()
f.close()
lex = r.split('\n')
out = []

for li in lex:
	line = []
	currentChar = ' '
	buffL = [currentChar,0]
	for char in li:
		if char == currentChar:
			buffL[1] += 1
		else:
			line.append((buffL[0],buffL[1]))
			currentChar = char
			buffL = [currentChar, 1]
	line.append((buffL[0],buffL[1]))
	out.append(line)

q = pickle.dumps(out)
sys.stdout.write(q)
