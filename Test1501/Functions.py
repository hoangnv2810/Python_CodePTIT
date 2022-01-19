import re
T = int(input())
while T > 0:
    s = input()
    a = s.split(',')
    regex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@$#]).{6,12}$'
    res = []
    for i in a:
        if re.match(regex, i):
            res.append(i)

    print(*res, sep=",")

    T -= 1

