from datetime import datetime
class KhachHang:
    def __init__(self, ma, name, vao, ra):
        self.ma = ma
        self.name = name
        self.vao = datetime.strptime(vao, '%H:%M')
        self.ra = datetime.strptime(ra, '%H:%M')

    def timePlay(self):
        return self.ra-self.vao

    def __str__(self):
        temp = str(self.timePlay()).split(":")
        return f"{self.ma} {self.name} {int(temp[0])} gio {int(temp[1])} phut"
