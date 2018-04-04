class product(object):
	def __init__(self, price, item_name, weight, brand, status):
		self.price = price 
		self.itemname = item_name
		self.weight = weight 
		self.brand = brand 
		self.status = "For Sale"

	def sell(self):
		self.status = "Sold"
		return self

	def addtax(self,tax):
		self.price *= (1-tax)
		print "After-tax sales Price:",self.price 
		return self 

	def returnP(self,reason):
		if reason =="defective":
			self.status ="defective"
			self.price = 0
			print "defective Item"
		elif reason =="in the box":
			self.status ="for sale"
		elif reason =="opened":
			self.status = "used"
			self.price *=(0.8)
		return self

	def display(self):
		print "ITEM:", self.itemname
		print "Final Price:", self.price 
		print "Brand:",self.brand
		print "Weight:", self.weight
		print "Condition:",self.status


iphone = product(800,"IphoneX","5lb","apple","used")


iphone.addtax(0.09).sell().returnP("opened").display()