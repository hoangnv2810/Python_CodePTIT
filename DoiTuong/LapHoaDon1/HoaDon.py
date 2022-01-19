class HoaDon:
    def __init__(self, ma, name, cu, moi):
        self.ma = f"KH{ma:02}"
        self.name = name
        self.cu = int(cu)
        self.moi = int(moi)

    def total(self):
        chiso = self.moi-self.cu
        if chiso > 100:
            return round((50*100 + 50*150 + (chiso-100)*200)*1.05)
        elif chiso >= 51:
            return round((50*100 + (chiso-50)*150)*1.03)
        else:
            return round(chiso*100*1.02)

    def __str__(self):
        return f"{self.ma} {self.name} {self.total()}"