how_many = input("Na ile osób chcesz zarezerwować stolik? ")
how_many = int(how_many)

if how_many > 8:
    print("Niestety, trzeba będzie poczekać na wolny stolik.")
else:
    print("Stolik jest gotowy!")