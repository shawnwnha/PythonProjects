class User(object):
	def __init__(self,name,email,phonenumber):
		self.name = name 
		self.email = email
		self.phonenumber = phonenumber
		self.login = False 



shawn = User("Shawn Nha","Shawn.W.Nha@gmail.com","+16086306650")
killa = User("KIlla","googogogo")

print shawn.name, shawn.email, shawn.phonenumber
print killa.email, killa.phonenumber

