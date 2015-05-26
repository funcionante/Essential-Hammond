#!/usr/bin/python
# encoding=utf-8

#não esquecer imports
import json
from interpreter import generate_pairs, create_image
from synthesizer import generate_sounds
from effects_processor import create_wav_file

#exemplos de pautas
pauta1 = 'The Simpsons:d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#,8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6'
pauta2 = 'Happy Birthday Song:d=4,o=5,b=125:16c,32p,32c,32p,8d,32p,8c,32p,8f,32p,e,16p,16c,32p,32c,32p,8d,32p,8c,32p,8g,32p,f,8p,16c,32p,32c,32p,8c6,32p,8a,32p,8f,32p,8e,32p,8d,8p,16a#,32p,32a#,32p,8a,32p,8f,32p,8g,32p,f'
pauta3 = 'We Wish You:d=4,o=5,b=40:16a4,16d,32d,32e,32d,32c#,16b4,16g4,16b4,16e,32e,32f#,32e,32d,16c#,16a4,16c#,16f#,32f#,32g,32f#,32e,16d,16b4,16a4,16b4,16e,16c#,8d'
pauta4 = 'Barbie girl:d=4,o=5,b=125:8g#,8e,8g#,8c#6,a,p,8f#,8d#,8f#,8b,g#,8f#,8e,p,8e,8c#,f#,c#,p,8f#,8e,g#,f# '
pauta5 = 'Indiana:d=4,o=5,b=250:e,8p,8f,8g,8p,1c6,8p.,d,8p,8e,1f,p.,g,8p,8a,8b,8p,1f6,p,a,8p,8b,2c6,2d6,2e6,e,8p,8f,8g,8p,1c6,p,d6,8p,8e6,1f.6,g,8p,8g,e.6,8p,d6,8p,8g,e.6,8p,d6,8p,8g,f.6,8p,e6,8p,8d6,2c6'

#pauta ====> interpretador de pautas     
'''pairs = generate_pairs(pauta1)

#para guardar em json a musica, para quando for preciso criar uma nova interpretação
outfile = open('musica.json', 'w')
json.dump(pairs, outfile)
outfile.close()

#interpretador de pautas ====> sintetizador 

#para abrir o ficheiro json da musica (neste caso, a que se acabou de guardar), para criar uma interpretação
infile = open('musica.json', 'r')
content = infile.read()
pairs = json.loads(content)

sounds = generate_sounds(pairs, '888888888')

#sintetizador ====> processador de efeitos
create_wav_file('test1.wav', sounds, 44100, 'none')


##############################################
#     de um modo mais rápido poderia ser:    #
##############################################
    
pairs = generate_pairs(pauta2)
sounds = generate_sounds(pairs, '888888888')
create_wav_file('test2.wav', sounds, 44100, 'none')

##############################################
#            ou ainda (à pro):               #
##############################################

create_wav_file('test3.wav', generate_sounds(generate_pairs(pauta3), '888888888'), 44100, 'echo')'''

##############################################
#    para gerar uma imagem de uma música:    #
##############################################

create_image(generate_pairs(pauta1), 'test3.jpg')