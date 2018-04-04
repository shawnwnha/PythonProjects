my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

names = my_dict.keys()
numbers = my_dict.values()
combine = zip(names,numbers)
print combine