class monster(object):
	def __init__(self, name, height, weight):
		self.name = name 
		self.height = height
		self.weight = weight
		self.intelligence = 0

class juka(monster):
	def __init__(self):
		super(juka,self).__init__()
		self.intelligence =10 