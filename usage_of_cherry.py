##############################
#							 #
#		  CHERRYPY			 #
#	BY DENNIS BARTASHEVICH	 #
#							 #
##############################

#Create Song
#http://localhost:8080/createSong?name=noteDaPauta&notes=notasDaPauta
#nomeDaPauta = "The Simpsons"
#notasDaPauta = "d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#, 8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6"
#Exemplo: http://localhost:2223/createSong?name=The+Simpsons&notes=d%3D4%2Co%3D5%2Cb%3D160%3Ac.6%2Ce6%2Cf%236%2C8a6%2Cg.6%2Ce6%2Cc6%2C8a%2C8f%23%2C+8f%23%2C8f%23%2C2g%2C8p%2C8p%2C8f%23%2C8f%23%2C8f%23%2C8g%2Ca%23.%2C8c6%2C8c6%2C8c6%2Cc6

#Create Interpretation
#http://localhost:2223/createInterpretation?registration=reg&id=idDaMusica&effects=efe&name=nomeDaInterpretacao
#reg = 888888888
#idDaMusica = 1
#efe = "none"
#nomeDaInterpretacao = "The Simpsons : Part 1"
#Exemplo: http://localhost:2223/createInterpretation?registration=888888888&id=40&effects=none&name=LOL

#Obter Imagem da Pauta (ID da Pauta)
#http://localhost:8080/getWaveForm?id=1
#(http://localhost:8080/getWaveForm?id=1) == (http://localhost:8080/img/1.jpg)
#Podes utilizar assim <img src="getWaveForm?id=1" alt=""></img>

#Obter fichero .wav da Interpretacao (ID da Interpretacao)
#http://localhost:8080/getWaveFile?id=1
#(http://localhost:8080/getWaveFile?id=1) == (http://localhost:8080/audio/1.wav)
#Podes utilizar assim <audio controls><source src="getWaveFile?id=1" type="audio/mpeg">Your browser does not support the audio element.</audio>

#listSongs() -> Devolve um JSON da tabela interpretacao (id,id_music,nome,registo,effects,upvotes,downvotes)
#Exemplo: [{"notes": "d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#, 8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6", "id": 1, "name": "The Simpsons"}, {"notes": "d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#, 8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6", "id": 2, "name": "The Simpsons"}]

#listNotes() -> Devolve um JSON da table musics (id,nome,notas)
#Exemplo: [{"name": "LOL", "id_music": 1, "downvotes": null, "effects": "none", "registration": 888888888, "upvotes": null, "id": 1}, {"name": "LOL", "id_music": 40, "downvotes": null, "effects": "echo", "registration": 888888888, "upvotes": null, "id": 2}, {"name": "LOLECHO", "id_music": 1, "downvotes": null, "effects": "echo", "registration": 888888888, "upvotes": null, "id": 3}]

#Obter notas de uma pauta (id da pauta)
#http://localhost:8080/getNotes?id=1
#Devolve o seguinte: d=4,o=5,b=160:c.6,e6,f#6,8a6,g.6,e6,c6,8a,8f#, 8f#,8f#,2g,8p,8p,8f#,8f#,8f#,8g,a#.,8c6,8c6,8c6,c6

#Obter musicas de uma pauta (id da pauta)
#http://localhost:8080/listSongFiles?id=1
#Devolve o seguinte: [{"name": "LOL", "id_music": 1, "downvotes": null, "effects": "none", "registration": 888888888, "upvotes": null, "id": 1}, {"name": "LOLECHO", "id_music": 1, "downvotes": null, "effects": "echo", "registration": 888888888, "upvotes": null, "id": 3}]