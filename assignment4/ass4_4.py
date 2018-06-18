set1=[0,0,0]
set2=[ 0,0,0]
set1[0]=int(input("enter a no: "))
set1[1]=int(input("enter a no: "))
set1[2]=int(input("enter a no: "))


set2[0]=int(input("enter a no: "))
set2[1]=int(input("enter a no: "))
set2[2]=int(input("enter a no: "))
a=set(set1)
b=set(set2)
print(a&b)
print(a-b)
