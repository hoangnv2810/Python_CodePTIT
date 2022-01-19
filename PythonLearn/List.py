# import math
#
#
# # Approach: Sqrt
# # def judgeSquareSum(c: int) -> bool:
# #     for a in range(int(math.sqrt(c))+1):
# #         b = math.sqrt(c-a*a)
# #         if b == int(b):
# #             return True
# #     return False
#
# # Approach: Two pointers
# def judgeSquareSum(c: int) -> bool:
#     left = 0
#     right = int(math.sqrt(c))
#     while left <= right:
#         cur = left * left + right * right
#         if cur == c:
#             return True
#         if cur < c:
#             left += 1
#         if cur > c:
#             left -= 1
#     return False
#
#
# def main():
#     print("Input: ")
#     c = int(input())
#     if judgeSquareSum(c):
#         print("Yes")
#     else:
#         print("No")
#
#
# if __name__ == "__main__":
#     main()

# n = int(input())
# a = []
# for i in input().strip().split():
#     a.append(int(i))
# for i in range(0, n):
#     print(f"So: {a[i]}")
# str = input()
# res = ""
# temp = ""
# for i in range(0, len(str)):
#     if str[i].isdigit():
#         res += temp*int(str[i])
#         temp = ""
#     else:
#         temp += str[i]
# print(res)

import functools
lis = [1, 2, 4, 5, 1, 3]
print(functools.reduce(lambda a, b: a+b, lis))
print(functools.reduce(lambda a, b: a if a > b else b, lis))

import operator
print(functools.reduce(operator.add, lis))
print(functools.reduce(operator.add, ['Hoang', 'Nguyen']))

import itertools
print(list(itertools.accumulate(lis, lambda a, b: a+b)))

#lambda functions
string = "GeeksforGeeks"
print(lambda string: string)
print(lambda x:print(x))
(lambda x : print(x))(string)

#difference between def() and lambda()
def cube(y):
    return y*y*y
print(cube(5))
lambda_cube = lambda y: y*y*y
print(lambda_cube(5))
#Example 1: Python lambda Function with List Comprehension
tables = [lambda x = i: x*10 for i in range(1, 11)]
for table in tables:
    print(table())
#Example 2: Python Lambda Fubction with if-else
Max = lambda a, b: a if(a > b) else b
print(Max(1, 2))
#Example 3: Python Lambda with Multiple statements
List = [[2,3,4], [1,4,136,64],[32,6,9,12]]
#Sort each sublist
sortList = lambda x: (sorted(i) for i in x)
res = sortList(List)
print(list(res))
secondLargest = lambda x, f: (y[len(y)-2] for y in f(x))
ans = secondLargest(List, sortList)
print(list(ans))
#Using lambda() Function with filter()
#Example 1:
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x%2 != 0), li))
print(final_list)
#Example 2:
ages = [13, 90, 17, 59, 21, 60, 5]
adults = list(filter(lambda age: age > 18, ages))
print(adults)
#Using lambda() Function with map()
#Example 1:
final_list = list(map(lambda x:x*2, li))
print(final_list)
#Example 2:
animals = ['dog', 'cat', 'parrot', 'rabbit']
uppered_animals = list(map(lambda animal: str.upper(animal), animals))
print(uppered_animals)

#Map()
#Code 1
def addition(n):
    return n+n
numbers = (1, 2, 3, 4)
res = map(addition, numbers)
print(list(res))
#Code 2
res = map(lambda x: x+x, numbers)
print(list(res))
#Code 3
numbers1 = (1, 2, 3)
numbers2 = (4, 5, 6)
res = map(lambda x, y: x+y, numbers1, numbers2)
print(list(res))
#Code 4
l = ['sat', 'bat', 'cat', 'mat']
test = list(map(list, l))
print(test)

#filter() in Python
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False
sequence = ['a', 'b', 'c', 'd']
filtered = filter(fun, sequence)
for s in filtered:
    print(s)

seq = [0, 1, 2, 3, 4, 5, 8, 15]
res = filter(lambda x: x%2 != 0, seq)
print(list(res))

#Enumerate() in Python
l1 = ["eat","sleep","repeat"]
s1 = "geek"
obj1 = enumerate(l1)
print(list(obj1))
obj2 = enumerate(s1)
print(list(obj2))
