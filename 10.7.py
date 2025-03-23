while True:
    num_1 = input("Podaj pierwszą liczbę: ")
    num_2 = input("Podaj drugą liczbę: ")

    try:
        num_3 = int(num_1) + int(num_2)
        print(num_3)
    except TypeError:
        print("Podaj LICZBY!!!")
    continue