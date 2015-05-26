#encoding:utf8
import cherrypy
import sqlite3 as sql
from interpreter import generate_pairs, create_image
from synthesizer import generate_sounds
from effects_processor import create_wav_file
###CONFIGS
myport = 2223
myaddress = '127.0.0.1'

class Root(object):

	#DONE!
	@cherrypy.expose
	def index(self):
		return open("index.html","r")

	#http://localhost:8080/createSong?name=The%20Simpsons&notes=c.6,e6,f%236,8a6,g.6,e6,c6,8a,8f%23,8f%23,8f%23,2g,8p,8p,8f%23,8f%23,8f%23,8g,a%23.,8c6,8c6,8c6,c6
	
	#DONE!
	@cherrypy.expose
	def createSong(self, **kw):
		try:
			x = repr(dict(kw=kw))
			x = x.split("'")
			#y do url = x[5]
			#x do url = x[9]
			if(x[7] == "name" and x[3] == "notes"):
				db = sql.connect("database.db")
				db.execute("INSERT INTO song (name,sheet) VALUES (?,?)", (x[9],x[5],))
				db.commit()
				result = db.execute("SELECT id FROM song")
				rows = result.fetchall()
				d = []
				for row in rows:
					d.append(row[0])
				db.close()

				create_image(generate_pairs(x[9]+":"+x[5]),'img/'+str(d[len(d)-1])+'.jpg')

			return "Música enviada com sucesso!"

		except Exception, e:
			return "Error"

	#http://localhost:2223/createInterpretation?registration=888888888&id=40&effects=none
	#AlMOST DOnE. NEED DB INTERECTION.
	@cherrypy.expose
	def createInterpretation(self, **kw):
		try:
			x = repr(dict(kw=kw))
			x = x.split("'")
			j = []
			if(x[3] == "registration" and x[7] == "id" and x[11] == "effects"):
				db = sql.connect("database.db")
				result = db.execute("SELECT name,sheet FROM song WHERE id=?",(x[9],))
				rows = result.fetchone()
				db.commit()
				db.close()
				pauta = rows[0]+":"+rows[1]
				filelocation = 'audio/'+x[9]+'.wav'
				regist = x[5]
				effect = x[13]

				create_wav_file(filelocation, generate_sounds(generate_pairs(pauta), regist), 44100, effect)
			return '''
	<audio controls>
	  <source src="audio/'''+x[9]+'''.wav" type="audio/ogg">
	Your browser does not support the audio element.
	</audio>'''
		except Exception, e:
			return "Error"

	#DONE!
	@cherrypy.expose
	def getWaveForm(self, **kw):
		x = repr(dict(kw=kw))
		x = x.split("'")
		if (x[3] == "id"):
			x = "img/"+x[5]+".jpg"
		else:
			x = "None"
		raise cherrypy.HTTPRedirect(x) 
		#return x

	#DONE!
	@cherrypy.expose
	def getWaveFile(self, **kw):
		x = repr(dict(kw=kw))
		x = x.split("'")
		if (x[3] == "id"):
			x = "audio/"+x[5]+".wav"
		else:
			x = "None"
		raise cherrypy.HTTPRedirect(x)

	#DONE!
	@cherrypy.expose
	def getNotes(self, **kw):
		x = repr(dict(kw=kw))
		x = x.split("'")
		ydourl = ""
		row = ""
		ydoy = x[3]
		if(ydoy == "id"):
			ydourl = x[5]
			print ydourl
			db = sql.connect("database.db")
			result = db.execute("SELECT sheet FROM song WHERE id=?",(ydourl,))
			rows = result.fetchone()
			row = rows
			db.commit()
			db.close()

		return row

	#DONE!
	@cherrypy.expose
	@cherrypy.tools.json_out()
	def listSongs(self):
		db = sql.connect("database.db")
		result = db.execute("SELECT * FROM song")
		rows = result.fetchall()
		d = []
		for row in rows:
			name = {"id":row[0],"name":row[1],"notes":row[2]}
			d.append(name)

		return d

		'''
		f = open('js/alllist.js','w')
		f.write(unicode("alllist("))
		f.write(unicode(json.dumps(d, ensure_ascii=False)))
		f.write(unicode(")"))
		f.close()
		db.commit()
		db.close()
		return open("allmusic.html","r")'''

	#DONE! JUST FOR TEST
	@cherrypy.expose
	def allmusic(self):
		return open("allmusic.html","r")

	#NOT USEFULL
	def update(self):
		cl = cherrypy.request.headers['Content-Length']
		rawbody = cherrypy.request.body.read(int(cl))
		#body = simplejson.loads(rawbody)
		# do_something_with(body)

		rawbody = rawbody.replace('"', '').split(":",1)
		print rawbody
		db = sql.connect("database.db")
		db.execute("INSERT INTO song (name,sheet) VALUES (?,?)", (rawbody[0],rawbody[1],))
		db.commit()
		db.close()

	#JUST FOR TEST
	@cherrypy.expose
	def upload(self):
		return open("upload.html")

cherrypy.config.update({'server.socket_host': myaddress,
	'server.socket_port': myport,
	})

cherrypy.quickstart(Root(),'/','config.conf')