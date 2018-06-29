import re
str="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
str1=re.compile(r"\b[Bb][a-zA-Z0-9]+")
str2=str1.findall(str)
print(str2)