#!/usr/bin/python
# encoding=utf-8

import wave
import json
from struct import pack
import math
from math import sin, pi
from interpreter import generate_pairs
from synthesizer import generate_sounds

rate = 44100

#returns the positive part of a value
def module(value):
	if value < 0:
		return -value
	return value

#return the same list of samples with the samples normalized to a default value
def normalize(data, value = 32767):
	
	maximum = 0
	
	for i in range(0, len(data)):
		if module(data[i]) > maximum:
			maximum = module(data[i])
	
	#print maximum
	
	if maximum != 0:
		for i in range(0, len(data)):
			data[i] = int(float(data[i]) * value / maximum)
	
	return data

#applis null effect and returns the samples
def effect_none(data, sounds):
    
	for sound in sounds:
		data += sound['samples']
		
	return data

#applies echo effect and returns the samples
def effect_echo(data, sounds):
	
	data = effect_none(data, sounds)
	
	#increases the duration by 0.5 seconds, so the echo in the end of the music is not cut
	for i in range(0, rate/2):
		data.append(0)
	
	#double echo (0.1 and 0.2 of delay)
	for i in range (0, len(data)):
		if i > rate/10:
			data[i] += 0.5 * data[i-rate/10]
		
		if i > rate/5:
			data[i] += 0.2 * data[i-rate/5]

	return data

def effect_tremolo(data, sounds):
	
	data = effect_none(data, sounds)
	
	for i in range (0, len(data)):
		data[i] += 0.3 * sin(2.0 * pi * 20 * i / rate) * data[i];

	return data
	
def effect_distortion(data, sounds):
	
	data = effect_none(data, sounds)
	
	for i in range (0, len(data)):
		data[i] += pow(data[i], 2)

	return data
	
def effect_chorus(data, sounds):
	
	for sound in sounds:
		
		subdata = sound['samples']
		subdata = normalize(subdata)
		
		freq = sound['freq'] + 50
		
		for i in range(0, len(subdata)):
		#for sample in data:
			subdata[i] += int(32000 * sin(2.0 * pi * freq * i / rate))
		data += subdata

	return data

def create_wav_file(fname, sounds, effect='none'):
	
	print 'Effects processor started. Generating wav file named ' + fname + ' with ' + effect + ' effect.'
	
	wv = wave.open(fname, 'w')
	wv.setparams((1, 2, rate, 0, 'NONE', 'not compressed'))

	data = []
	
	# applies the effects
	if effect == 'echo':
		data = effect_echo(data, sounds)
	
	elif effect == 'tremolo':
		data = effect_tremolo(data, sounds)
	
	elif effect == 'distortion':
		data = effect_distortion(data, sounds)
		
	elif effect == 'chorus':
		data = effect_chorus(data, sounds)
	
	# applies null effect in the other cases, including when effect = 'nono', as intended	
	else:
		data = effect_none(data, sounds)
		
	data = normalize(data)

	wvData = ''
	for v in data:
		wvData += pack('h', v)

	wv.writeframes(wvData)
	wv.close()
	
	print 'Effects processor ended.'


if __name__ == '__main__':
	
	pauta = 'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6'
	
	pairs = generate_pairs(pauta)
	
	sounds = generate_sounds(pairs, '888888888')
	
	create_wav_file('test.wav', sounds, 'echo')
