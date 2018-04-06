class animals(object):
	def __init__(self,name,health):
		self.name =name 
		self.health =health

	def walk(self):
		self.health -= 1 
		return self

	def run(self):
		self.health -= 5 
		return self

	def display_health(self):
		print self.health
		return self


class dog(animals):
	def __init__(self,name,health):
		super(dog, self).__init__(name,health)
		self.health =170

	def pet(self):
		self.health +=5
		return self


class dragon(animals):
	def __init__(self,name,health):
		super(dragon,self).__init__(name,health)
		self.health = 170

	def fly(self):
		self.health -=10
		return self 

	def display_health(self):
		super(dragon,self).display_health()
		print "I am a dragon"

Wonbong = animals("cat",200)

Wonbong.walk().walk().walk().run().run().display_health()

Wooju = dog("dog",170)

Wooju.walk().walk().walk().run().run().display_health()

Dragoo = dragon("drangon",300)

Dragoo.fly().display_health()