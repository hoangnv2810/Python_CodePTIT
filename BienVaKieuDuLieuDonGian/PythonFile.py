import re

s = input()
regex = r'[A-Za-z_]+\.py$'
if re.match(regex, s):
    print("yes")
else:
    print("no")