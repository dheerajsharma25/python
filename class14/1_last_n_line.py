#Write a Python program to read last n lines of a file


# #first method
# f=open("abc.txt","r")
# count=0
# a=0
# for line in f:
#     count+=1
#
# f.seek(0)
# for line in f:
#     a+=1
#     if a>=count-5:
#         print(line)
# f.close()


#secound method
f=open("abc.txt","r")
content=f.readlines()
number=int(input("enter the number of lines from last you want to print :"))
for x in range(len(content)-number,len(content)):
    print(content[x])
f.close()