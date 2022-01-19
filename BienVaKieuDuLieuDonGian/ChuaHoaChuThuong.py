str = input()
cntL = 0
cntH = 0
for i in str:
    if i.islower():
        cntL += 1
    else:
        cntH += 1
if cntL >= cntH:
    print(str.lower())
else:
    print(str.upper())