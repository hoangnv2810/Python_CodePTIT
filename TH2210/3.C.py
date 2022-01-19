cot1 = int(input())
hang1 = int(input())
cot2 = int(input())
hang2 = int(input())

if hang2 == hang1 or hang2 == cot1 or cot2 == cot1 or cot2 == hang1:
    print("YES")
else:
    print("NO")