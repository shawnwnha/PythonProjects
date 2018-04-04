def cointoss():
	counttails = 0
	countheads = 0

	for k in range(1,5001):
		import random
		probability = round(random.random())
		coin=""

		if(probability == 0):
			coin="tail"
			counttails+=1
		else:
			coin="head"
			countheads+=1

		print "Attempt #"+str(k),": Throwing a coin.... it's a",coin,"! ... Got",countheads,"heads so far and",counttails,"tails so far."


cointoss()