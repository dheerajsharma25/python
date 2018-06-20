#Q.3- Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class temperature:
	def __init__(self,fahrenheit,celsius):
		self.fahrenheit=fahrenheit
		self.celsius=celsius
		
	def convertFahrenheit(self):
		result=(((9*self.celsius)/5)+32)
		print("Temprature in fahrenheit:",result)
	
	def convertCelsius(self):
		result=(((self.fahrenheit-32)*5)/9)
		print("Temprature in celsius",result)
		
t=temperature(int(input("enter temperature in fahrenheit:")),int(input("enter temperature in celsius:")))
t.convertFahrenheit()
t.convertCelsius()