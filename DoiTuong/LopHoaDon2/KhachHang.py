from datetime import datetime
class KhachHang:
    def __init__(self, ma, ten, so_phong, ngay_den, ngay_di, tien_dv):
        self.ma = f"KH{ma:02}"
        self.ten = ten
        self.so_phong = so_phong
        self.ngay_den = datetime.strptime(ngay_den, '%d/%m/%Y')
        self.ngay_di = datetime.strptime(ngay_di, '%d/%m/%Y')
        self.tien_dv = int(tien_dv)

    def so_ngay_o(self):
        return (datetime.date(self.ngay_di)-datetime.date(self.ngay_den)).days+1

    def tien_phong(self):
        if self.so_phong.startswith("1"):
            return 25
        elif self.so_phong.startswith("2"):
            return 34
        elif self.so_phong.startswith("3"):
            return 50
        else:
            return 80

    def total(self):
        return self.so_ngay_o()*self.tien_phong() + self.tien_dv

    def __lt__(self, other):
        return self.total() > other.total()

    def __str__(self):
        return f"{self.ma} {self.ten} {self.so_phong} {self.so_ngay_o()} {self.total()}"


