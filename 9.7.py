from user_class import User

class Privileges():

    def __init__(self, *privileges):
        self.privileges = []
        self.privileges = privileges

    def show_privileges(self):
        print(f"Oto lista dostępnych przywilejów: ")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(User):

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges('może dodać post', 'może usunąć post', 'może zbanować użytkownika')


me = Admin('Dominik', 'Kowalczyk', 22)
me.privileges.show_privileges()