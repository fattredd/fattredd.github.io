import json

class food(object):
	def __init__(self, name, price=0.00,amount=0):
		self.name = name
		self.price = price
		self.amount = amount

obj = food('ham',2.50,3)

def toDict(obj):
	d = { '__class__':obj.__class__.__name__,
		'__module__':obj.__module__,
		}
	d.update(obj.__dict__)
	return d
def toObj(d):
	class_name = d.pop('__class__')
	module_name = d.pop('__module__')
	module = __import__(module_name)
	class_ = getattr(module, class_name)
	args = dict((key.encode('ascii'), value) for key, value in d.items())
	inst = class_(**args)
	return inst
def printObj(obj):
	for prop, value in vars(obj).iteritems():
		print prop,': ', value

print
enc = json.dumps(obj, default=toDict)
print enc
print '==>'
unc = json.loads(enc, object_hook=toObj)
printObj(unc)
