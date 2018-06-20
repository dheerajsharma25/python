# Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
# 1. Display expenditure and savings 
# 2. Calculate total salary
# 3. Display salary

class expenditure:
	def __init__(self,expenditure,savings):
		self.expenditure=expenditure
		self.savings=savings

	def total_salary(self):
		print("your expenditure is ",self.expenditure)
		print("your saving is",self.savings)
		salary=self.expenditure+self.savings
		print("your salary is",salary)
		
a=expenditure(int(input("enter your expenditure:")),int(input("enter your savings:")))
a.total_salary()