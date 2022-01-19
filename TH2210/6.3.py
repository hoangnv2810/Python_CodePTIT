#
#
#
# string = input()
# print (string[2])
# #print (string[len(string)-2])
# print(string[-2])
# print (string[0:5])
# print (string[0:len(string)-2])
# ans = ""
# for i in range(len(string)):
#     if i%2 == 0:
#         ans += string[i]
# print(ans)
#
# ans = ""
# for i in range(len(string)):
#     if i%2 != 0:
#         ans += string[i]
# print(ans)
#
#
# rever = (list(reversed(string)))
# ans4 = ''
# for a in range (len(rever)):
#     ans4 += rever[a]
# print (ans4)
# ans3 = ''
# counter = 0
# for i in range (len(rever)//2 + len(rever)%2):
#     ans3 += rever[counter]
#     counter += 2
#     ans3 = list(ans3)
# rans_3 = ''
# for i in range (len(ans3)):
#     rans_3 += ans3[i]
#
# print (rans_3)
# print(len(string))


# n = int(input())
# i = 1
# while 2 ** i <= n:
#   i += 1
# print(i - 1, 2 ** (i - 1))

string = input()

rever = (list(reversed(string)))

ans3 = ''
counter = 0
for i in range (len(rever)//2 + len(rever)%2):
    ans3 += rever[counter]
    counter += 2
    ans3 = list(ans3)
print(ans3)

rans_3 = ''
for i in range (len(ans3)):
    rans_3 += ans3[i]

print (rans_3)