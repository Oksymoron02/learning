number = input("Podaj liczbę, aby dowiedzieć się, czy jest parzysta czy nieparzysta: ")
number = int(number)

if number % 2 == 0:
    print(f"\nLiczba {str(number)} jest parzysta.")
else:
    print(f"\nLiczba {str(number)} jest nieparzysta.")