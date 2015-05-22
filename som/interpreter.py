import json
import math

freqs = [None] * 100

for i in range(-48, 48):
	freqs[i] = int(220 * math.pow(2,(i/12.0)))
	print freqs[i]
	

#returns a new @value for the @parameter (d, o or b) according to the presets
#in the string @parameters or the same @value if there are no presets 
def updateParameter(parameters, parameter, value):
	
	i = parameters.find(parameter)
	if i != -1:
		value = ''
		i += 2
		while i < len(parameters) and parameters[i].isdigit():
			value = value + parameters[i]
			i += 1
	return value

def interpreter(pauta):
	
	#gets the name of the music
	i = pauta.find(':')
	name = pauta[:i]
	
	#default values
	d = 4
	o = 6
	b = 63
	
	#gets the part that contains the presets of the parameters
	parameters = pauta[pauta.find(':')+1:pauta.rfind(':')]
	
	#defines the 3 parameters according to the presets
	d = updateParameter(parameters, 'd=', 4)
	o = updateParameter(parameters, 'o=', 6)
	b = updateParameter(parameters, 'b=', 63)
	
	print d
	print o
	print b
	
	#gets the part that contains the musical notes
	notes = pauta[pauta.rfind(':')+1:]	
	print notes
	
	data = []
	
	while True:
		
		note = notes[:notes.find(',')]
		
		i = 0
		newd = ''
		fifty = False
		newo = ''
		
		while note[i].isdigit():
			newd = newd + note[i]
			i += 1			
		
		if note.find('c#') != -1:
			tone = 4
			
		elif note.find('c') != -1:
			tone = 3		

		elif note.find('d#') != -1:
			tone = 6
			
		elif note.find('d') != -1:
			tone = 5

		elif note.find('e') != -1:
			tone = 7
		elif note.find('f#') != -1:
			tone = 9
			
		elif note.find('f') != -1:
			tone = 8

		elif note.find('g#') != -1:
			tone = 11

		elif note.find('g') != -1:
			tone = 10

		elif note.find('a#') != -1:
			tone = 1

		elif note.find('a') != -1:
			tone = 0

		elif note.find('b') != -1 or note.find('h') != -1:
			tone = 2

		else:
			tone = 77

			
		print ("tone: %d") % (tone)
		
		if note.find('.') != -1:
			fifty = True
			i = note.find('.') + 1
		
		while i < len(note) and note[i].isdigit():
			newo = newo + note[i]
			i += 1
		
		
		print "note:" + note
			
		if newd == '':
			newd = d
		
		if newo == '':
			newo = o
		
		print "newo:" + newo
		print "newd:" + newd
		
		newd = int(newd)
		newo = int(newo)
		b = int(b)
		
		time = float((float(60)/b) * (1.0/newd))
		
		if fifty:
			time = 1.5 * time
				
		print ('time: %f') % time
		
		if tone != 77:
			freq = freqs[12 * (int(newo) - 4) + tone]
		else:
			freq = 0
			
		print ('freq: %f') % freq
		
		data.append({'time': 4*time, 'freq': freq})
		
		if notes.find(',') != -1:	
			notes = notes[notes.find(',')+1:]
			print i
			print i
			print notes
		else:
			break
	
	return data
	


if __name__ == '__main__':
	
	pauta = 'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6'
	
	print pauta
	
	data = interpreter(pauta)
	
	name = '1.json'
	
	outfile = open(name, 'w')
	json.dump(data, outfile)
	outfile.close()
	
