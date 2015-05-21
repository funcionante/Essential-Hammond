import json
import math

freqs = [None] * 100

for i in range(-50, 50):
	freqs[i] = 444 * math.pow(2,(i/12))
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
	
	#defines de 3 parameters according to the presets
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
		newd = 0
		fifty = False
		newo = 0
		
		while note[i].isdigit():
			newd = newd + int(note[i])
			i += 1
		
		if note.find('c') != -1:
			tone = 0
			i += 1
		elif note.find('c#') != -1:
			tone = 1
			i += 2
		elif note.find('d') != -1:
			tone = 2
			i += 1
		elif note.find('d#') != -1:
			tone = 3
			i += 2
		elif note.find('e') != -1:
			tone = 4
			i += 1
		elif note.find('f') != -1:
			tone = 5
			i += 1
		elif note.find('f#') != -1:
			tone = 6
			i += 2
		elif note.find('g') != -1:
			tone = 7
			i += 1
		elif note.find('g#') != -1:
			tone = 8
			i += 2
		elif note.find('a') != -1:
			tone = 9
			i += 1
		elif note.find('a#') != -1:
			tone = 10
			i += 2
		elif note.find('b') != -1 or note.find('h') != -1:
			tone = 11
			i += 1
		else:
			tone = 77
			
		print tone
		
		if note.find('.') != -1:
			fifty = True
			i += 1
			print fifty
		
		while i < len(note) and note[i].isdigit():
			newo = newo + int(note[i])
			i += 1
		
		
		if newd == 0:
			newd = d
		
		if newo == 0:
			newo = o
		
		print newd
		time = float((float(60)/float(b)) * (float(1)/float(newd)))
		
		if fifty:
			time = 1.5 * time
				
		print ('time: %f') % time
		
		if tone != 77:
			freq = 12 * (int(newo) - 4) + tone
		else:
			freq = 0
			
		print ('freq: %f') % freq
		
		data.append({'time': time, 'freq': freq})
		
		if notes.find(',') != -1:	
			notes = notes[notes.find(',')+1:]
			print i
			print notes
		else:
			break
	
	name = name + '.json'
	
	outfile = open(name, 'w')
	json.dump(data, outfile)
	outfile.close()

if __name__ == '__main__':
	
	pauta = 'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6'
	
	print pauta
	
	interpreter(pauta)
	
