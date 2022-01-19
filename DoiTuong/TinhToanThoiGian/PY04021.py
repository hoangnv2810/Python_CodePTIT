from KhachHang import KhachHang
if __name__ == '__main__':
    T = int(input())
    listKH = []
    while T > 0:
        ma = input()
        ten = input()
        vao = input()
        ra = input()
        listKH.append(KhachHang(ma, ten, vao, ra))
        T -= 1
    listKH.sort(key=lambda x: x.timePlay(), reverse=True)
    for i in listKH:
        print(i)
