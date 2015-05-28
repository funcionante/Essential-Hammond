#encoding:utf8
import sqlite3 as sql
import sys
import os.path

def create_song(name, notes):
	command = 'INSERT INTO musics(name, notes) VALUES("' + name + '", "' + notes + '")'
	db.execute(command)
	db.commit()

def get_all_notes():
	command = 'SELECT * FROM musics'
	result = db.execute(command)
	rows = result.fetchall()
	d = []
	for row in rows:
		name = {"id":row[0],"name":row[1],"notes":row[2]}
		d.append(name)

	return d

def get_all_songs():
	command = 'SELECT * FROM interpretations'
	result = db.execute(command)
	rows = result.fetchall()
	d = []
	for row in rows:
		name = {"id":row[0],"id_music":row[1],"name":row[2],"registration":row[3],"effects":row[4],"upvotes":row[5],"downvotes":row[6]}
		d.append(name)

	return d

def last_id():
	result = db.execute("SELECT id FROM musics")
	rows = result.fetchall()
	x = []
	for row in rows:
		x.append(row[0])

	return x[len(x)-1]

def last_id_interpretations():
	result = db.execute("SELECT id FROM interpretations")
	rows = result.fetchall()
	x = []
	for row in rows:
		x.append(row[0])

	return x[len(x)-1]

def create_interpretation(registration, effects,id_music,name):
	
	command = 'INSERT INTO interpretations(id_music,name,registration, effects) VALUES("' + id_music + '","' + name + '","' + registration + '", "' + effects + '")'
	db.execute(command)
	db.commit();

def get_interpretations():
	
	command = 'SELECT * FROM interpretations'
	db.execute(command)
	db.commit();
	
def list_songs(music):
	
	print ' ID / NAME / NOTES '
	for row in musics:
		print "%s / %s / %s".format(row[0], row[1], row[2]) 
	
	
'''def listSongs(interpretations):
	
	print 'ID / ID_MUSIC / REGISTRATIONS / EFFECTS / UPVOTES / DOWNVOTES'
	for row in interpretations:
		print "%s / %s / %s / %s / %s / %s ".format(row[0], row[1], row[2], row[3], row[4], row[5])'''
		
#def listSongFiles():

def get_notes(ID):
	command = 'SELECT notes FROM musics WHERE id =' + ID
	result = db.execute(command)
	return result.fetchone()

def get_notes_and_name(ID):
	command = 'SELECT name,notes FROM musics WHERE id =' + ID
	result = db.execute(command)
	return result.fetchone()

#def get_waveFile():

#def get_waveForm():

'''   def get_interpretations_by_music_id(ID):
	command = 'SELECT FROM interpretations, musics WHERE '  '''
	
	
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

#creates a new library database if there is no one. needs create.txt file to work properly.
if not os.path.isfile('database/songs.db'):
	
	if not os.path.isfile('database/create.txt'):
		print 'We need a database to run the program. We don\'t have one, so we need a "create.txt" file to create the library. Copy a valid "create.txt" file to this folder and reopen the program.'
		exit(1)
		
	db = sql.connect('database/songs.db')
	
	createDBfile = open('database/create.txt', 'r')
	
	for line in createDBfile:
		db.execute(line)	
	
	db.commit()
	createDBfile.close()
	db.close()

db = sql.connect('database/songs.db',check_same_thread=False)