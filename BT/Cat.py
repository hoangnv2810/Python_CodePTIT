class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name}")

    def roll_over(self):
        print(f"{self.name}")

my_cat = Cat("Meo", 6)
print(my_cat.name)