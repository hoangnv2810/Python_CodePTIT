from SinhVien import SinhVien

if __name__ == '__main__':
    T = int(input())
    listSV = []
    while T > 0:
        listSV.append(SinhVien(input().strip(), input().strip()))
        T -= 1
    listSV.sort()
    print(*listSV, sep="\n")