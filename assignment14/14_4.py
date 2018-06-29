import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''' 
p=re.compile(r"(.+)! RT (.+): (.+) http:(.+)")
result=p.match(tweet)
print(result[1],result[3])
