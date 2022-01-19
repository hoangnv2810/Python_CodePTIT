import math
n, k = [int(x) for x in input().split()]
cnt = 0
for i in range(10**(k-1), 10**k-1):
    if math.gcd(n, i) == 1:
        cnt += 1
        print(i, end=(" " if cnt < 10 else "\n"))
    if cnt == 10:
        cnt = 0
# import math
# t = int(input())
# while t > 0:
#     n = input()
#     if math.gcd(int(n), int(n[::-1])) == 1:
#         print("YES")
#     else:
#         print("NO")
#     t -= 1
