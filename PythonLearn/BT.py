# n = int(input())
# a = [[x for x in input().split()] for y in range(n)]
# print(a)
# t = 10
# res = []
# while t > 0:
#     a = input()
#     b = [int(x) for x in a.split()]
#     t -= len(b)
#     for i in b:
#         res.append(i%42)
# print(len(set(res)))

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     cnt = 1
#     while n != 1:
#         if n % 2 == 0:
#             n /= 2
#             cnt += 1
#         else:
#             n = n * 3 + 1
#             cnt += 1
#     print(cnt)

# t = int(input())
# while t > 0:
#     n = int(input())
#     a = {}
#     while n > 0:
#         r = int(input())
#         if r in a:
#             a[r] += 1
#         else:
#             a[r] = 1
#         n -= 1
#     res_key = max(dict(sorted(a.items(), key=lambda cmp: (cmp[1], cmp[0]))), key=a.get) #key=lambda cmp: cmp[::-1]
#     print(res_key)
#     t -= 1

# def SoNhoNhatConThieu(a):
#     largest = max(a)
#     if largest < 1:
#         return 1
#     tmp = set(a)
#     tmp1 = set(range(1, largest+1))
#     res = tmp1-tmp
#     if len(res) == 0:
#         return largest+1
#     else:
#         return min(res)
#
# n = int(input())
# a = [int(x) for x in input().split()]
# print(SoNhoNhatConThieu(a))

#Day So Nhi Phan
# n = int(input())
# a = [int(x) for x in input().split()]
# j , cnt = 0, 0
# for i in range(1, len(a)):
#     if a[i] != a[j]:
#         cnt += 1
#     j += 1
# print(cnt)

#Lai suat ngan hang
# import math
# t = int(input())
# while t > 0:
#     n, x, m = [float(x) for x in input().split()]
#     print(math.ceil(math.log(m/n, 1+x/100)))
#     t -= 1

#Tong chu so thuan nghich
# t = int(input())
# def check(n):
#     if len(n) == 1:
#         return False
#     m = n[::-1]
#     if n == m:
#         return True
#     else:
#         return False
# while t > 0:
#     n = input()
#     m = [int(x) for x in list(n)]
#     if check(str(sum(m))):
#         print("YES")
#     else:
#         print("NO")
#
#     t -= 1

#Tong chu so nguyen to
# t = int(input())
# import math
# def check(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n%i == 0:
#             return False
#     return True
# while t > 0:
#     n = input()
#     m = [int(x) for x in list(n)]
#     if check(sum(m)):
#         print("YES")
#     else:
#         print("NO")
#
#     t -= 1

#So chia het cho 3
# t = int(input())
# import math
# def check(n):
#     if n%3 == 0:
#         return True
#     return False
# while t > 0:
#     n = input()
#     m = [int(x) for x in list(n)]
#     if check(sum(m)):
#         print("YES")
#     else:
#         print("NO")
#
#     t -= 1

#Tich chu so
# t = int(input())
# while t > 0:
#     n = input()
#     m = [int(x) for x in list(n)]
#     res = 1
#     for i in m:
#         if i != 0:
#             res *= i
#     print(res)
#     t -= 1

#So xen ke
# t = int(input())
# def check(n):
#     if len(n)%2 == 0 or n[0] == n[1]:
#         return False
#     for i in range(2, len(n)):
#         if i%2 == 0:
#             if n[i-2] != n[i]:
#                 return False
#     return True
#
# while t > 0:
#     n = input()
#     if check(n):
#         print("YES")
#     else:
#         print("NO")
#     t -= 1

#Chen le nguyen to
# import math
# t = int(input())
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n%i == 0:
#             return False
#     return True
# def check(m):
#     for i in range(0, len(m)):
#         if i%2 == 0 and m[i]%2 != 0:
#             return False
#         elif i%2 == 1 and m[i]%2 == 0:
#             return False
#     return True
# while t > 0:
#     n = input()
#     m = [int(x) for x in list(n)]
#     if isPrime(sum(m)) and check(m):
#         print("YES")
#     else:
#         print("NO")
#     t -= 1

#Vi tri nguyen to
# import math
# t = int(input())
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n%i == 0:
#             return False
#     return True
#
# def check(m):
#     for i in range(0, len(m)):
#         if isPrime(i) and isPrime(m[i]) == False:
#             return False
#         elif isPrime(i) == False and isPrime(m[i]) == True:
#             return False
#     return True
#
# while t > 0:
#     n = input()
#     m = [int(x) for x in list(n)]
#     if check(m):
#         print("YES")
#     else:
#         print("NO")
#     t -= 1

