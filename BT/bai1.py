class Number():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def input_info(self):
        print(f"Number 1: {self.number1} Number 2: {self.number2}")

    def addition(self):
        return(self.number1 + self.number2)

    def subtract(self):
        return (self.number1 - self.number2)

    def multi(self):
        return (self.number1 * self.number2)

    def division(self):
        return (self.number1 / self.number2)


a = Number(1, 2)
a.input_info()
print(a.addition())
print(a.subtract())
print(a.multi())
print(a.division())
