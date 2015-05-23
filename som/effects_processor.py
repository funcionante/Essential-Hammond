#!/usr/bin/python
# encoding=utf-8

import wave
import json
from struct import pack
from math import sin, pi
from interpreter import generate_pairs
from synthesizer import generate_sounds

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
	
	print maximum
	
	if maximum != 0:
		for i in range(0, len(data)):
			data[i] = int(float(data[i]) * value / maximum)
	
	return data

#applis null effect and returns the samples
def effect_none(data, sounds):
    
	for sound in sounds:
		data += sound['samples']
	
	data = normalize(data)
		
	return data

#applies echo effect and returns the samples
def effect_echo(data, sounds):
	
	data = effect_none(data, sounds)
	
	#increases the duration by 0.5 seconds, so the echo in the end of the music is not cut
	for i in range(0, 4410 * 5):
		data.append(0)
	
	#double echo (0.1 and 0.2 of delay)
	for i in range (0, len(data)):
		if i > 4410:
			data[i] += 0.5 * data[i-4410]
		
		if i > 4410 * 2:
			data[i] += 0.3 * data[i-4410*2]
	
	data = normalize(data)

	return data
		
def create_wav_file(fname, sounds, rate=44100, effect='none'):

	wv = wave.open(fname, 'w')
	wv.setparams((1, 2, 44100, 0, 'NONE', 'not compressed'))

	data = []
	
	# applies the effects
	if effect == 'none':
		data = effect_none(data, sounds)
	
	elif effect == 'echo':
		data = effect_echo(data, sounds)

	wvData = ''
	for v in data:
		wvData += pack('h', v)

	wv.writeframes(wvData)
	wv.close()


if __name__ == '__main__':
	
	pauta = 'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6'
	
	pairs = generate_pairs(pauta)
	
	sounds = generate_sounds(pairs, '888888888')
	
	create_wav_file('test.wav', sounds, 44100, 'echo')
