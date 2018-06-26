class AgeTooSmall(Exception):
	pass
age=0
while age<18 :
	age=int(input("enter the age of a person"))
	
	try:
		if age<18:
			raise AgeTooSmallError("the age is too small")
	except error as e:
		print(e)
		