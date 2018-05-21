#Time based art
import time
import turtle

for times in range(10):
	t = time.time()
	ts = str(t).replace('.','')
	# xxnn
	# x - right(xx*4)
	# n - forward(nn*10)
	sets=[]
	for x in range(4):
		out = [int(ts[x::4][::2]),int(ts[x::4][1::2])]
		sets.append(out)
	color = (
		round(1/int(ts[::-8]),2),
		round(1/int(ts[1::-8]),2),
		round(1/int(ts[2::-8]),2))
	turtle.pencolor(color)
	for x in sets:
		turtle.right(x[0]*2)
		turtle.forward(x[1])
	turtle.dot(5)
	turtle.pu()
	turtle.setpos(0,0)
	turtle.pd()
time.sleep(10)
