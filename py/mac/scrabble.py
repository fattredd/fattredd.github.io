scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
		 "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
		 "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
		 "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
		 "x": 8, "z": 10}
import sys, copy
usable = sys.argv[1].lower()
print usable
letters=[]
for l in usable:
	letters.append(l)

f = open('sowpods.txt','r')
q = f.read()
f.close()
s = q.split('\r\n')
words=[]
for x in s:
	words.append(x.lower())

possible=[]
for word in words:
	left=copy.deepcopy(letters)
	poss=True
	for l in word:
		if not l in left:
			poss=False
			break
		else:
			w=left.pop(left.index(l))
	if poss:
		possible.append(word)

possible.sort()
for word in possible:
	num = 0
	for l in word:
		num += scores[l]
	print num, word
