import re

txt = "j"
x = re.search("j", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")