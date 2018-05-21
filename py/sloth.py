f,n,r=open('i','r'),0,f.read().split('\n')
for i in r:n+=i;f.close()
l,t,a=len(n),[int(i) for i in r],t/float(l)
print 'A',l,'\nT',t,'\nv',a