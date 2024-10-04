number = input("Proszę podaj liczbę, aby sprawdzić czy jest wielokrotnością liczby 10: ")
number = int(number)

if number % 10 == 0:
    print(f"Liczba {number} jest wielokrotnością liczby 10.")
else:
    print(f"Liczba {number} nie jest wielokrotnością liczby 10.")