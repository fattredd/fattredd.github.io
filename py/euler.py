#euler problem 16
import sys
println = sys.stdout.write

def addDigits(x):
	l = [int(i) for i in list(str(x))]
	return sum(l)

#problem 5
def smallest(x):
	num = 0
	while True:
		check = 0
		num += 1
		println('\nChecking '+str(num)+'-')
		for i in range(1,x+1):
			println(str(i)+' - ')
			if num%i == 0:
				check += 1
			else:
				break
		if x == check:
			return num

def factorial(x):
	out = 1
	for i in range(1,x+1):
		out *= i
	return out