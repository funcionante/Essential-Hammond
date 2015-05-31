#!/usr/bin/python
# encoding=utf-8

import json
import math
from math import sin, pi
from interpreter import generate_pairs

#produces the sequence of samples for each pair with a given registration
def generate_sounds(pairs, registration):
	
	print 'Synthesizer started. Generating sounds.'
	
	#dictio to be converted into json with all the samples of the music. pairs frequency-samples
	sounds = []
	
	#frequencies of the 9 oscillators calculated for each note
	freqs = [None] * 9
	
	#ratio to calculate frequencies (lookup table)
	ratio = [1.0/2, 2.0/3, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0]
	
	#amplitudes calculated for each note by the registration
	amplitudes = [None] * 9
	
	rate = 44100
	
	for pair in pairs:
		mainfreq = pair['freq']
		duration = pair['time']
		
		for i in range(0, 9):
			freqs[i] = int(mainfreq * ratio[i])
			amplitudes[i] = float(registration[i]) / 8 * (32000/9.0)
		
		data = []
		
		nsamples = int(rate * duration)
			
		for i in range(0, nsamples):
			
			sample = 0
			
			for j in range(0, 9):
				sample += int(amplitudes[j] * sin(2.0 * pi * freqs[j] * i / rate))
			data.append(sample)
		
		sounds.append({'freq': mainfreq, 'samples': data})
	
	print 'Interpreter ended.'
	
	return sounds 
		
#just for tests
if __name__ == '__main__':
	
	pauta = 'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6'
	
	pairs = generate_pairs(pauta)
	
	sounds = generate_sounds(pairs, '888888888')
	
	outfile = open('sounds.json', 'w')
	json.dump(sounds, outfile)
	outfile.close()
