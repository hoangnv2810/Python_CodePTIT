import re

T = int(input())
while T > 0:
    a = re.findall('\d+', input())
    b = [int(x) for x in a]
    print(max(b))
    T -= 1