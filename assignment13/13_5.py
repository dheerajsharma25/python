try:
	a=int(input("enter the values"))	
except ValueError as b:
	print(b,"enter an integer value")
	

	
try:
	l=[1,3,5,2]
	print(l[6])
except IndexError as b:
	print(b,"\tenter the value of list in range")
	
	

try:
	import sys
	import gw utility.book
except Exception as b:
	print(b)