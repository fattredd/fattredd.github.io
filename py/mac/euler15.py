from math import factorial

def path(x):
	num = factorial(2*x)
	den = factorial(x)**2
	res = float(num)/float(den)
	return int(res)