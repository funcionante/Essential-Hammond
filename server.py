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
	
	
	#Verify if device is Mobile or Desktop/Laptop.
	#Compare header to existing patterns, case some of header is equal to pattern.
	@cherrypy.expose
	def novamusica(self):
		if(is_mobile(cherrypy.request)):
			return open("index.html","r")
		else:
			return open("desk/novamusica.html","r")
	
	#Verify if device is Mobile or Desktop/Laptop.
	#Compare header to existing patterns, case some of header is equal to pattern.
	@cherrypy.expose
	def novainterpretacao(self):
		if(is_mobile(cherrypy.request)):
			return open("index.html","r")
		else:
			return open("desk/interpretacao.html","r")
	
	#Verify if device is Mobile or Desktop/Laptop.
	#Compare header to existing patterns, case some of header is equal to pattern.
	@cherrypy.expose
	def tocarmusica(self):
		if(is_mobile(cherrypy.request)):
			return open("index.html","r")
		else:
			return open("desk/tocarmusica.html","r")

	#Receives name and notes as URL parameters, verify if correct. Send to database.
	#Create imagem (image name = id of notes)
	#If creating of image gives any error. Data will not be sent to database.
	#Returns Sucess or Error.
	#Exemple: http://localhost:2223/createInterpretation?registration=888888888&id=40&effects=none&name=LOL
	@cherrypy.expose
	def createSong(self, name=None, notes=None):
		try:
			if(len(name) == 0 or notes == "undefined:undefined"):
				raise Exception

			name = name.decode("utf-8") #decodes url to string
			notes = notes.decode("utf-8") #decodes url to string

			create_image(generate_pairs(name+':'+notes),'img/'+str(last_id())+'.jpg') #create image
			create_song(name, notes) #sents data to database
			return "Sucess"
		except Exception, e:
			return "Something went wrong"

	#Ex: http://localhost:2223/createInterpretation?registration=888888888&id=40&effects=none&name=LOL
	@cherrypy.expose
	def createInterpretation(self, registration = None, id = None, effects = None, name = None):
		try:
			if(not registration.isdigit() or len(registration) != 9 or len(name) == 0 or len(effects) == 0 or len(id) == 0 or not id.isdigit()):
				raise Exception

			getno = get_notes_and_name(id) #gets notes and name
			pauta = getno[0] + ":" + getno[1] # join name and notes
			filelocation = 'audio/'+str(last_id_interpretations())+'.wav'

			create_wav_file(filelocation, generate_sounds(generate_pairs(pauta), registration), effects) #creates .wav file with name as id of interpretation
			create_interpretation(registration,effects,id,name) #sents data do database

			return "Sucess"
		except Exception, e:
			return "Something went wrong"

	#(http://localhost:8080/getWaveForm?id=1) == (http://localhost:8080/img/1.jpg)
	@cherrypy.expose
	def getWaveForm(self, id=None):
		try:
			x = "img/"+id+".jpg"

		except Exception, e:
			return "Something went wrong"
		raise cherrypy.HTTPRedirect(x) #redirects to img file

	#(http://localhost:8080/getWaveFile?id=1) == (http://localhost:8080/audio/1.wav)
	@cherrypy.expose
	def getWaveFile(self, id=None):
		try:
			x = "audio/"+id+".wav"

		except Exception, e:
			return "Something went wrong"
		raise cherrypy.HTTPRedirect(x) #redirects to wave file 

	#http://localhost:8080/getNotes?id=1
	@cherrypy.expose
	def getNotes(self, id=None):
		try:
			return get_notes(id) #returns notes

		except Exception, e:
			return "Something went wrong"

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def listSongFiles(self, id=None):
		try:
			return get_songs(id) #returns all interpretations associated to that id (notes)

		except Exception, e:
			return "Something went wrong"

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def listNotes(self):
		try:
			return get_all_notes() #returns table musics (name, notes and id) in json format

		except Exception, e:
			return "Something went wrong"

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def listSongs(self):
		try:
			return get_all_songs() #returns table interpretation (name, id_music, downvotes, upvotes, registration, effects and id) in json format

		except Exception, e:
			return "Something went wrong"

path   = os.path.abspath(os.path.dirname(__file__))
config = {
  'global' : {
    'server.socket_host' : myaddress,
    'server.socket_port' : myport,
    'server.thread_pool' : 8
  },
  '/static' : {
    'tools.staticdir.on'            : True,
    'tools.staticdir.dir'           : os.path.join(path, 'public'),
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