#Q.5-: 
def fact(x):
	if x==1 or x==0:
		return 1
	else:
		f=x*fact(x-1)
		return f
		
d={}
for x in range(5):
	num=int(input("enter any number:"))
	a=fact(num)
	d[num]=a
	
print(d)	
	
	
