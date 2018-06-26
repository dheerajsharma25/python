try:
	raise NameError("Hi there")
except NameError:
    print("An exception")
    raise  

#output would be like!
#NameError: Hi there
