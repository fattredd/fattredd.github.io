# 25x80
# genmap
from random import uniform
m = [0]*15
step = 1
nstep = 1

# lowerBound, upperBound, deviation
def nextint(lower, upper, dev):
	dev=int(dev)
	init = upper-lower/2
	rand = uniform(-1*dev,dev)
	return init+rand

# 0 (1) 2 [3] 4 (5) 6 {7} 8 (9) 10 [11] 12 (13) 14
m[7] = nextint(0,0,1/step)
step += nstep
m[3] = nextint(0,m[7],1/step)
m[11] = nextint(m[7],0,1/step)
step += nstep
m[1] = nextint(0,m[3],1/step)
m[5] = nextint(m[3],m[7],1/step)
m[9] = nextint(m[7],m[11],1/step)
m[13] = nextint(m[11],0,1/step)
step += nstep
m[0] = nextint(0,m[1],1/step)
m[2] = nextint(m[1],m[3],1/step)
m[4] = nextint(m[3],m[5],1/step)
m[6] = nextint(m[5],m[7],1/step)
m[8] = nextint(m[7],m[9],1/step)
m[10] = nextint(m[9],m[11],1/step)
m[12] = nextint(m[11],m[13],1/step)
m[14] = nextint(m[13],0,1/step)

print(m)
'''
for x in m:
	print'-'*(20+int(x*20)) # '''
#import numpy as np
import matplotlib.pyplot as plt
plt.plot(m)
plt.show()
