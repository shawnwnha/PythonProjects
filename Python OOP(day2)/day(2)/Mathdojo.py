class MathDojo(object):
	def __init__(self):
		self.total = 0
			
	def add(self,*arg):
		self.addition = 0
		for k in arg:
			if type(k)== list or type(k)==tuple:
				for i in k:
					self.addition += i
			elif type(k)== int:
				self.addition += k
		self.total += self.addition
		return self
# completed ==========================================================

	def subtract(self,*arg):
		self.subtraction = 0
		for k in arg:
			if type(k)==list or type(k)==tuple:
				for i in k:
					self.subtraction += i
			elif type(k)==int:
				self.subtraction += k
		self.total -= self.subtraction
		return self
# completed ==========================================================

	def result(self):
		print self.total
		return self

x = MathDojo()

x.add([1,2,3],2).add(2,5).subtract([1,2,3],1).result()