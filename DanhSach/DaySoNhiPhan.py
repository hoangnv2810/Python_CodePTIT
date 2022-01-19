n = int(input())
a = [int(x) for x in input().split()]
j , cnt = 0, 0
for i in range(1, len(a)):
    if a[i] != a[j]:
        cnt += 1
    j += 1
print(cnt)