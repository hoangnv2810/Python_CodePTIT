class Circle():
    def __init__(self, o, r):
        self.tam = o
        self.r = r

    def describe(self):
        print(f"Hinh tron tam O({self.tam[0]},{self.tam[1]}) ban kinh R = {self.r}")

    def get_area(self):
        print(3.14*(self.r**2))

    def get_perimeter(self):
        print(3.14*self.r*2)

a = Circle((1, 2), 3)
a.describe()
a.get_area()
a.get_perimeter()