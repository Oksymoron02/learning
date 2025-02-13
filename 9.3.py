class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def describe_user(self):
        print(f"Imię: {self.first_name} \nNazwisko: {self.last_name} \nWiek: {self.age}")

    def greet_user(self):
        print(f"Witaj, {self.first_name}!")

me = User(input("Podaj imię: "), input("Podaj nazwisko: "), input("Podaj wiek: "))
me.describe_user()
print()
me.greet_user()
