#Q4. Call factorial function using thread.

import threading
from threading import Thread
import time

class factorial(Thread):
	def run(self):
		n=int(input("enter any number:"))
		fact=1
		for i in range(1,n+1):
			fact = fact * i
		print("factorial:",fact)
		
t=factorial()
t.start()