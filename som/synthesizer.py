import json
import math
from math import sin, pi

def normalizer

def synthesizer(pairs, registration):

	#dictio to be converted into json with all the samples of the music. pairs frequence-samples
	sounds = []
	
	#frequences of the 9 oscillators calculated for each note
	freqs = [None] * 9
	
	#ratio to calculate frequences (lookup table)
	ratio = [1.0/2, 2.0/3, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0]
	
	#amplitudes calculated for each note by the registration
	amplitudes = [None] * 9
	
	rate = 44100
	
	for pair in pairs:
		mainfreq = pair['freq']
		duration = pair['time']
		
		for i in range(0, 9):
			freqs[i] = mainfreq * ratio[i]
			amplitudes[i] = float(registration[i]) / 8 * 2000
		
		data = []
		
		
		nsamples = int(rate * duration)
			
		for i in range(0, nsamples):
			
			sample = 0
			
			for j in range(0, 9):
				sample += int(amplitudes[j] * sin(2 * math.pi * freqs[j] * i / rate))
			data.append(sample)

		print len(data)
		
		sounds2 = {}
		
		sounds.append({'freq': mainfreq, 'samples': data})
		
		print sounds
		
	return sounds 
		
	

if __name__ == '__main__':
	
	infile = open('1pauta.json', 'r')
	content = infile.read()

	#json from interpreter with the info of notes and duration. pairs frequence-time
	pairs = json.loads(content)
	
	sounds = synthesizer(pairs, "888888888")
	
	outfile = open('1inter.json', 'w')
	json.dump(sounds, outfile)
	outfile.close()
