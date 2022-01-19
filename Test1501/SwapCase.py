s = input()
res = ""
for i in s:
    if i.islower():
        res += i.upper()
    elif i.isupper():
        res += i.lower()
    else:
        res += i
print(res)
