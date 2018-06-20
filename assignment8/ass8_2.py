#Q.2-

import time
format=time.asctime(time.localtime(time.time()))
print("formated time:",format)


#Q.3-

from datetime import datetime
p= datetime.now()
print(p)
print(p.strftime("%B"))


#Q.4- 

from datetime import datetime
p= datetime.now()
print(p)
print(p.strftime("%A"))

#Q.5- 

import datetime
p=datetime.date.today()
print(p)
print(p.day)

#Q.6-

import time
print(time.localtime())

#Q.7- 

import math
a=math.factorial(int(input("enter any number:")))
print("factorial of that number:",a)


#Q.8-

import math
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("GCD:",math.gcd(a,b))

#Q.9-

import os
print(os.getcwd())
print(os.environ)




