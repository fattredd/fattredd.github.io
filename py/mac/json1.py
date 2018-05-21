from json import *

data = [ {'a':'A', 'b':(2,4), 'c':3.0 } ]
print 'DATA: ', repr(data)

data_string = dumps(data)
print 'JSON encoded: ', data_string
decoded = loads(data_string)
print 'decoded: ', decoded

print '1: ', type(data[0]['b'])
print '2: ', type(data_string[0])
print '3: ', type(decoded[0]['b'])