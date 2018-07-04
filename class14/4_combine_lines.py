#Write a Python program to combine each line from first file with the \
# corresponding line in second file.
with open("abc.txt","r") as f1:
    with open("test.txt","r") as f2:
        with open("new.txt","w") as f3:
            f1_list=f1.readlines()
            f2_list=f2.readlines()
            for x in range(len(f1_list)):
                f3.write(f1_list[x]+f2_list[x])


