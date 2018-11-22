import re
#The match() function returns a match object
# if the text matches the pattern. Otherwise it returns None
pattern = r"Cookie"
sequence = "Cookie"
if re.match(pattern, sequence):
  print("Match!")
else: print("Not a match!")