#Doan cuoi nguyen to
# import math
# t = int(input())
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n%i == 0:
#             return False
#     return True
# while t > 0:
#     n = input();
#     if isPrime(int(n[-4:])):
#         print("YES")
#     else:
#         print("NO")
#     t -= 1

# Dau cuoi nguyen to
# import math
# t = int(input())
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n%i == 0:
#             return False
#     return True
# while t > 0:
#     n = input();
#     if isPrime(int(n[-3:])) and isPrime(int(n[:3])):
#         print("YES")
#     else:
#         print("NO")
#     t -= 1

#Tong chu so Tich chu so
# t = int(input())
# while t > 0:
#     n = input()
#     cntOld = int(len(n)/2)
#     sumEven = 0
#     mulOld = 1
#     cntZero = 0
#     for i in range(0, len(n)):
#         if i%2 == 0:
#             sumEven += int(n[i])
#         elif i%2 == 1 and n[i] != "0":
#             mulOld *= int(n[i])
#         elif i%2 == 1 and n[i] == "0":
#             cntZero += 1
#     if cntZero == cntOld:
#         mulOld = 0
#     print(sumEven, mulOld)
#     t -= 1

#Tich chu so Tong chu so
# t = int(input())
# while t > 0:
#     n = input()
#     sumOld = 0
#     mulEven = 1
#     for i in range(0, len(n)):
#         if i%2 == 1:
#             sumOld += int(n[i])
#         elif i%2 == 0 and n[i] != "0":
#             mulEven *= int(n[i])
#     print(mulEven, sumOld)
#     t -= 1

#Uu the nguyen to
# import math
# t = int(input())
# def isPrime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(math.sqrt(n))+1):
#         if n%i == 0:
#             return False
#     return True
# while t > 0:
#     n = input()
#     cntPrime = 0
#     for i in n:
#         if isPrime(int(i)):
#             cntPrime += 1
#     if isPrime(len(n)) and cntPrime > len(n)-cntPrime:
#         print("YES")
#     else:
#         print("NO")
#     t -= 1

#So sao nguyen to cung nhau
# import math
# t = int(input())
# while t > 0:
#     n = input()
#     if math.gcd(int(n), int(n[::-1])) == 1:
#         print("YES")
#     else:
#         print("NO")
#     t -= 1

#Nguyen to cung nhau
# import math
# n, k = [int(x) for x in input().split()]
# cnt = 0
# for i in range(10**(k-1), 10**k-1):
#     if math.gcd(n, i) == 1:
#         cnt += 1
#         print(i, end=(" " if cnt < 10 else "\n"))
#     if cnt == 10:
#         cnt = 0

#Bo ba nguyen to cung nhau
# import math
# l, r = [int(x) for x in input().split()]
# for i in range(l, r-1):
#     for j in range(i+1, r):
#         for k in range(j+1, r+1):
#             if math.gcd(i, j) == 1 and math.gcd(i, k) == 1 and math.gcd(j, k) == 1:
#                 print(f"({i}, {j}, {k})")

#Tinh tong phan thuc
# t = int(input())
# while t > 0:
#     n = int(input())
#     res = 0
#     if n%2 == 1:
#         for i in range(1, n+1,2):
#             res += 1.0/i
#     else:
#         for i in range(2, n+1, 2):
#             res += 1.0/i
#     print(format(round(res, 6), '.6f'))
#     t -= 1

#Xau thang bang
# t = int(input())
# def check(s):
#     for i in range(1, len(s)):
#         if abs(ord(s[i])-ord(s[i-1])) != abs(ord(s[-i-1])-ord(s[-i])):
#             return False
#     return True
#
# while t > 0:
#     s = input()
#     if check(s):
#         print("YES")
#     else:
#         print("NO")
#     t -= 1

#Ma hoa 1
# t = int(input())
# while t > 0:
#     s = input()
#     s += "*"
#     res = ""
#     cnt = 1
#     for i in range(0, len(s)-1):
#         if s[i] == s[i+1]:
#             cnt += 1
#         else:
#             res += str(cnt) + s[i]
#             cnt = 1
#     print(res)
#     t -= 1

#Ma hoa 2
# p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
# while True:
#     list_str = [str(x) for x in input().split()]
#     if list_str[0] == "0":
#         break
#     k = int(list_str[0])
#     s = list_str[1]
#     if k == 0: break
#     res = ""
#     for i in range(0, len(s)):
#         res = p[(p.index(s[i]) + k) % 28] + res
#     print(res)

#Tinh diem trung binh
n = int(input())
def check(a):
    Min = min(a)
    Max = max(a)
    return [x for x in a if x != Min and x != Max]
a = [float(x) for x in input().split()]
b = check(a)
print(round(sum(b)/len(b), 2))
