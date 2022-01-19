import re
s = ""
while True:
    try:
        str = input()
        s += str + " "
    except:
        break

a = re.split(r'[.?!\n]', s)
for i in a:
    if i != "":
        print(' '.join(i.split()).capitalize())
