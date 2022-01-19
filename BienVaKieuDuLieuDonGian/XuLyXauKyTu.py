s1 = input().lower().split()
s2 = input().lower().split()
for i in sorted(set(s1+s2)):
    print(i, end= " ")
print()
for i in sorted(set(s1).intersection(set(s2))):
    print(i, end=" ")
