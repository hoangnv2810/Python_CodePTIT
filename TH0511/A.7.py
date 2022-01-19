# n = int(input())
# res = dict()
# while n > 0:
#     a = [x for x in input().split()]
#     for i in a:
#         if i in res.keys():
#             res[i] = res[i] + 1
#         else:
#             res[i] = 1
#     n -= 1
#
# for i in sorted(res.keys()):
#     print(i, res[i])

n = int(input())
cnt = {}
for i in range(n):
  for w in input().split():
    cnt[w] = cnt.get(w, 0) + 1
f = [(-count, w) for (w, count) in cnt.items()]
for c, w in sorted(f):
     print(w, -c)