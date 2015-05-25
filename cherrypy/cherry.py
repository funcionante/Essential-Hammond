#encoding:utf8
import cherrypy
import sqlite3 as sql

class Root(object):

	#DONE!
	@cherrypy.expose
	def index(self):
		return open("index.html","r")

	#http://localhost:8080/createSong?name=The%20Simpsons&notes=c.6,e6,f%236,8a6,g.6,e6,c6,8a,8f%23,8f%23,8f%23,2g,8p,8p,8f%23,8f%23,8f%23,8g,a%23.,8c6,8c6,8c6,c6
	
	#DONE!
	@cherrypy.expose
	def createSong(self, **kw):
		x = repr(dict(kw=kw))
		x = x.split("'")
		xdourl = ""
		ydourl = ""
		xdox = x[7]
		ydoy = x[3]
		if(xdox == "name" and ydoy == "notes"):
			xdourl = x[9]
			ydourl = x[5]

			db = sql.connect("database.db")
			db.execute("INSERT INTO song (name,sheet) VALUES (?,?)", (xdourl,ydourl,))
			db.commit()
			result = db.execute("SELECT * FROM song")
			rows = result.fetchall()
			d = []
			for row in rows:
				name = {"id":row[0],"name":row[1],"notes":row[2]}
				d.append(name)
			db.close()

		return "Música enviada com sucesso!"

	#ALMOST DONE!
	@cherrypy.expose
	def getWaveForm(self, **kw):
		x = repr(dict(kw=kw))
		x = x.split("'")
		if (x[3] == "id"):
			x = "http://localhost:2222/img/"+x[5]+".jpg"
		else:
			x = "None"
		return x

	#ALMOST DONE!
	@cherrypy.expose
	def getWaveFile(self, **kw):
		x = repr(dict(kw=kw))
		x = x.split("'")
		if (x[3] == "id"):
			x = "http://localhost:2222/audio/"+x[5]+".wav"
		else:
			x = "None"
		return x

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

cherrypy.config.update({'server.socket_host': '127.0.0.1',
	'server.socket_port': 2222,
	})

cherrypy.quickstart(Root(),'/','config.conf')