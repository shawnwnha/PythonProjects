x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()

y =x[0:len(x)/2]
z =x[len(x)/2: ]

z.append(y)

count = len(z)-1

while count >0:
	z[count]=z[count-1]
	count-=1

z[0] =y

print z