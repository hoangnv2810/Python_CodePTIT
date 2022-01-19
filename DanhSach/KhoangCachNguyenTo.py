n, x = map(int, input().split())
prime = [True for _ in range(10000)]
i = 2
while i*i <= 10000:
    if(prime[i] == True):
        for j in range(i*i, 10000, i):
            prime[j] = False
    i += 1
cnt, tmp = 0, x
print(x, end=" ")
for i in range(2, 10000):
    if cnt == n: break
    if prime[i] == True:
        tmp += i
        cnt += 1
        print(tmp, end=" ")

