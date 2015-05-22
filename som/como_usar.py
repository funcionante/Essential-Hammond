#!/usr/bin/python
# encoding=utf-8

import json
from interpreter import generate_pairs
from synthesizer import generate_sounds
from effects_processor import create_wav_file

#exemplos de pautas
pauta1 = 'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6'
pauta2 = 'Happy Birthday Song:d=4,o=5,b=125:16c, 32p, 32c, 32p, 8d, 32p, 8c, 32p, 8f, 32p, e, 16p, 16c, 32p, 32c, 32p, 8d, 32p, 8c, 32p, 8g, 32p, f, 8p, 16c, 32p, 32c, 32p, 8c6, 32p, 8a, 32p, 8f, 32p, 8e, 32p, 8d, 32p, 16a#, 32p, 32a#, 32p, 8a, 32p, 8f, 32p, 8g, 32p, f'

#pauta ====> interpretador de pautas     
pairs = generate_pairs(pauta1)

#para guardar em json a musica, para quando for preciso criar uma nova interpretação
outfile = open('musica.json', 'w')
json.dump(pairs, outfile)
outfile.close()

#interpretador de pautas ====> sintetizador 

#para abrir o ficheiro json da musica (neste caso, a que se acabou de guardar), para criar uma interpretação
infile = open('musica.json', 'r')
content = infile.read()
pairs = json.loads(content)

sounds = generate_sounds(pairs, "888888888")

#sintetizador ====> processador de efeitos
create_wav_file('test1.wav', sounds, 44100, 'none')


##############################################
#     de um modo mais rápido poderia ser:    #
##############################################
    
pairs = generate_pairs(pauta2)
sounds = generate_sounds(pairs, "888888888")
create_wav_file('test2.wav', sounds, 44100, 'none')

##############################################
#            ou ainda (à pro):               #
##############################################

create_wav_file('test3.wav', generate_sounds(generate_pairs(pauta2), "888888888"), 44100, 'echo')
