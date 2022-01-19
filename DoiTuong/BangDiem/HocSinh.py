class HocSinh:
    def __init__(self, ma, ten, diem):
        self.ma = f"HS{ma:02}"
        self.ten = ten
        self.diem = diem

    def sumPoint(self):
        sum = 0
        for i in range(len(self.diem)):
            if i == 0 or i == 1:
                sum += self.diem[i]*2
            else:
                sum += self.diem[i]
        return round(sum/12, 2)

    def rank(self):
        avg = float(self.sumPoint())
        if avg >= 9:
            return "XUAT SAC"
        elif avg >= 8:
            return "GIOI"
        elif avg >= 7:
            return "KHA"
        elif avg >= 5:
            return "TB"
        else:
            return "YEU"

    def __str__(self):
        return '{} {} {} {}'.format(self.ma, self.ten, '%.1f'%self.sumPoint(), self.rank())

    def __gt__(self, other):
        return self.sumPoint() > other.sumPoint()

    def __lt__(self, other):
        if self.sumPoint().__eq__(other.sumPoint()):
            return self.ma < other.ma
        return self.sumPoint() > other.sumPoint()

    def __eq__(self, other):
        return self.sumPoint() == other.sumPoint()


