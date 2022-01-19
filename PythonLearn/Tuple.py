#Python Tuples
Tuple1 = ()
print(type(Tuple1))
Tuple1 = ('Hoang', 'For')
print(Tuple1)
list = [1,2,3,4,5]
print(tuple(list))
Tuple1 = tuple("Hoang")
print(Tuple1)
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Hoang', 'Nguyen')
Tuple3 = (Tuple1, Tuple2)
print(Tuple3)
Tuple1 = ('Hoang',)*3
print(Tuple1)
Tuple1 = ('Hoang')
n = 5
for i in range(int(n)):
    Tuple1 = (Tuple1,)
    print(Tuple1)
#Accessing Tuple with Indexing
Tuple1 = tuple("Geeks")
print(Tuple1[0])
#Tuple unpacking
Tuple1 = ("Geeks", "For", "Geeks")
a, b, c = Tuple1
print(a)
print(b)
print(c)
print(len(Tuple1))
#Concatenation of tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('Geeks', 'For', 'Geeks')
Tuple3 = Tuple1 + Tuple2
print(Tuple3)
#Slicing of a Tuple
Tuple1 = tuple('HoangNguyen')
print(Tuple1[1:])
print(Tuple1[::-1])
print(Tuple1[0:5])
#Deleting a tuple
Tuple1 = (0, 1, 2, 3)
del Tuple1