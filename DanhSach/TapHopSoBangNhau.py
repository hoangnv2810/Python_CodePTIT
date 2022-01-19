n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
ans = list(set(a)-set(b))
if len(ans) == 0:
    print("YES")
else:
    print("NO")