import math

n = int(input())

i = 1
while i <= int(math.sqrt(n))+1:
    if i*i <= n:
        print(i*i, end=" ")
    i+=1