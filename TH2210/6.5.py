cnt = 0
res = -1
b = []
while True:
  a = int(input())
  b.append(a)
  if a == 0:
    break
  res = max(res,a)

for i in range(len(b)):
  if b[i] == res:
    print(i+1)
    break