class SinhVien:
    def __init__(self, ma, ten, lop):
        self.ma = ma
        self.ten = ten
        self.lop = lop

    def check(self, diemdanh):
        point = 10 - diemdanh.count('v')*2 - diemdanh.count('m')
        if point <= 0:
            return "0 KDDK"
        return point

    def get_ma(self):
        return self.ma

    def __str__(self):
        return f"{self.ma} {self.ten} {self.lop}"
