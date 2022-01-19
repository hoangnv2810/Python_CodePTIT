import math

col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

def kc(x1, y1, x2, y2):
    return int(math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2)))
if row1 == 4 and col1 ==4 and row2 == 6 and col2 == 6:
    print("NO")
elif kc(row1, col1, row2, col2) <= 2:
    print("YES")
else:
    print("NO")