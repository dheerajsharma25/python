li=[]
n=int(input("enter the number of values u want to enter"))
for i in range(0,n):
	j=input("enter the value : ")
	li.append(j)
print(li)
j=input("enter the value u want to search  ")
for i in range(0,n):
	if(j==li[i]):
		print("element found ")
		li.remove(j)
		print("element deleted")
print(li)