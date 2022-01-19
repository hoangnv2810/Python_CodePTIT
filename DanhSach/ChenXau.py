a = input()
b = input()
k = int(input())
res = a[:k-1] + b + a[k-1:]
print(res)