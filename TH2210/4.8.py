n = int(input())

def solve(n):
    if n == 0 or n == 1:
        return 1
    return solve(n-1)*n

sum = 0
for i in range(1, n+1):
    sum += solve(i)

print(sum)