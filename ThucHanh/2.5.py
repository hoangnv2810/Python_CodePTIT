num = input()
try:
    i = num.index(".")
    print(num[i+1])
except:
    print(0)
