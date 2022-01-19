n = int(input())
a = [int(x) for x in input().split()]
prime = [True for i in range(max(a)+1)]
def sieve(n):
    prime[0] = False
    prime[1] = False
    i = 2;
    while i*i <= n:
        if prime[i] == True:
            for j in range(i*i, n+1, i):
                prime[j] = False
        i += 1

sieve(max(a))
b = list(filter(lambda x: prime[x] == True, a))
b.sort()
ans = []
j = 0
for i in range(n):
    if prime[a[i]]:
        ans.append(b[j])
        j += 1
    else:
        ans.append(a[i])

for i in ans:
    print(i, end=" ")