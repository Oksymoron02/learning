users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'maria',
        'last': 'skłodowska-curie',
        'location': 'paryż',
    },
}

for username, user_info in users.items():
    print('\nNazwa użytkownika: ' + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tImię i nazwisko: " + full_name.title())
    print("\tMiejscowość: " + location.title())