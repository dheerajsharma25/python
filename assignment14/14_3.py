import re
str="A, very very; irregular_sentence"
str1=re.sub("[^a-zA-Z0-9]+"," ",str)
print(str1)
