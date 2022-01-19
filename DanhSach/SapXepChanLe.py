n = int(input())
a = []
while len(a) < n:
   s = [int(x) for x in input().split()]
   for i in s:
       a.append(i)

old = list(filter(lambda x: x%2 != 0, a))
old.sort(reverse=True)
even = list(filter(lambda x: x%2 == 0, a))
even.sort()
j, k = 0, 0
for i in a:
    if i%2 == 0 and j < len(even):
        print(even[j], end=" ")
        j += 1
    elif i%2 != 0 and k < len(old):
        print(old[k], end=" ")
        k += 1
