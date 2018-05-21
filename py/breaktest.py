import sys

def test(num):
	for x in range(num):
		try:
			sys.stdout.write(str(x))
			sys.stdout.flush()
		except KeyboardInterrupt:
			print '\nStopping at', x
			break
	print 'All done'

if __name__ == '__main__':
	test(100000)