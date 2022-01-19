from HoaDon import HoaDon
if __name__ == '__main__':
    T = int(input())
    listHD = []
    for i in range(1, T + 1):
        listHD.append(HoaDon(i, input(), input(), input()))
        T -= 1

    listHD.sort(key=lambda x: x.total(), reverse=True)
    print(*listHD, sep="\n")