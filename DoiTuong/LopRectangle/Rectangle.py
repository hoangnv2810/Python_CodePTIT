class Rectangle:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color.title()

    def perimeter(self):
        return (self.width + self.height)*2

    def area(self):
        return self.width*self.height

    # def color(self):
    #     return str(self.color.title())

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color))
        t -= 1