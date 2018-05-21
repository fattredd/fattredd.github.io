#Time based art
import time
import turtle

turtle.ht()
turtle.speed(0)
for times in range(1000):
	t = time.time()
	ts = str(t).replace('.','').zfill(16)
	# ab [c] [de] [fg] [h] [j] [klmnop]
	# 01  2   34   56   7   8   9
	# c fill
	# de rotation
	# fg distance/size
	# h circle? h>=5
	# j relative pen size
	# k-p color of line
	color = (
		round(10/int(ts[10:12]),2) if int(ts[10:12])>=10 else 0,
		round(10/int(ts[12:14]),2) if int(ts[12:14])>=10 else 0,
		round(10/int(ts[14:16]),2) if int(ts[14:16])>=10 else 0)
	sets={
		'rot': int(ts[4:6]),
		'size': int(ts[6:8]),
		'circle': True if int(ts[8:9])>4 else False,
		'psize': int(ts[9:10])/2,
		'color': color,
		'fill': True if int(ts[1:2])>4 else False
	}
	turtle.color(sets['color'])
	turtle.pensize(sets['psize'])
	turtle.right(sets['rot'])
	if sets['circle']:
		turtle.begin_fill()
		turtle.circle(sets['size'])
		turtle.end_fill()
	else:
		turtle.forward(sets['size'])
		#turtle.dot(5)
	'''
	turtle.pu()
	turtle.setpos(0,0)
	turtle.pd()#'''
time.sleep(10)
