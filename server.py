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
myaddress = '0.0.0.0'
current_dir = os.path.dirname(os.path.abspath(__file__))

class Root(object):

	#This function receives ID that belongs to interpretations table and increment by 1 upvote field.
	#In case of bad ID (wrong or does not exist) will return "Something went wrong".
	@cherrypy.expose
	def addVote(self, id=None):
		try:
			add_upvotes(id)
			return "Vote added"

		except Exception, e:
			return "Something went wrong"

	#This function receives ID that belongs to interpretations table and increment by 1 downvote field.
	#In case of bad ID (wrong or does not exist) will return "Something went wrong".
	@cherrypy.expose
	def delVote(self, id=None):
		try:
			add_downvotes(id)
			return "Vote added"

		except Exception, e:
			return "Something went wrong"

	#Verify if device is Mobile or Desktop/Laptop.
	#Compare header to existing patterns, case some of header is equal to pattern.
	@cherrypy.expose
	def index(self):
		if(is_mobile(cherrypy.request)):
			return open("index.html","r")
		else:
			return open("desk/index.html","r")
	
	
	@cherrypy.expose
	def novamusica(self):
		if(is_mobile(cherrypy.request)):
			return open("index.html","r")
		else:
			return open("desk/novamusica.html","r")
	
	@cherrypy.expose
	def novainterpretacao(self):
		if(is_mobile(cherrypy.request)):
			return open("index.html","r")
		else:
			return open("desk/interpretacao.html","r")
	
	@cherrypy.expose
	def tocarmusica(self):
		if(is_mobile(cherrypy.request)):
			return open("index.html","r")
		else:
			return open("desk/tocarmusica.html","r")

	@cherrypy.expose
	def createSong(self, name=None, notes=None):
		try:
			if(len(name) == 0 or len(notes) == 0 or notes == "undefined:undefined"):
				raise Exception

			name = name.decode("utf-8")
			notes = notes.decode("utf-8")
			create_song(name, notes)

			create_image(generate_pairs(name+':'+notes),'img/'+str(last_id())+'.jpg')
			return "Sucess"
		except Exception, e:
			return "Something went wrong"

	@cherrypy.expose
	def createInterpretation(self, registration = None, id = None, effects = None, name = None):
		try:
			if(not registration.isdigit() or len(registration) != 9):
				raise Exception

			create_interpretation(registration,effects,id,name)
			getno = get_notes_and_name(id)
			pauta = getno[0] + ":" + getno[1]
			filelocation = 'audio/'+str(last_id_interpretations())+'.wav'

			create_wav_file(filelocation, generate_sounds(generate_pairs(pauta), registration), effects)

			return "Sucess"
		except Exception, e:
			return "Something went wrong"

	@cherrypy.expose
	def getWaveForm(self, id=None):
		try:
			x = "img/"+id+".jpg"

		except Exception, e:
			return "Something went wrong"
		raise cherrypy.HTTPRedirect(x)

	@cherrypy.expose
	def getWaveFile(self, id=None):
		try:
			x = "audio/"+id+".wav"

		except Exception, e:
			return "Something went wrong"
		raise cherrypy.HTTPRedirect(x)

	@cherrypy.expose
	def getNotes(self, id=None):
		try:
			return get_notes(id)

		except Exception, e:
			return "Something went wrong"

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def listSongFiles(self, id=None):
		try:
			return get_songs(id)

		except Exception, e:
			return "Something went wrong"

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def listNotes(self):
		try:
			return get_all_notes()

		except Exception, e:
			return "Something went wrong"

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def listSongs(self):
		try:
			return get_all_songs()

		except Exception, e:
			return "Something went wrong"

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
  '/desk' : {
    'tools.staticdir.on'            : True,
    'tools.staticdir.dir'           : os.path.join(path, 'desk'),
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
