def draw_stars(arr):
	for k in arr:
		string = ""
		if(type(k)==int):
			for i in range(0,k):
				string += "*"
			print string
		else:
			for j in range(0,len(k)):
				string += str(k[0])
			print string

draw_stars([6,'killa',7,'westside'])

