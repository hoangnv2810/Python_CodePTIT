from datetime import datetime
class ThiSinh:
    def __init__(self, name, dob, diem1, diem2, diem3):
        self.name = name
        self.dob = datetime.strptime(dob, '%d/%m/%Y')
        self.diem1 = float(diem1)
        self.diem2 = float(diem2)
        self.diem3 = float(diem3)

    def sumPoint(self):
        return '%.1f' % (self.diem1 + self.diem2 + self.diem3)

    def __str__(self):
        return self.name + " " + datetime.date(self.dob).strftime('%d/%m/%Y') + " " + self.sumPoint()

T = 5
while T > 0:
    name = input()
    dob = input()
    diem1 = input()
    diem2 = input()
    diem3 = input()
    ts = ThiSinh(name, dob, diem1, diem2, diem3)
    print(ts)
    break
    T -= 1