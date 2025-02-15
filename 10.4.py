filename = 'guest_book.txt'

with open(filename, 'a', encoding='utf-8') as lista_gosci:
    while True:
        name = input("Podaj swoje imię: ")
        if name == 'q':
            break
        else:
            print(f"Witaj, {name.title()}!")
            lista_gosci.write(name.title() + "\n")