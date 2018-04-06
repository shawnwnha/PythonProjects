class Bike(object):
	def __init__(self, price, max_speed, miles):
		self.price = price 
		self.max_speed = max_speed
		self.miles = 0

	def displayinfo(self):
		print self.price, self.max_speed, self.miles
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		return self

	def reverse(self):
		print "Reversing"
		if self.miles >0:
			self.miles -= 5
		return self


bmw = Bike("$100,000" , "340km/h", "1600 miles")
yamaha = Bike("$15,000" , "333km/h", "19 miles")
kawasaki = Bike("$20,000" , "360km/h", "200 miles")

bmw.ride().ride().ride().reverse().displayinfo()
yamaha.ride().ride().reverse().reverse().displayinfo()
kawasaki.reverse().reverse().reverse().displayinfo()





# When method function does not return any value, it should return self so that it can be chained!!!!!!!!!!!!!!!!!!!!!!!!!!!! (WHEN FUNCTION DOES NOT RETURN VALUE BUT WANTS TO BE CHAINED, IT SHOULD BE "RETURN SELF")
# adding if statements to prevent reverse(self) shows negative value. 