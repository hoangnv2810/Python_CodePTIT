class SinhVien:
    def __init__(self, ten, line):
        self.ten = ' '.join(ten.title().split())
        self.ac = line.split()[0]
        self.sm = line.split()[1]

    def __lt__(self, other):
        if self.ac == other.ac and self.sm == other.sm:
            return self.ten < other.ten
        if self.ac == other.ac:
            return self.sm < other.sm
        return self.ac > other.ac


    def __str__(self):
        return f"{self.ten} {self.ac} {self.sm}"

