def greet_users(names):
    for name in names:
        msg = "Witaj, " + name.title() + "!"
        print(msg)

usernames = ['halina', 'tymek', 'marzena']
greet_users(usernames)