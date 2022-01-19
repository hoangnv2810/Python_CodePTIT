s = input()
a = []
tmp = ""
for i in range(len(s)):
    tmp += s[i]
    if len(tmp) == 2:
        a.append(tmp)
        tmp = ""
ans = list(sorted(set(a)))
res = {}
for i in ans:
    res[i] = a.count(i)
k = int(input())
check = False
for key, values in res.items():
    if values >= k:
        check = True
        print(key, res[key])
if check == False:
    print("NOT FOUND")