#Q.3- Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, 


class cop:
	def __init__(self,name,age,work_experience,designation):
		self.name=name
		self.age=age
		self.work_experience=work_experience
		self.designation=designation
	def display(self):
		print("your name is ",self.name )
		print("your age is ",self.age)
		print("your work_experience ",self.work_experience)
		print("your designation",self.designation)
		
	def update(self,name,age,work_experience,designation):
		self.name=name
		self.age=age
		self.work_experience=work_experience
		self.designation=designation
		
class mission(cop):
	def add_mission_details(self):
		super().display()
		super().update(input("enter your name:"),int(input("enter your age:")),int(input("enter your work_experience:")),input("enter your designation:"))
		super().display()
		
c=mission(input("enter your name:"),int(input("enter your age:")),int(input("enter your work_experience:")),input("enter your designation:"))
c.add_mission_details()		
		
	