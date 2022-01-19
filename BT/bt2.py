try:
    with open("responses.txt", "r") as f:
        a = f.read().split()
        print(len(a))
except FileNotFoundError:
    print("Khong ton tai file")