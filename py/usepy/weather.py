import json, urllib2, time

class weather(object):
	def __init__(self, d):
		self.name = d['name']
		self.temp = {'curr':(d['main']['temp']-273.15)*1.8+32,
			     'min':(d['main']['temp_min']-273.15)*1.8+32,
			     'max':(d['main']['temp_max']-273.15)*1.8+32}
		self.humidity = d['main']['humidity']
		self.pressure = d['main']['pressure']
		self.rain = d['weather']['description']
		self.sun = {'rise':time.strftime('%H:%M:%S',time.localtime(d['sys']['sunrise'])),
			    'set':time.strftime('%H:%M:%S',time.localtime(d['sys']['sunset']))}
	def __repr__(self):
		print self.name + '\n'
		print self.rain + '\n'
		print 'Temp (deg C):', self.temp['curr']
		print '\tMin:', self.temp['min']
		print '\tMax:', self.temp['max'], '\n'
		print 'Sunrise:', self.sun['rise']
		print 'Sunset:', self.sun['set']


def curWeather(loc='Altoona,PA'):
	baseUrl =  'http://api.openweathermap.org/data/2.5/weather?q='
	url = baseUrl+loc.replace(' ','')
	info = urllib2.urlopen(url).read()
	d = json.loads(info)
	return d

if __name__ == '__main__':
	import sys
	weather = curWeather(sys.argv[1])
	sys.stdout.write(weather)
	sys.stdout.flush()