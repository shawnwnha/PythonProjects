class patient(object):
	def __init__(self,id_p,name,allegies):
		self.id = id_p
		self.name = name
		self.allegies = allegies
		self.bednumber = None



class hospital(object):
	def __init__(self,name,capacity):
		self.patients =[]
		self.name = name 
		self.capacity = capacity


	def admit(self,p):
		import random
		if self.capacity > len(self.patients):
			self.patients.append(p)
			p.bednumber = random.randint(0,100) 
			print "admitted!"
		else:
			print "sorry for inconvenience"

		return self 

	def discharge(self,p):
		for i in range(0,len(self.patients)):
			if p == self.patients[i].name:
				self.patients[i].bednumber = None
				print self.patients[i].name,"got discharged"
				self.patients.pop(i)
				return self








patient1 = patient("JohnW","John Wick","penut butter")
patient2 = patient("ShawnN","Shawn Nha","water")
patient3 = patient("WooL","Woomin Lee","marijuana")
patient4 = patient("KILLA","Donald T","colored people")



swedish_Hospital = hospital("Swedish Hospital",3)

print swedish_Hospital.capacity

swedish_Hospital.admit(patient1).admit(patient2).admit(patient3).discharge("Shawn Nha")


