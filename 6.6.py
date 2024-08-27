favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
    }

people = ['janek', 'dominik', 'dawid', 'sara', 'kuba', 'kacper', 'paweł']

for person in people:
    if person in favorite_languages.keys():
        print(person.title() + ', dziekujemy za udział w ankiecie!')
    else:
        print(person.title() + ', weź udział w ankiecie!')