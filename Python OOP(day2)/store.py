# class store(object):
# 	def __init__(self, products, location, owner):
# 		self.product = products
# 		self.location = location
# 		self.owner = owner 

# 	def add_product(self,newproducts):
# 		self.product.append(newproducts)
# 		return self

# 	def remove_product(self,productname):
# 		self.product.remove(productname)
# 		return self 

# 	def inventory(self):
# 		print "This is a list of products of", self.owner, "in", self.location
# 		for k in self.product:
# 			if k == "Macbook":
# 				model = "Pro 15 inch"
# 				year = 2018
# 				price = "$2000"
# 			elif k == "Playstation":
# 				model = "3"
# 				year = 2017
# 				price = "$600"
# 			elif k == "PSP":
# 				model = "advanced"
# 				year = 2015
# 				price = "$450"
# 			elif k == "Nintendo":
# 				model = "3ds"
# 				year = 2019
# 				price = "Undefined"
# 			elif k == "WII":
# 				model = "U"
# 				year = 2016
# 				price ="$800"

# 			print "Product Name:",k,"Model:",model, "Year:",year, "Price:",price

# 		return self

# x = store(["Macbook","Playstation","PSP","Nintendo"],"Downtown Seattle","GameStop Seattle")


# x.add_product("WII").remove_product("Macbook").inventory()

x = {"shawn" : "nha","car" : "lambo"}

print x.values()