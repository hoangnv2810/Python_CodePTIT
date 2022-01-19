def convert(num):
    if num >= 0 and num <= 9:
        return chr(ord('0') + num)
    else:
        return chr(ord('A') + num - 10)

def sovle(num):
    res = ""
    while num > 0:
        res += convert(num%base)
        num = num//base
    return res[::-1]

T = int(input())
while T > 0:
    num, base = [int(x) for x in input().split()]
    print(sovle(num))
    T -= 1

