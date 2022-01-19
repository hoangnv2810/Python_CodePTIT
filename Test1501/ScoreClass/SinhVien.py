class SinhVien:
    def __init__(self, name, diem1, diem2, diem3):
        self.name = name
        self.diem1 = float(diem1)
        self.diem2 = float(diem2)
        self.diem3 = float(diem3)

    def tong(self):
        return '%.1f'%(self.diem1*0.1 + self.diem2*0.3 + self.diem3*0.6);

    def __str__(self):
        return "{} {}".format(self.name, self.tong())

T = 4
while T > 0:
    print(SinhVien(input(), input(), input(), input()))
    T -= 1
