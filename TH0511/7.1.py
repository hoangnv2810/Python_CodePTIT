a = [int(x) for x in input().split()]

mp = dict()

for i in range(len(a)):
    if a[i] in mp.keys():
        mp[a[i]] += 1
    else:
        mp[a[i]] = 1

for i in mp:
    if mp[i] == 1:
        print(i, end=" ")