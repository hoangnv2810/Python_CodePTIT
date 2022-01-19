msv = "B19DCCN281"
n = int(msv[-1])
for i in range(1, 101+n):
    if i%2 == 0 and i%4 == 0:
        print("FizzBuzz", end=" ")
    elif i%2 == 0 and i%4 != 0:
        print("Fizz", end= " ")
    elif i%4 == 0 and i%2 != 0:
        print("Buzz", end= " ")
    else:
        print(i, end= " ")

