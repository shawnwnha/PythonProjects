class call(object):
	def __init__(self,id_u,name,number,time,reason):
		self.id = id_u
		self.name = name 
		self.number = number
		self.time = time 
		self.reason = reason

	def display(self):
		print self.id, self.name, self.number, self.time, self.reason
		return self



class callcenter(object):
	def __init__(self):
		self.calls = [] 
		self.qsize = len(self.calls)

	def add(self,class_new):
		self.calls.append(class_new)
		return self 

	def remove(self):
		self.calls.pop(0)
		return self 

	def info(self):
		print len(self.calls) 
		for k in self.calls:
			k.display()
		return self
# This is Ninja Challenge: completed
	def delete(self,delete_number):
		x=0
		for k in self.calls:
			if delete_number == k.number:
				self.calls.pop(x)
			x+=1
		return self

	# def sort(self):
	# 	for i in range(0,len(self.calls)-1):
	# 		temp = 0
	# 		if self.calls[i].time[0] < self.calls[i+1].time[0]:
	# 			temp = self.calls[i].time[0]
	# 			self.calls[i]




p1 = call("GorillaGorilla","Shawn Nha",6086306650,"1250","emergency")
p2 = call("GorillaXXX","Sumi Nha",7777777777,"1111","deactivate")
p3 = call("KillaBee","Wu Tang",6666666666,"0606","question")

callcenter = callcenter()

callcenter.add(p1).add(p2).add(p3).delete(7777777777).info()
