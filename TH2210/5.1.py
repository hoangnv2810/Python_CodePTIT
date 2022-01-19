s = input()
print(s[2])
print(s[2:])
print(s[0:5])
print(s[0:-1])
for i in range(len(s)):
    if i%2 == 0:
        print(i, end="")
    print()

for i in range(len(s)):
    if i%2 != 0:
        print(i, end="")
    print()

print(s[-1:0])

print(len(s))