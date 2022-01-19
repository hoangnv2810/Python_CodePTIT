class Matrix():
    def __init__(self, m, n, a):
        self.m = m
        self.n = n
        self.a = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                self.a[i][j] = a[i][j]

    def cong(self, b):
        res = [[0 for j in range(self.n)] for i in range(self.m)]
        for i in range(0, self.m):
            for j in range(0, self.n):
                res[i][j] = self.a[i][j] + b.a[i][j]
        return res

    def tru(self, b):
        res = [[0 for j in range(self.n)] for i in range(self.m)]
        for i in range(0, self.m):
            for j in range(0, self.n):
                res[i][j] = self.a[i][j] - b.a[i][j]
        return res

    def mul(self, b):
        res = [[0 for j in range(self.m)] for i in range(b.n)]
        for i in range(0, self.m):
            for j in range(0, b.n):
                tmp = 0
                for k in range(0, self.n):
                    tmp += self.a[i][k]*b.a[k][j]
                res[i][j] = tmp

a = Matrix(2, 2,[[1, 2], [2, 3]])
b = Matrix(2, 2,[[1, 2], [2, 3]])
print(a.cong(b))
print(a.mul(b))