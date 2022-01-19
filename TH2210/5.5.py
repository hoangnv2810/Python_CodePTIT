s = input()
ans = []
for i in range(len(s)):
    if s[i] == "f":
        ans.append(i)

if len(ans) == 0:
    print(-1)
elif len(ans) >= 2:
    print(ans[0], ans[-1])
else:
    print(ans[0])
