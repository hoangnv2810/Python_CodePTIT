import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, Point):
        return "%.4f" % math.sqrt((self.x-Point.x)**2 + (self.y-Point.y)**2)
