prompt = "\nPowiedz mi coś o sobie, a wyświetlę to na ekranie: "
prompt += "\nNapisz 'koniec', aby zakończyć działanie programu. "

active = True
while active:
    message = input(prompt)

    if message == 'koniec':
        active = False
    else:
        print(message)
        