n = int(input())
ans = 0
while n > 0:
    a = int(input())
    if a == 0:
        ans += 1
    n -= 1
print(ans)