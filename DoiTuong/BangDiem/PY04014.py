from HocSinh import HocSinh
if __name__ == '__main__':
    T = int(input())
    listHS = []
    for i in range(1, T + 1):
        name = input()
        diem = [float(x) for x in input().split()]
        listHS.append(HocSinh(i, name, diem))

    listHS.sort()
    print(*listHS, sep="\n")