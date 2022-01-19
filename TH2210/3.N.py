listX = []
listY = []

x1 = int(input())
listX.append(x1)
y1 = int(input())
listY.append(y1)
x2 = int(input())
listX.append(x2)
y2 = int(input())
listY.append(y2)
x3 = int(input())
listX.append(x3)
y3 = int(input())
listY.append(y3)

x4 = [x for x in listX if listX.count(x) == 1]
y4 = [y for y in listY if listY.count(y) == 1]
print(x4[0])
print(y4[0])