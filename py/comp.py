# Computer comparison, bitch
import os, sys
import pickle

class cpu(object):
	def __init__(self, name, **kwargs):
		self.name = name
		self.price = float(kwargs.get('price',0.00)) #in USD
		self.url = kwargs.get('url','NA') #URL of product
		self.clockSpeed = float(kwargs.get('clockSpeed',0.0)) #GHz
		self.cores = kwargs.get('cores',2)
	def __repr__(self):
		out = 'CPU: '+str(name)+'\n\t'
		out += '$'+str(self.price)+'\n\t'
		out += str(self.clockSpeed)+' GHz\n\t'
		out += str(self.cores)+' cores'
		return out

class gpu(object):
	def __init__(self, name, **kwargs):
		self.name = name
		self.price = kwargs.get('price',0) #in USD
		self.url = kwargs.get('url','NA') #URL of product
		self.brand = kwargs.get('brand','') #NVIDIA
		self.line = kwargs.get('line','') #GeForce
		self.clock = kwargs.get('clock',0) #MHz
		self.memoryclock = kwargs.get('memoryclock',0) #MHz
		self.cores = kwargs.get('cores',1)
		self.memorytype = kwargs.get('memorytype','GDDR5')
	def __repr__(self):
		out = 'GPU: '+str(name)+'\n\t'
		out += '$'+str(self.price)+'\n\t'
		out += str(self.clock)+' MHz Clock Freq\n\t'
		out += str(self.memoryclock)+' MHz '
		out += self.memorytype+' Ram'
		if self.hdmi:
			out += '\n\tHas HDMI support'
		else:
			out += '\n\tNo HDMI support'
		return out

class ram(object):
	def __init__(self, name, **kwargs):
		self.name = name
		self.price = kwargs.get('price',0) #in USD
		self.url = kwargs.get('url','NA') #URL of product
		self.size = kwargs.get('size',0) #GB
		self.type = kwargs.get('type','DDR3')
	def __repr__(self):
		out = 'RAM: '+str(name)+'\n\t'
		out += '$'+str(self.price)+'\n\t'
		out += str(self.size)+'GB '
		out += str(self.type)
		return out

class monitor(object):
	def __init__(self, name, **kwargs):
		self.name = name
		self.price = kwargs.get('price',0) #in USD
		self.url = kwargs.get('url','NA') #URL of product
		self.size = kwargs.get('size',15) #inches
		self.width = kwargs.get('width',1920) #px
		self.height = kwargs.get('height',1080) #px
		self.matte = kwargs.get('matte',False) #matte screen?
	def __repr__(self):
		out = 'Monitor: '+str(name)+'\n\t'
		out += '$'+str(self.price)+'\n\t'
		out += str(self.size)+'"\n\t'
		out += str(self.width)+'x'+str(self.height)
		return out

class hdd(object):
	def __init__(self, name, **kwargs):
		self.name = name
		self.price = kwargs.get('price',0) #in USD
		self.url = kwargs.get('url','NA') #URL of product
		self.size = kwargs.get('size',500) #GB
		self.ssd = kwargs.get('ssd',False)
	def __repr__(self):
		out = 'HDD: '+str(name)+'\n\t'
		out += '$'+str(self.price)+'\n\t'
		out += str(self.size)+'GB'
		if self.ssd:
			out += ' SSD'
		return out

class compy(object):
	def __init__(self, name, **kwargs):
		self.name = name
		self.cpu = kwargs.get('cpu',cpu('Generic'))
		self.gpu = kwargs.get('gpu',gpu('Generic'))
		self.monitor = kwargs.get('monitor',monitor('Generic'))
		hddsize = kwargs.get('hddsize',500)
		self.hdd = kwargs.get('hdd',hdd('Generic',size=hddsize))
		ramsize = kwargs.get('ramsize',2)
		self.ram = kwargs.get('ram',ram('Generic',size=ramsize))
		self.os = kwargs.get('os','Unknown')
		self.usb = kwargs.get('usb',3) #amount of ports
		self.webcam = kwargs.get('webcam',True)
		self.price = kwargs.get('price',0)
	def __repr__(self):
		out = 'Computer: '+str(name)+'\n\t'
		out += '$'+str(self.price)+'\n'
		out += self.cpu.__repr__()+'\n'
		out += self.gpu.__repr__()+'\n'
		out += self.ram.__repr__()+'\n'
		out += self.hdd.__repr__()+'\n'
		out += self.monitor.__repr__()+'\n'
		out += 'Misc:\n\t'+str(self.usb)+' USB ports'
		out += '\n\tOS: '+self.os
		if self.webcam:
			out += '\n\tHas a webcam'
		return out
	def partPrices(self):
		out = self.cpu.price
		out += self.gpu.price
		out += self.monitor.price
		out += self.hdd.price
		out += self.ram.price
		return out

def pInfo(l,fname='comp.p'):
	'''Pickle a list of computer classes'''
	pinfo = pickle.dumps(l)
	f = open(fname,'w+')
	f.write(pinfo)
	f.close()

def pLoad(fname='comp.p'):
	'''Load a list of computer classes'''
	f = open(fname,'r')
	pinfo = f.read()
	info = pickle.loads(pinfo)
	return info

