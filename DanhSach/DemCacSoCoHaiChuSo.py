s = input()
a = []
tmp = ""
for i in range(len(s)):
    tmp += s[i]
    if len(tmp) == 2:
        a.append(tmp)
        tmp = ""
ans = list(sorted(set(a), key=a.index))
for i in ans:
    print(i, a.count(i))