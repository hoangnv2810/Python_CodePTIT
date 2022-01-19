import math

class Prime():
    def __init__(self):
        self.x = 0

    def is_prime(self, x):
        self.x = x
        if self.x < 2:
            return False
        for i in range(2, int(math.sqrt(self.x))+1):
            if self.x%i == 0:
                return False
        return True

    def next_prime(self, x):
        self.x = x
        a = [b for b in range(self.x+1, 2*self.x) if self.is_prime(b)]
        return min(a)

class CheckNumber(Prime):
    def __init__(self, x):
        self.x = x

    def parity_check(self):
        if self.x % 2 == 0:
            print("CHAN")
        else:
            print("LE")

    # def is_prime(self, x):




num = Prime()
print(num.is_prime(7))
print(num.next_prime(7))