def greet_users(names):
    for name in names:
        print(f"Witaj, {name.title()}!")

usernames = ['halina', 'tymek', 'marzena']
greet_users(usernames)