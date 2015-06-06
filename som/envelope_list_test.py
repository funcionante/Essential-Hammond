from effects_processor import get_env

#this program gives a graphical view of the envelope list

env = get_env()
k = 0

for i in env:

	line = ''
	
	if k%2 == 0:
	
		for j in range (0, int(i*50)):
			line += '*'
		
		print ('%3d')%(k) + ' ' + line
		
	k+=1
