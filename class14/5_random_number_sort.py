#Write a Python program to write 10 random numbers into a file.\
#  Read the file and then sort the numbers and then store it to another file.
import os
import random
random_list=[]
for x in range(100):
    random_list.append(x)
random.shuffle(random_list)
with open("random_number_unshorted.txt","w") as f1:
    for x in range(10):
        f1.write(str(random_list[x])+"\n")
os.remove("random_word_shorted.txt")
with open("random_number_unshorted.txt","r+") as f1:
    with open("random_word_shorted.txt","w") as f2:
        random_list1=f1.readlines()
        for x in range(len(random_list1)):
            random_list1[x]=int(random_list1[x])
        random_list1.sort()
        # f2.write("".join(random_list1))
        for x in random_list1:
            f2.write(str(x)+"\n")
