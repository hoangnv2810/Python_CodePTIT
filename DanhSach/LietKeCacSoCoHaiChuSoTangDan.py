s = input()
# print(list(map(''.join, zip(*[iter(s)]*2))))
a = []
tmp = ""
for i in range(len(s)):
    tmp += s[i]
    if len(tmp) == 2:
        a.append(tmp)
        tmp = ""
ans = list(sorted(set(a)))
for i in ans:
    print(i, end=" ")