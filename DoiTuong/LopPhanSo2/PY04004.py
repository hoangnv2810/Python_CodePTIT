import math
class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def ruGon(self):
        temp = math.gcd(self.tu, self.mau)
        self.tu = int(self.tu/temp)
        self.mau = int(self.mau/temp)

    def add(self, PhanSo):
        self.tu = self.tu*PhanSo.mau + PhanSo.tu*self.mau
        self.mau = self.mau*PhanSo.mau

    def __str__(self):
        return '{}/{}'.format(self.tu, self.mau)

a = [int(x) for x in input().split()]
ps1 = PhanSo(a[0], a[1])
ps2 = PhanSo(a[2], a[3])
ps1.add(ps2)
ps1.ruGon()
print(ps1.__str__())