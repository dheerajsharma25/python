#Q1. Create a threading process such that it sleeps for 5 seconds and then prints out a message.

#method-1
import threading
from threading import Thread
import time 
def display():
	print("child thread:",threading.current_thread().getName())
	bt=time.time()
	time.sleep(3)
	print("child thread:",threading.current_thread())
	et=time.time()
	print("total time taken:",et-bt)

t=Thread(target=display)
t.start()