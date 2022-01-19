class Person:
    def __init__(self, name, gender, dob):
        self.name = name
        self.gender = gender
        self.dob = dob

    def description_person(self):
        print(f"{self.name} {self.gender} {self.dob}")


class Student(Person):
    def __init__(self, name, gender, dob, id, gpa, email):
        super().__init__(name, gender, dob)
        self.id = id
        self.gpa = gpa
        self.email = email

    def description_student(self):
        print(f"{self.id} {self.name} {self.gender} {self.gpa} {self.email}")

    def check_scholarship(self):
        if self.gpa >= 3.2:
            print("Yes")
        else:
            print("No")


