from struct import pack
import wave
import json
from interpreter import interpreter
from synthesizer import synthesizer

pauta = 'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6'
data = interpreter(pauta)
outfile = open('1pauta.json', 'w')
json.dump(data, outfile)
outfile.close()




infile = open('1pauta.json', 'r')
content = infile.read()

#json from interpreter with the info of notes and duration. pairs frequence-time
pairs = json.loads(content)

sounds = synthesizer(pairs, "888888888")

outfile = open('1inter.json', 'w')
json.dump(sounds, outfile)
outfile.close()





rate=44100
wv = wave.open('test.wav', 'w')
wv.setparams((1, 2, rate, 0, 'NONE', 'not compressed'))

infile = open('1inter.json', 'r')
content = infile.read()	
data = json.loads(content)
print data

wvData=''

for note in data:
	for v in note['samples']:
		wvData += pack('h',v)


wv.writeframes(wvData)
wv.close()
