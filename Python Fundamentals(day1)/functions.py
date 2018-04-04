def oddeven():
	for k in range(1,2001):
		if(k%2==0):
			print "Number is", k, "this is an even number"
		else:
			print "Number is", k, "this is an odd number"

# oddeven()
def multilist(arr,num):
	for k in range(0,len(arr)):
		arr[k]*=num
	return arr

# b=multilist([1,2,3,4],5)
# print  b





def layered_multiples(arr):
	count = 0
	new_arr= []
 	for k in arr:
 		new_temp=[]
 		for i in range(0,k):
 			new_temp.append(1)
 		new_arr.append(new_temp)
 	return new_arr


# g = layered_multiples([6,8,8,10])

# print g
