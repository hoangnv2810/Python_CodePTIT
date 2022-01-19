n = int(input())
num = int(n)
a = []
while n > 1:
    a.append(int(input()))
    n -= 1
for i in range(1, num+1):
    if i not in a:
        print(i)
        break
