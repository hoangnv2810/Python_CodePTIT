col1 = int(input())
row1 = int(input())
col2 = int(input())
row2 = int(input())

if abs(row2-row1) == abs(col2-col1) or col2 == col1 or row2 == row1:
    print("YES")
else:
    print("NO")