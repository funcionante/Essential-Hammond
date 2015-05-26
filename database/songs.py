#encoding:utf8
import sqlite3 as sql
import sys
import os.path

def create_song(name, notes):
	command = 'INSERT INTO musics(name, notes) VALUES("' + name + '", "' + notes + '")'
	db.execute(command)
	db.commit()

def get_musics():
	command = 'SELECT * FROM musics'
	db.execute(command)


def create_interpretation(registration, effects):
	
	command = 'INSERT INTO interpretations(registration, effects) VALUES("' + registration + '", "' + effects + '")'
	db.execute(command)
	db.commit();

def get_interpretations():
	
	command = 'SELECT * FROM interpretations'
	db.execute(command)
	
def list_songs(music):
	
	print ' ID / NAME / NOTES '
	for row in musics:
		print "%s / %s / %s".format(row[0], row[1], row[2]) 
	
	
'''def listSongs(interpretations):
	
	print 'ID / ID_MUSIC / REGISTRATIONS / EFFECTS / UPVOTES / DOWNVOTES'
	for row in interpretations:
		print "%s / %s / %s / %s / %s / %s ".format(row[0], row[1], row[2], row[3], row[4], row[5])'''
		
#def listSongFiles():

	#Devolve a lista de ficheiros de uma música. Estes ficheiros podem ser imagens apresentando uma visão gráfica das notas da música e ficheiros WAV com a música

def get_notes(ID):
	
	command = 'SELECT * FROM musics WHERE id =' + ID
	result = db.execute(command)
	return result.fetchall()

#def get_waveFile():
	
	#Devolve um ficheiro WAV contendo a interpretação da música.
	
#def get_waveForm():

	#Devolve uma imagem contendo uma representação gráfica das notas

def get_interpretations_by_music_id(ID):
	command = 'SELECT FROM interpretations, musics WHERE '
	
	
def edit_musics(ID, name, notes):
	if name != '':
		command = 'UPDATE musics SET name = "' + name + '" WHERE id = ' + ID
		db.execute(command)
	
	if notes != '':
		command = 'UPDATE musics SET notes = "' + notes + '" WHERE id = ' + Id
		db.execute(command)
		
def edit_interpretations(ID, registration, effects):
	if  registration != '':
		command = 'UPDATE interpretations SET registration = "' + registration + '" WHERE id = ' + ID
		db.execute(command)
	
	if  effects != '':
		command = 'UPDATE interpretations SET effects = "' + effects + '" WHERE id = ' + ID
		db.execute(command)


def more_upvotes(ID, upvotes):
	command = 'UPDATE interpretations SET upvotes = "' + upvotes + 1 +  '" WHERE id = ' + ID
	db.execute(command)
	db.commit()
	
def more_downvotes(ID, downvotes):
	command = 'UPDATE interpretations SET downvotes = "' + downvotes + 1 +  '" WHERE id = ' + ID
	db.execute(command)
	db.commit()
	
#creates a new library database if there is no one. needs create.txt file to work properly.
if not os.path.isfile('songs.db'):
	
	if not os.path.isfile('create.txt'):
		print 'We need a database to run the program. We don\'t have one, so we need a "create.txt" file to create the library. Copy a valid "create.txt" file to this folder and reopen the program.'
		exit(1)
		
	db = sql.connect('songs.db')
	
	createDBfile = open('create.txt', 'r')
	
	for line in createDBfile:
		db.execute(line)	
	
	db.commit()
	createDBfile.close()
	db.close()

db = sql.connect('songs.db')
