#age = int(input())
#
#if age < 4:
#    print("Cena biletu wstepu wynosi 0 zł.")
#elif age < 18:
#    print("Cena biletu  wstępu wynosi 5 zł.")
#else:
#    print("Cena biletu wstępu wynosi 10 zł.")

age = int(input())

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print(f"Cena biletu wstępu wynosi " + str(price) + " zł.")