#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user. 
q=int(input("enter the units "))
q1=q*100
if(q1>1000):
	dis=((q/10)*100)
	q1=q1-dis
	print("total cost is %d"%(q1))
else:
		print("no discount and tatal cost is %d"%(q1))
