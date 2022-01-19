while True:
    num = input()
    try:
        print(int(num))
        break
    except ValueError:
        print("Nhap lai: ")