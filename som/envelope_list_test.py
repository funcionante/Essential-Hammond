from effects_processor import get_env

#this program gives a graphical vies of the envelope list

env = get_env()

for i in env:

		line = ''
		
		for j in range (0, int(i*50)):
			line += '*'
		
		print line
