
l = ['killa','westside',777]


string = "String: "
sum = 0

for k in l:
	if type(k) == str:
		string+= k + ' '
	else:
		sum += k 

count = 0
result = 0

while count<len(l)-1:
	if type(l[count]) == type(l[count+1]):
		result +=1
	count +=1

if result == len(l)-1:
	if(isinstance(l[0],int)):
		print "this is Integer list"
		print "sum: " +str(sum)
	else:
		print "this is String list"
		print string
else:
	print "this is mixed string "
	print "sum: " +str(sum), string


