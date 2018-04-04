"""
words = "It's thanksgiving day. It's my birthday,too!"

print words.find("day")

wordsnew = words.replace("day", "month")

print wordsnew

"""
"""
x = [2,54,-2,7,12,98]

print min(x)
print max(x)
"""
"""
newlist = []
x = ["hello",2,54,-2,7,12,98,"world"]

newlist.append(x[0])
newlist.append(x[len(x)-1])

print newlist
"""
"""
x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()

y = x[0: len(x)/2]
z = x[len(x)/2: ]

z.append(y)

length = len(z)-1

while length>0:
	z[length] =z[length-1]
	length -=1

z[0] = y

print z
"""