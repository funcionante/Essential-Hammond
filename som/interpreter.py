#!/usr/bin/python
# encoding=utf-8

import json
import math
from PIL import Image

#returns a list of frequencies that can be accessed like this: freqs[12 * int(octave) + tone], with 0 < octave < 7 and 0 < tone < 11 
def get_freqs():
	freqs = [None] * 96

	for i in range(-48, 48):
		freqs[i + 48] = int(261.63 * math.pow(2,(i/12.0)))
	return freqs

#returns a new @value for the @parameter (d, o or b) according to the presets
#in the string @parameters or the same @value if there are no presets 
def update_parameter(parameters, parameter, value):
	
	i = parameters.find(parameter)
	if i != -1:
		value = ''
		i += 2
		while i < len(parameters) and parameters[i].isdigit():
			value = value + parameters[i]
			i += 1
	
	return int(value)

def generate_pairs(pauta):
	
	print 'Interpreter started. Generating pairs frequencies-notes.'
	
	#gets the name of the music
	name = pauta[:pauta.find(':')]
	
	#default values
	d = 4
	o = 6
	b = 63
	
	#gets the part that contains the presets of the parameters
	parameters = pauta[pauta.find(':')+1:pauta.rfind(':')]
	
	#defines the 3 parameters according to the presets
	d = update_parameter(parameters, 'd=', 4)
	o = update_parameter(parameters, 'o=', 6)
	b = update_parameter(parameters, 'b=', 63)
	
	#print ('parameters: %d, %d, %d') % (d, o, b)
	
	#gets the list of frequencies (lookup table)
	freqs = get_freqs()
	
	#gets the part that contains the musical notes
	notes = pauta[pauta.rfind(':')+1:]	
	
	#list that will be returned at the end with pairs freq-time
	pairs = []
	
	#cicle that will go through the notes and will interpret each note
	while True:
		
		#print 'notes: ' + notes
		
		#if it isn't the last note of string notes, it will read until the comma
		if notes.find(',') != -1:
			note = notes[:notes.find(',')]
		#else, it takes the only note in the string
		else:
			note = notes
		
		#print "note: " + note
		
		#initializes the variables
		i = 0 #index of string note
		value = '' #the value of the note
		newo = '' #new o parameter
		tone = 0 #the tone of the note
		fifty = False # if there is a dot increasing the duration of the note by 50%
		
		#if there is a blank space in the beginning of the string
		if note[0] == ' ':
			i += 1
			
		#if there is a new set to the value of the note
		while note[i].isdigit():
			value = value + note[i]
			i += 1			
		
		#gets the tone of the note
		if note.find('c#') != -1:
			tone = 1
			i = note.find('c#') + 2
			
		elif note.find('c') != -1:
			tone = 0
			i = note.find('c') + 1	

		elif note.find('d#') != -1:
			tone = 3
			i = note.find('d#') + 2
			
		elif note.find('d') != -1:
			tone = 2
			i = note.find('d') + 1

		elif note.find('e') != -1:
			tone = 4
			i = note.find('e') + 1
		
		elif note.find('f#') != -1:
			tone = 6
			i = note.find('f#') + 2
			
		elif note.find('f') != -1:
			tone = 5
			i = note.find('f') + 1

		elif note.find('g#') != -1:
			tone = 8
			i = note.find('g#') + 2

		elif note.find('g') != -1:
			tone = 7
			i = note.find('g') + 1

		elif note.find('a#') != -1:
			tone = 10
			i = note.find('a#') + 2

		elif note.find('a') != -1:
			tone = 9
			i = note.find('a') + 1

		elif note.find('b') != -1:
			tone = 11
			i = note.find('b') + 1
		
		elif note.find('h') != -1:
			tone = 11
			i = note.find('h') + 1

		elif note.find('p') != -1:
			tone = 77
			i = note.find('p') + 1

		#print ("tone: %d") % (tone)
		
		# if there is a dot increasing the duration of the note by 50%
		if note.find('.') != -1:
			fifty = True
			i = note.find('.') + 1
		
		#if there is a new set to the parameter o
		while i < len(note) and note[i].isdigit():
			newo = newo + note[i]
			i += 1
		
		#if the new value of the note was not defined, it will be applied d	
		if value == '':
			value = d
		
		#if the new o was not defined, it will be applied the default one	
		if newo == '':
			newo = o
		
		value = int(value)
		newo = int(newo)
		
		#print "newo: %d" % (newo)
		#print "value: %d" % (value)
		
		#print b
		#print d
		
		#calculates the time
		time = float((float(60)/b) * (float(d)/value))
		
		if fifty:
			time *= 1.5
				
		#print ('time: %f') % time
		
		#calculates the frequency
		if tone != 77:
			freq = freqs[12 * int(newo) + tone]
		else:
			freq = 0
			
		#print ('freq: %f') % freq
		
		#adds the pair
		pairs.append({'time': time, 'freq': freq})
		
		if notes.find(',') != -1:	
			notes = notes[notes.find(',')+1:]
		else:
			break
	
	print 'Interpreter ended.'
	
	return pairs
	
#creates an image with a view of the notes contained in the pairs freq-time given
def create_image(pairs, name):
	
	print 'Creating image named ' + name + '.'
	
	#because frequencies are not linear, we will need the lookup table
	#to do the opposite: getting the index by a frequency we have.
	#so, the graphic will represent the notes linearly
	freqs = get_freqs()
	
	#height is 500 by deafault. 
	height = 500
	
	#width will be defined bt the total duration of the music. Each second is 100 pixels.
	width = 0
	for pair in pairs:
		width += int(100 * pair['time'])
	
	#new image in black and white mode, and colored in white by default
	im = Image.new('1', (width, height), 1)
	
	#these are the variables used to define the limites where the lines (that represents the notes) will be written (pixels in black)
	startx = 0
	starty = 0
	endx = 0
	endy = 0
	
	for pair in pairs:
		endx += int(100 * pair['time'])
		
		freq = pair['freq']
		
		if freq != 0:
			i = freqs.index(freq)
			
			starty = height - (495*i/95) - 5
			endy = starty + 5
		
			for x in range(startx, endx):
				for y in range(starty, endy):
					pixel = 0 #black pixel to color de line
					im.putpixel( (x,y), pixel)
		
		startx = endx
		
	im.save(name)
	
	print 'Image created.'
	
	

if __name__ == '__main__':
	
	pauta = 'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6'
	
	pairs = generate_pairs(pauta)
	
	create_image(pairs, 'testimg.jpg')
	
	outfile = open('musica.json', 'w')
	json.dump(pairs, outfile)
	outfile.close()
