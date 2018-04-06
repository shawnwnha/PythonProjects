
class car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price 
		self.speed = speed
		self.fuel = fuel 
		self.mileage = mileage

		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12

		self.display_all()

	def display_all(self):
		print "Price:", self.price
		print "Speed:", self.speed
		print "Fuel:", self.fuel
		print "mileage:", self.mileage
		print "tax:", self.tax


car1 = car(2000,"35mph","FULL","15mpg")
car2 = car(1000,"66mph","FULL","500mpg")
car3 = car(3000,"80mph","Half","10mpg")
car4 = car(4000,"100mph","FULL","10mpg")
car5 = car(100000,"170mph","Half","10mpg")
car6 = car(200000,"200mph","FULL","0mpg")

