n = int(input())
res = dict()
for i in range(n):
    k, v = [x for x in input().split(" ", 1)]
    res[k] = v.split(" ")

m = int(input())
ans = []
for i in range(m):
    s, name = [x for x in input().split()]
    tmp = s[0]
    for k, v in res.items():
        if k == name:
            chek = False
            for l in v:
                if l.lower() == tmp or tmp == "e" and l == "X":
                    chek = True
            if chek == False:
                ans.append("Access denied")
            else:
                ans.append("OK")

for i in ans:
    print(i)
