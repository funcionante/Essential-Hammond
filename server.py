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
	def tocarmusica(self, id=None):
		try:
			if(id == None):
				id = "1"
				vaz = ""
				vax = ""
				z = get_all_notes()
				d = get_songs(id)
			else:
				vaz = ""
				vax = ""
				z = get_all_notes()
				d = get_songs(id)

			for y in z:
				if(str(id) == str(y["id"])):
					vaz = vaz + '''<a href="tocarmusica?id='''+str(y["id"])+'''" class="list-group-item active">'''+y["name"].encode("utf-8")+'''</a>'''
				else:
					vaz = vaz + '''<a href="tocarmusica?id='''+str(y["id"])+'''" class="list-group-item">'''+y["name"].encode("utf-8")+'''</a>'''

			getno = get_notes_and_name(id) #gets notes and name
			pauta = (getno[0] + ":" + getno[1]).encode("utf-8") # join name and notes
			for x in d:
				
				up = x['upvotes']
				down = x['downvotes']
				
				if up == 0 and down == 0:
					up100 = 50
					down100 = 50
				else:
					up100 = up*100/(up+down)
					down100 = 100-up100
					
				vax = vax + '''
				<div class="col-sm-6 col-md-4">
	                <div class="thumbnail">
		                  <div class="caption">
		                    <h3>'''+x['name'].encode("utf-8")+'''</h3>
		                    <div class="progress">
							  <div id="voted'''+str(x['id'])+'''" class="progress-bar progress-bar" style="width: 0%">
								Voto enviado.
		                      </div>
		                      <div class="progress-bar progress-bar-success" style="width: '''+str(up100)+'''%">
								'''+str(up)+'''
		                      </div>
		                      <div class="progress-bar progress-bar-danger" style="width: '''+str(down100)+'''%">
								'''+str(down)+'''
		                      </div>
		                    </div>
		                    <span><b>Registo:</b> <span>'''+str(x['registration'])+'''</span></span>
		                    <button type="button" class="btn btn-default btn-sm pull-right" onclick="delVote('''+str(x['id'])+''')">
		                      <span class="glyphicon glyphicon-thumbs-down" aria-hidden="true"></span>
							</button>
		                    <button type="button" class="btn btn-default btn-sm pull-right" onclick="addVote('''+str(x['id'])+''')">
		                      <span class="glyphicon glyphicon-thumbs-up" aria-hidden="true"></span>
		                    </button>
	                    <p><b>Efeito:</b> <span>'''+x['effects'].encode("utf-8")+'''</span></p>

	                    <audio class="player" controls>
	                      <source src="audio/'''+str(x['id'])+'''.wav" type="audio/wav">
	                        Não foi possível reproduzir a música.
	                      </audio>
	                    </div>
	                  </div>
	                </div>'''

			return '''

<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Tocar Música</title>

  <!-- Bootstrap Core CSS -->
  <link href="desk/css/bootstrap.min.css" rel="stylesheet">

  <!-- Custom CSS -->
  <link href="desk/css/shop-item.css" rel="stylesheet">
  <link href="desk/css/style.css" rel="stylesheet">


</head>

<body>

  <!-- Navigation -->
  <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
    <div class="container">
      <!-- Brand and toggle get grouped for better mobile display -->
      <div class="navbar-header">
        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="/">Proj2App</a>
      </div>
      <!-- Collect the nav links, forms, and other content for toggling -->
      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
        <ul class="nav navbar-nav">
          <li>
            <a href="novamusica">Nova Música</a>
          </li>
          <li>
            <a href="novainterpretacao">Nova Interpretação</a>
          </li>
          <li class="active">
            <a href="tocarmusica">Tocar Música</a>
          </li>
        </ul>
      </div>
      <!-- /.navbar-collapse -->
    </div>
    <!-- /.container -->
  </nav>

  <!-- Page Content -->
  <div class="container">

    <div class="row">

      <div class="col-md-3">
        <p class="lead">Lista de Músicas</p>
        <div class="list-group">
        	'''+vaz+'''
          <!--<a href="#" class="list-group-item">Música 1</a>
          <a href="#" class="list-group-item active">Música 2</a>
          <a href="#" class="list-group-item">Música 3</a>-->
        </div>
      </div>

      <div class="col-md-9">

        <div class="thumbnail">
        <img class="img-responsive" src="img/'''+str(id)+'''.jpg" alt="">
          <div class="caption-full">
            <h4><a href="#">'''+getno[0].encode("utf-8")+'''</a>
            </h4>
            <p>'''+pauta+'''</p>
          </div>
        </div>

        <div class="row">
                '''+vax+'''
        </div>
            </div>

          </div>

        </div>
        <!-- /.container -->

        <div class="container">

          <hr>

          <!-- Footer -->
          <footer>
            <div class="row">
              <div class="col-lg-12">
                <p>Copyright &copy; 2015. Todos os direitos reservados. Desenvolvido em <a href="http://getbootstrap.com/" target="_blank">Bootstrap</a>. Template original: <a href="https://github.com/IronSummitMedia/startbootstrap-shop-item" target="_blank">Shop Item</a>.</p>
              </div>
            </div>
          </footer>

        </div>
        <!-- /.container -->

        <!-- jQuery -->
        <script src="desk/js/jquery.js"></script>

        <!-- Bootstrap Core JavaScript -->
        <script src="desk/js/bootstrap.min.js"></script>

        <!-- Scripts -->
        <script src="desk/js/scripts.js"></script>

      </body>

      </html>
'''
		except Exception, e:
			return "Não existem músicas"

	#Forces mobile version, in case trying to see website in desktop
	@cherrypy.expose
	def mobile(self):
		return open("index.html","r")

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
	'''def tocarmusica(self):
		if(is_mobile(cherrypy.request)):
			return open("index.html","r")
		else:
			return open("desk/tocarmusica.html","r")'''

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
