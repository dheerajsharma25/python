li=[1,2,'a','b',7,7.0,6,'q']
i1=[]
f=[]
c=[]
for i in li:
	if(type(i)==int):
		i1.append(i)
	elif(type(i)==float):
		f.append(i)
	else:
		c.append(i)
print(li)
print(i1)
print(f)
print(c)