# Dice bitch
# V1.5
# Added fudge dice
# V1.0
# Initial
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
	if dice[1] == 'f':
		for i in range(int(dice[0])):
			roll = random.randint(-1,1)
			out.append(roll)
	else:
		for i in range(int(dice[0])):
			roll = random.randint(1,int(dice[1]))
			out.append(roll)
	if dice[1] == 'f':
		for i in range(int(dice[0])):
			roll = random.randint(-1,1)
			out.append(roll)
	return out

# Handle multiple rolls
def multiroll(s):
	dice = s.split(' ')
	out = []
	for i in dice:
		cur = roll(i)
		out += cur
	return out


# Special operations for cmd line
def pirate(l,ignore=False):
	success = 0
	for x in l:
		if x == 1:
			success += 1
		if x == 6:
			success += 1
			r=roll('1d6')
			l.append(r)
	if ignore:
		return success, l
	else:
		return success

def add(l, ignore=False):
	out = 0
	for i in l:
		out += int(i)
	if ignore:
		return out, l
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
			s = s.replace(x,'')
			if 'list' in s:
				s.replace('list','')
				l = True
			if 'l' in s:
				s.replace('l','')
				l = True
			else:
				l = False
			s = multiroll(s)
			out = operations[x](s,l)
			return out
	out = multiroll(s)
	return out

if __name__ == '__main__':
	import sys
	print parse(' '.join(sys.argv[1:]))
