b = []
while True:
    a = int(input())
    if a == 0:
        break
    b.append(a)

res = 0
for i in range(1, len(b)):
    if b[i] > b[i-1]:
        res += 1

print(res)
