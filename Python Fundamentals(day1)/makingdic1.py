name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
	new_dict = {}
	listaddition = zip(name,favorite_animal)
	new_dict = dict(listaddition)

	print new_dict 

make_dict(name, favorite_animal)


