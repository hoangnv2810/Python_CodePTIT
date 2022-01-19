n = input()
res = 0
def helper(s):
    sum = 0
    for i in s:
        sum += ord(i)-ord('0')
    return str(sum)

while len(n) != 1:
    tmp = helper(n)
    n = tmp
    res += 1
print(res)