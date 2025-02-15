filename = 'imiona.txt'

with open(filename, 'w') as names:
    name = input("Podaj swoje imię: ")
    names.write(name.title())