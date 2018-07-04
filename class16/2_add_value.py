# Insert values in the tables.

import pymysql as py

db=py.connect("localhost","root","nihal@85210","library")
cursor=db.cursor()

cursor.execute("insert into book values(001,'looking for alaska','india','fiction')")
cursor.execute("insert into titles values(001,'looking for alaska','1001',101,2005)")
cursor.execute("insert into publishers values(001,'abc','london',10002,11001)")
cursor.execute("insert into zip_code values(001,'ambala','haryana',133203)")
cursor.execute("insert into auther_titles values(001,10010,1012012)")
cursor.execute("insert into authors values(001,'john','null','green')")
cursor.execute("select * from book")
result=cursor.fetchall()
print(result)
db.commit()
db.close()

