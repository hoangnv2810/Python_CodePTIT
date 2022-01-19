p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    list_str = [str(x) for x in input().split()]
    if list_str[0] == "0":
        break
    k = int(list_str[0])
    s = list_str[1]
    if k == 0: break
    res = ""
    for i in range(0, len(s)):
        res = p[(p.index(s[i]) + k) % 28] + res
    print(res)