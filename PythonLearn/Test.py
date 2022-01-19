import math
def checkPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        print(i)
        if n%i == 0:
            return False
    return True
print(checkPrime(4))

# def main():
#     T = int(input())
#     while T > 0:
#         s = input()
#         res = "0"
#         if len(s) == 1:
#             print(s[0])
#             continue
#         tmp = int(s[len(s)-1])
#         for i in reversed(range(len(s)-1)):
#             if i > 0:
#                 res = "0" + res
#             if tmp >= 5:
#                 tmp = int(s[i])+1
#             else:
#                 tmp = int(s[i])
#         res = str(tmp)+res
#         print(res)
#         T -= 1
#
# if __name__ == "__main__":
#     main()