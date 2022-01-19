t = int(input())
while t > 0:
    num = input()
    check = True
    for i in range (1, len(num)):
        if num[i]<num[i-1]:
            check = False
            break
    if check == True:
        print("YES")
    else:
        print("NO")
    t -= 1