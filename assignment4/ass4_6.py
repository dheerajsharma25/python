d={}
name=""
marks=""
for i in range(3):
	name=input("enter the name of student :")
	marks=int(input("enter the marks of student :"))
	d[name]=marks
print("the dictionary is")
print(d)
s=list(d)
s.sort()
print(s)