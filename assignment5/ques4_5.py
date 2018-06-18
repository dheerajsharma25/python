n=int(input("enter an number between 1-200   "))
p1="no prize"
p2="Wooden Dog"
p3="Book"
p4="Chocolates"
if((n>=1)and(n<=50)):
	print("Sorry! No prize this time.")
elif((n>=51)and(n<=150)):
		print("Congratulations!you have won  %s"%(p2))
elif((n>=151)and(n<=180)):
		print("Congratulations!you have won %s"%(p3))
elif((n>=181)and(n<=200)):
		print("Congratulations!you have won %s"%(n,p4))
else:
	print("please enter correct number")

