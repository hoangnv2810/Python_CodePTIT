from KhachHang import KhachHang
if __name__ == '__main__':
    T = int(input())
    listKH = []
    for i in range(1, T+1):
        listKH.append(KhachHang(i, input().strip(), input().strip(), input().strip(), input().strip(), input().strip()))
    listKH.sort()
    print(*listKH, sep="\n")