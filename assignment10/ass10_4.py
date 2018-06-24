#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area. 


class shape:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		self.result=self.length*self.breadth
		
class rectangle(shape):
	def arearect(self):
		print("area of rectangle:",self.result)

class square(shape):
	def areasqur(self):
		print("area of square:",self.result)
		
	
r=rectangle(int(input("length of rectangle:")),int(input("breadth of rectangle:")))
r.area()
r.arearect()

s=square(int(input("length of square:")),int(input("breadth of square:")))
s.area()
s.areasqur()