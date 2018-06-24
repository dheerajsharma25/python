#Q.1- Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is 
	

class animal:
	def __init__(self,no_of_legs):
		self.no_of_legs=no_of_legs
	
	def display(self):
		print("they have",self.no_of_legs,"legs")

class tiger(animal):
	def ani(self):
		print("Tiger is a carnivorus animal")
		

c=tiger(int(input("enter no legs of tiger:")))
c.ani()
c.display()
		
	
