import os, os.path
import random
import string

import cherrypy

class HTML(object):
	@cherrypy.expose
	def index(self):
		cherrypy.response.headers["Content-Type"] = "text/html"
		return open("index.html","r").read()

	@cherrypy.expose
	def generate(self, length=8):
	    some_string = ''.join(random.sample(string.hexdigits, int(length)))
	    cherrypy.session['mystring'] = some_string
	    return some_string

if __name__ == '__main__':
 conf = {
     '/': {
         'tools.sessions.on': True,
         'tools.staticdir.root': os.path.abspath(os.getcwd())
     },
     '/static': {
         'tools.staticdir.on': True,
         'tools.staticdir.dir': './public'
     }
 }
cherrypy.tree.mount(HTML(), '/', conf)
cherrypy.engine.start()
cherrypy.engine.block()