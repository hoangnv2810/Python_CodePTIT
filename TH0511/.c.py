n = 0
tmp = None
res = {}
list = []
ox = []
oy = []
while n < 16:
    a = [int(x) for x in input().split()]
    list.append(a[0])
    list.append(a[1])
    ox.append(list[n])
    oy.append(list[n + 1])
    n = n+2
i = 0
for x in ox:
    for i in range(0,8):
        if x == ox[i] and ox.index(x) != i:
            tmp = True
i = 0
for y in oy:
    if tmp == True:
      break
    for i in range(0,8):
        if y == oy[i] and oy.index(y) != i:
            tmp = True
            break
n = 0
i = 0
for n in range(0,8):
    if tmp == True:
        break
    for i in range(0,8):
        if  abs(ox[n] - ox[i]) == abs(oy[n] - oy[i]) and i != n:
            tmp = True
            break
if tmp == True:
  print('YES')
else:
  print('NO')