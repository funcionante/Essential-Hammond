from effects_processor import get_decreasing

#this program gives a graphical view of the decreasing list

dec = get_decreasing()

for i in dec:

		line = ''
		
		for j in range (0, int(i*50)):
			line += '*'
		
		print line
