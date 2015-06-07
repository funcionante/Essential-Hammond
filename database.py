#encoding:utf8
import sqlite3 as sql
import sys
import os.path
import re

# checks if device is mobile or desktop
def is_mobile(request):
    ismobile = False

    if request.headers.has_key('User-Agent'):
        user_agent = request.headers['User-Agent']

        # Test common mobile values.
        patterns = "(xoom|up.browser|up.link|mmp|symbian|smartphone|phone|tablet|midp|wap|windows ce|pda|mobile|mini|palm|netfront|nokia)"

        patt_compiled = re.compile(patterns, re.IGNORECASE)
        match = patt_compiled.search(user_agent)

        if match:
           ismobile = True

    return ismobile 

# creates a new line in musics table
def create_song(name, notes):
	command = 'INSERT INTO musics(name, notes) VALUES("' + name + '", "' + notes + '")'
	db.execute(command)
	db.commit()
	
#shows the all content from musics table	
def get_all_notes():
	command = 'SELECT * FROM musics'
	result = db.execute(command)
	rows = result.fetchall()
	d = []
	for row in rows:
		name = {"id":row[0],"name":row[1],"notes":row[2]}
		d.append(name)

	return d
	
#shows the all content from interpretations table	
def get_all_songs():
	command = 'SELECT * FROM interpretations'
	result = db.execute(command)
	rows = result.fetchall()
	d = []
	for row in rows:
		name = {"id":row[0],"id_music":row[1],"name":row[2],"registration":row[3],"effects":row[4],"upvotes":row[5],"downvotes":row[6]}
		d.append(name)

	return d

# shows all id's from musics table, raising IndexError exception when a sequence subscript is out of range
def last_id():
	try:
		result = db.execute("SELECT id FROM musics")
		rows = result.fetchall()
		x = []
		for row in rows:
			x.append(row[0])
		return x[len(x)-1]+1
	except IndexError, e:
		return 1

# shows all id's from interpretations table, raising IndexError exception when a sequence subscript is out of range 
def last_id_interpretations():
	try:
		result = db.execute("SELECT id FROM interpretations")
		rows = result.fetchall()
		x = []
		for row in rows:
			x.append(row[0])

		return x[len(x)-1]+1
	except IndexError, e:
		return 1

# creates a new line in interpretations table 
def create_interpretation(registration, effects,id_music,name):
	
	command = 'INSERT INTO interpretations(id_music,name,registration, effects) VALUES("' + id_music + '","' + name + '","' + registration + '", "' + effects + '")'
	db.execute(command)
	db.commit()

# shows the all content from interpretations table
def get_interpretations():
	
	command = 'SELECT * FROM interpretations'
	db.execute(command)

# shows the content from musics table
def list_songs(music):
	
	print ' ID / NAME / NOTES '
	for row in musics:
		print "%s / %s / %s".format(row[0], row[1], row[2]) 

# shows the notes from a song according to corresponding id, in musics table
def get_notes(ID):
	command = 'SELECT notes FROM musics WHERE id =' + ID
	result = db.execute(command)
	return result.fetchone()

# shows the name and notes from a song according to corresponding id, , in musics table
def get_notes_and_name(ID):
	command = 'SELECT name,notes FROM musics WHERE id =' + ID
	result = db.execute(command)
	return result.fetchone()
	
# update the name or notes from musics table according to corresponding id. checks if there is not empty spaces in order to update	
def edit_musics(ID, name, notes):
	if name != '':
		command = 'UPDATE musics SET name = "' + name + '" WHERE id = ' + ID
		db.execute(command)
	
	if notes != '':
		command = 'UPDATE musics SET notes = "' + notes + '" WHERE id = ' + Id
		db.execute(command)

# update the registration or effects from interpretations table according to corresponding id. checks if there is not empty spaces in order to update	
def edit_interpretations(ID, registration, effects):
	if  registration != '':
		command = 'UPDATE interpretations SET registration = "' + registration + '" WHERE id = ' + ID
		db.execute(command)
	
	if  effects != '':
		command = 'UPDATE interpretations SET effects = "' + effects + '" WHERE id = ' + ID
		db.execute(command)
		
# shows a specifif line from interpretations table according to corresponding id	
def get_songs(ID):
	command = 'SELECT * FROM interpretations WHERE id_music = ' + ID
	result = db.execute(command)
	rows = result.fetchall()
	d = []
	for row in rows:
		name = {"id":row[0],"id_music":row[1],"name":row[2],"registration":row[3],"effects":row[4],"upvotes":row[5],"downvotes":row[6]}
		d.append(name)

	return d
	
#increases in one unity the posivite likes in interpretations table	
def add_upvotes(ID):
	command = 'SELECT upvotes FROM interpretations WHERE id = ' + str(ID)
	result = db.execute(command)
	result = result.fetchone()
	result = result[0] + 1
	command = 'UPDATE interpretations SET upvotes = "' + str(result) + '" WHERE id = ' + str(ID)
	db.execute(command)
	db.commit()
	

#increases in one unity the negative likes in interpretations table	
def add_downvotes(ID):
	command = 'SELECT downvotes FROM interpretations WHERE id = ' + str(ID)
	result = db.execute(command)
	result = result.fetchone()
	result = result[0] + 1
	command = 'UPDATE interpretations SET downvotes = "' + str(result) + '" WHERE id = ' + str(ID)
	db.execute(command)
	db.commit()



#cria uma nova songs database if no one is available. needs create.txt file to work properly.
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

db = sql.connect('songs.db',check_same_thread=False)
