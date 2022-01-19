class User:
    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts

    def description_user(self):
        print(f"Name: {self.first_name} \nLast: {self.last_name}")

    def welcome_user(self):
        print(f"Welcome {self.last_name}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User("Nguyen", "A", 2)

user.reset_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
