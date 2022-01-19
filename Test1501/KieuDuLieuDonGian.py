import math
res = []
def facto(num):
    tmp = []
    while num%2 == 0:
        tmp.append(2)
        num /= 2
    for i in range(3, int(math.sqrt(num))+1, 2):
        while num%i == 0:
            tmp.append(i)
            num = int(num/i)
    if num > 1:
        tmp.append(num)
    res.append(sum(tmp))


if __name__ == "__main__":
    T = int(input())
    while T > 0:
        n = int(input())
        facto(n)
        T -= 1

ans = 1
for i in res:
    ans *= i
print(int(ans))