n = int(input())
a = []
res = 0
for i in input().split():
    a.append(int(i))
for i in range(0, n-1):
    for j in range(i+1, n):
        if(a[i] > a[j]): 
            res += 1
print(res)