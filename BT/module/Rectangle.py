class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def primeter(self):
        print(f"Chu vi: {(self.width+self.height)*2}")

    def area(self):
        print(f"Dien Tich: {self.width*self.height}")

my_rec = Rectangle(2, 3)
my_rec.primeter()
my_rec.area()