#Q.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
import math 
class circle:
	def __init__(self,radius):
		self.radius=radius
		
	def area(self):
		getarea=math.pi*self.radius*self.radius
		print(getarea)
	
	def circumference(self):
		result=2*math.pi*self.radius
		print(result)
a=circle(int(input("enter the radius:")))
a.area()
a.circumference()