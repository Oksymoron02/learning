users = ['admin', 'oksymoron', 'mehashin', 'franul', 'thinker']

for user in users:
    if user == 'admin':
        print(f"Witaj, " + user.title() + "! Czy chcesz przejrzeć dzisiejszy raport?")
    else:
        print(f"Witaj, " + user.title() + "! Dziękujemy, że ponownie się zalogowałeś.")