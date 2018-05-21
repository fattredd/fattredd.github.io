import pickle
#from objfunc import *

#d = toDict(obj)
#print 'toDict: ', d
#pickle.dump(d, open("db1.db", "w"))

data = 'trollolol line 1\nline 2 lol'
print 'data var:\n',data
print
file = open('db1.db','r+')
file.write(data)
file.flush()
print 'file.txt:'
print file.read()