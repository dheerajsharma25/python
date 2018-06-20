#Q.2- Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
 
 
class student:
	def __init__(self,name,roll_number):
		self.name=name
		self.roll=roll_number
	def display(self):
		print("your name:",self.name)
		print("your roll_number:",self.roll)

a=student(input("enter name:"),int(input("enter roll:")))
a.display()