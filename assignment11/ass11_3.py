#Q3. Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list 

import threading
from threading import Thread
import time

class mythread(Thread):	
	def run(self):
		l=[]
		for x in range(5):
			l.append(int(input("enter the no:")))
		print(l)
		bt=time.time()
		time.sleep(2)
		i=2
		for x in l:
			print(x)
			et=time.time()
			print("time taken:",et-bt)
			time.sleep(i)
			i=i+2

t=mythread()
t.start()