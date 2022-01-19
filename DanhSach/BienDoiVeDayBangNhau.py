n = int(input())
a = [int(x) for x in input().split()]
ans = {}
for i in range (n):
    sum = 0
    for j in range (n):
        sum += abs(a[i]-a[j])
    ans[a[i]] = sum
res = sorted(ans.items(), key= lambda ans: ans[1])
print(f"{res[0][1]} {res[0][0]}")