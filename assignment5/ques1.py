
year=int(input("enter the year of your choice"))
if (year %4)==0:
	print("year is a leap year")
if(year %100)==0:
	print("year is not a leap year")
if(year %400==0):
	print("year is a leap year")
else:
	print("this isnt a leap year")