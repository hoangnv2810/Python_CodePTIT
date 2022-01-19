s = input()
ans = []
for i in range(len(s)):
    if s[i] == "p":
        ans.append(i)

if len(ans) == 0:
    print(-2)
elif len(ans) >= 2:
    print(ans[1])
else:
    print(-1)
