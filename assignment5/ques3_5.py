#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
a=int(input("enter age of 1st user "))
b=int(input("enter age of 2nd user "))
c=int(input("enter age of 3rd user "))
if((a<b)and(a<c)):
	print("a is the youngest one")
elif(b<a)and(b<c):
	print("b is the youngest one")
else:
	print("c is the youngest one")
print("oldest is :")	
if((a>b)and(a>c)):
	print("a is the oldest one")
elif(b>a)and(b>c):
	print("b is the oldest one")
else:
	print("c is the oldest one")


		
	

