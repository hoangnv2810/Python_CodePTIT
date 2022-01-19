import math

n = int(input())
row = [0]*n
col = [0]*n
for i in range(n):
    tmp = input()
    for j in range(len(tmp)):
        if tmp[j] == 'C':
            row[i] += 1
            col[j] += 1
res = 0
for i in row:
    if i >= 2:
       res += math.comb(i, 2)
for j in col:
    if j >= 2:
        res += math.comb(j, 2)
print(res)