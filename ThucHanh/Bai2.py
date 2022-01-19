import math
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
soManhMe = []
msv = "B19DCCN281"
a = int(msv[-1])
i, cnt = 1, 0
while cnt <= 30+a-1:
    for j in range(2, int(math.sqrt(i))+1):
        if prime(j) == True and i%(j**2) == 0:
            soManhMe.append(i)
            cnt += 1
    i += 1
print(soManhMe[-1])
