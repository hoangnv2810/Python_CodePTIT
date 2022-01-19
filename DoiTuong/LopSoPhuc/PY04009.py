class SoPhuc:
    def __init__(self, thuc, ao):
        self.thuc = thuc
        self.ao = ao

    def __repr__(self):
        if self.ao >= 0:
            return '{} + {}i'.format(self.thuc, self.ao)
        else:
            return '{} - {}i'.format(self.thuc, abs(self.ao))

def add(sp1:SoPhuc, sp2:SoPhuc):
    return SoPhuc(sp1.thuc + sp2.thuc, sp1.ao + sp2.ao)

def mul(sp1:SoPhuc, sp2:SoPhuc):
    return SoPhuc(sp1.thuc*sp2.thuc-sp1.ao*sp2.ao, sp1.thuc*sp2.ao+sp1.ao*sp2.thuc)

T = int(input())
while T > 0:
    a = [int(x) for x in input().split()]
    sp1 = SoPhuc(a[0], a[1])
    sp2 = SoPhuc(a[2], a[3])
    print(mul(add(sp1, sp2), sp1), mul(add(sp1, sp2), add(sp1, sp2)), sep=", ")
    T -= 1

