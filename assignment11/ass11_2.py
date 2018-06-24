#Q2. Make a thread that prints numbers from 1-10, waits for 1 sec between

import threading
from threading import Thread
import time 

class mythread(Thread):
	def run(self):
		for x in range(1,11):
			print(x)
			time.sleep(1)
			
t=mythread()
t.start()