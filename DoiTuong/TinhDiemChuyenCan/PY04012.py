from SinhVien import SinhVien

if __name__ == '__main__':
    listSV = []
    T = int(input())
    for i in range(T):
        listSV.append(SinhVien(input().strip(), input().strip(), input().strip()))
    listDD = []
    for i in range(T):
        s = input().strip()
        listDD.append(s)
    for i in listSV:
        for j in listDD:
            s = j.split()
            if i.get_ma() == s[0]:
                print(i, i.check(s[1]))
                break