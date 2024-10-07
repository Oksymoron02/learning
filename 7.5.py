prompt = "Podaj swój wiek: "
age = ""

while True:
    age = input(prompt)
    if int(age) == 'koniec':
        break
    elif int(age) < 3:
        print('Bilet darmowy')
    elif int(age) < 12:
        print('Cena biletu to 10 zł.')
    else:
        print('Cena biletu to 15 zł.')