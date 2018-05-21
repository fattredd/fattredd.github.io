# Dice bitch
# V1.0
# fattredd
import random

# A single roll. Given as a string '2d6'
def roll(s):
	dice = s.split('d')
	if not len(dice) == 2:
		return []
	if dice[0] == '':
		dice[0] = 1
	out = []
	for i in range(int(dice[0])):
		roll = random.randint(1,int(dice[1]))
		out.append(roll)
	return out

# Handle multiple rolls
def multiroll(s,l=False):
	dice = s.split(' ')
	out = []
	if l:
		mem = []
	for i in dice:
		cur = roll(i)
		out += cur
		if l:
			mem += cur
	if l:
		return out, mem
	else:
		return out


# Special operations for cmd line
def pirate(l,ignore=None):
	success = 0
	for x in l:
		if x == 1:
			success += 1
		if x == 6:
			success += 1
			r=roll('1d6')
			l.append(r)
	if not ignore == None:
		return success, ignore
	else:
		return success

def add(l, ignore=None):
	out = 0
	for i in l:
		out += int(i)
	if not ignore == None:
		return out, ignore
	else:
		return out

operations = {
	'sum': add,
	'add': add,
	'total': add,
	'pirate': pirate,
	'p':pirate
}

# CMD line handling
def parse(s):
	for x in operations.keys():
		if x in s:
			# fancy shit that returns the list of
			# die rolled along with the operation
			if 'list' in s:
				s.replace('list','')
				l = True
			else:
				l = False
			ns = s.replace(x,'')
			ns = multiroll(ns,l)
			if l:
				out = operations[x](ns[0],ns[1])
			else:
				out = operations[x](ns)
			return out
	out = multiroll(s)
	return out

if __name__ == '__main__':
	import sys
	print parse(' '.join(sys.argv[1:]))
