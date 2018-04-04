class cards(object):
	def __init__(self,suit,val):
		self.suit = suit
		self.val = val 
	# def __repr__(self):
	# 	return "this is the {} of {}".format(self.val,self.suit)

# class decks(object):
# 	def __init__(self):
# 		self.deck_list = []
# 		suits = ['spade','clover','diamond','heart']
# 		for suit in suits:
# 			for val in range(0,14):
# 				temp_card = cards(suit,val)
# 				self.deck_list.append(temp_card)

# 	def shuffle(self):
# 		for x in range(0,len(self.deck_list)):
# 			rand_idx = random.randint(0,51)
# 			temp = self.deck_list[x]
# 			self.deck_list[x] = self.deck_list[rand_idx]
# 			self.deck_list[rand_idx] = temp

# d = decks()



x = cards("spade",12)
y = cards("heart",5)
print x 

print y 