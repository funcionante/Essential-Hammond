#encoding:utf8
import cherrypy
import sqlite3 as sql
from som.interpreter import generate_pairs, create_image
from som.synthesizer import generate_sounds
from som.effects_processor import create_wav_file
from database import *
import os.path


###CONFIGS
myport = 8080
myaddress = '127.0.0.1'
current_dir = os.path.dirname(os.path.abspath(__file__))

class Root(object):

	@cherrypy.expose
	def addVote(self, id=None):
		try:
			add_upvotes(id)

		except Exception, e:
			return "Something went wrong"

	'''
	def addVote(self, **kw):
		try:
			x = repr(dict(kw=kw))
			x = x.split("'")
			if (x[3] == "id"):
				add_upvotes(x[5])
			else:
				return "Error"
		except Exception, e:
			return "Something went wrong"'''

	@cherrypy.expose
	def delVote(self, id=None):
		try:
			add_downvotes(id)

		except Exception, e:
			return "Something went wrong"

	'''
	def delVote(self, **kw):
		try:
			x = repr(dict(kw=kw))
			x = x.split("'")
			if (x[3] == "id"):
				add_downvotes(x[5])
			else:
				return "Error"
		except Exception, e:
			return "Something went wrong"'''

	#DONE!
	@cherrypy.expose
	def index(self):
		return open("index.html","r")

	@cherrypy.expose
	def createSong(self, name=None, notes=None):
		try:
			name = name.decode("utf-8")
			notes = notes.decode("utf-8")
			create_song(name, notes)

			create_image(generate_pairs(name+':'+notes),'img/'+str(last_id())+'.jpg')
			return "Musica enviada com sucesso!"

		except Exception, e:
			return "Something went wrong"

	#http://localhost:8080/createSong?name=The%20Simpsons&notes=c.6,e6,f%236,8a6,g.6,e6,c6,8a,8f%23,8f%23,8f%23,2g,8p,8p,8f%23,8f%23,8f%23,8g,a%23.,8c6,8c6,8c6,c6
	#DONE!
	'''
	def createSong(self, **kw):
		try:
			x = repr(dict(kw=kw))
			x = x.split("'")
			if(x[7] == "name" and x[3] == "notes"):
				create_song(x[9], x[5])

				create_image(generate_pairs(x[9]+":"+x[5]),'img/'+str(last_id())+'.jpg')

			return "Música enviada com sucesso!"

		except Exception, e:
			return "Error"'''

	@cherrypy.expose
	def createInterpretation(self, registration = None, id = None, effects = None, name = None):
		try:
			create_interpretation(registration,effects,id,name)
			getno = get_notes_and_name(id)
			pauta = getno[0] + ":" + getno[1]
			filelocation = 'audio/'+str(last_id_interpretations())+'.wav'

			create_wav_file(filelocation, generate_sounds(generate_pairs(pauta), registration), effects)

			return "Interpretação enviada com sucesso!"
		except Exception, e:
			return "Something went wrong"

	#http://localhost:2223/createInterpretation?registration=888888888&id=40&effects=none&name=LOL
	#DONE!
	'''def createInterpretation(self, **kw):
		try:
			x = repr(dict(kw=kw))
			x = x.split("'")
			j = []
			if(x[3] == "registration" and x[7] == "id" and x[11] == "effects" and x[15] == "name"):
				create_interpretation(x[5],x[13],x[9],x[17])
				getno = get_notes_and_name(x[9])
				pauta = getno[0] + ":" + getno[1]
				filelocation = 'audio/'+str(last_id_interpretations())+'.wav'
				regist = x[5]
				effect = x[13]

				create_wav_file(filelocation, generate_sounds(generate_pairs(pauta), regist), effect)
			return "Interpretação enviada com sucesso!"
		except Exception, e:
			return "Error"'''

	@cherrypy.expose
	def getWaveForm(self, id=None):
		try:
			x = "img/"+id+".jpg"

		except Exception, e:
			return "Something went wrong"
		raise cherrypy.HTTPRedirect(x)

	#DONE!
	'''
	def getWaveForm(self, **kw):
		try:
			x = repr(dict(kw=kw))
			x = x.split("'")
			if (x[3] == "id"):
				x = "img/"+x[5]+".jpg"
			else:
				return "Error"
		except Exception, e:
			return "Something went wrong"
		raise cherrypy.HTTPRedirect(x)'''

	@cherrypy.expose
	def getWaveFile(self, id=None):
		try:
			x = "audio/"+id+".wav"

		except Exception, e:
			return "Something went wrong"
		raise cherrypy.HTTPRedirect(x)

	#DONE! FALTA CHECK IF EXIST
	'''
	def getWaveFile(self, **kw):
		try:
			x = repr(dict(kw=kw))
			x = x.split("'")
			if (x[3] == "id"):
				x = "audio/"+x[5]+".wav"
			else:
				return "Error"
		except Exception, e:
			return "Something went wrong"
		raise cherrypy.HTTPRedirect(x)'''

	@cherrypy.expose
	def getNotes(self, id=None):
		try:
			return get_notes(id)

		except Exception, e:
			return "Something went wrong"

	#DONE! FALTA CHECK IF EXIST
	'''
	def getNotes(self, **kw):
		try:
			x = repr(dict(kw=kw))
			x = x.split("'")
			ydourl = ""
			row = ""
			ydoy = x[3]
			if(ydoy == "id"):
				return get_notes(x[5])
			else:
				return "ERROR"
		except Exception, e:
			return "Something went wrong"'''

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def listSongFiles(self, id=None):
		try:
			return get_songs(id)

		except Exception, e:
			return "Something went wrong"

	'''
	@cherrypy.tools.json_out()
	def listSongFiles(self, **kw):
		try:
			x = repr(dict(kw=kw))
			x = x.split("'")
			ydourl = ""
			row = ""
			ydoy = x[3]
			if(ydoy == "id"):
				return get_songs(x[5])
			else:
				return "ERROR"
		except Exception, e:
			return "Something went wrong"'''

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def listNotes(self):
		try:
			return get_all_notes()

		except Exception, e:
			return "Something went wrong"

	#DONE!
	'''
	@cherrypy.tools.json_out()
	def listNotes(self):
		return get_all_notes()'''

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def listSongs(self):
		try:
			return get_all_songs()

		except Exception, e:
			return "Something went wrong"

	#DONE!
	'''
	@cherrypy.tools.json_out()
	def listSongs(self):
		return get_all_songs()'''

	#DONE! JUST FOR TEST
	@cherrypy.expose
	def allmusic(self):
		return open("allmusic.html","r")

	#JUST FOR TEST
	@cherrypy.expose
	def upload(self):
		return open("upload.html")

path   = os.path.abspath(os.path.dirname(__file__))
config = {
  'global' : {
    'server.socket_host' : myaddress,
    'server.socket_port' : myport,
    'server.thread_pool' : 8
  },
  '/static' : {
    'tools.staticdir.on'            : True,
    'tools.staticdir.dir'           : os.path.join(path, './public'),
  },
  '/img' : {
    'tools.staticdir.on'            : True,
    'tools.staticdir.dir'           : os.path.join(path, 'img'),
  },
  '/audio' : {
    'tools.staticdir.on'            : True,
    'tools.staticdir.dir'           : os.path.join(path, 'audio'),
  }
}

cherrypy.quickstart(Root(),'/',config = config)
