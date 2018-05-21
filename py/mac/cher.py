import cherrypy
cherrypy.config.update({'server.socket_port': 80})

class web(object):
	def index(self):
		return 'Success!'
	def re(self, input='None'):
		return input
	def text_html(self,input=None):
		return '404 Error!\n<br>\n'+str(input)
	index.exposed = True
	re.exposed = True

cherrypy.quickstart(web())