class User():
    def __init__(self, first_name, last_name, age, login_attemps=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attemps = login_attemps
        self.login_attemps = 0
    
    def describe_user(self):
        print(f"Imię: {self.first_name} \nNazwisko: {self.last_name} \nWiek: {self.age}")

    def greet_user(self):
        print(f"Witaj, {self.first_name}!")

    def increment_login_attemps(self):
        self.login_attemps += 1

    def reset_login_attemps(self):
        self.login_attemps = 0

me = User('Dominik', 'Kowalczyk', 22)
me.describe_user()
me.increment_login_attemps()
me.increment_login_attemps()
me.increment_login_attemps()
me.increment_login_attemps()
print(me.login_attemps)
me.increment_login_attemps()
me.increment_login_attemps()
me.increment_login_attemps()
me.increment_login_attemps()
print(me.login_attemps)
me.reset_login_attemps()
print(me.login_attemps)