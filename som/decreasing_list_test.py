from effects_processor import get_decreasing

#this program gives a graphical view of the decreasing list

dec = get_decreasing()
k = 0

for i in dec:

	line = ''
	
	if k%8 == 0:
		
		for j in range (0, int(i*50)):
			line += '*'
			
		print ('%3d')%(k) + ' ' + line
	
	k+=1
