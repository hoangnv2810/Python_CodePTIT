import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def ruGon(self):
        temp = math.gcd(self.tu, self.mau)
        self.tu = int(self.tu/temp)
        self.mau = int(self.mau/temp)

    def __str__(self):
        return '{}/{}'.format(self.tu, self.mau)

tu, mau = [int(x) for x in input().split()]
ps = PhanSo(tu, mau)
ps.ruGon()
print(ps.__str__())