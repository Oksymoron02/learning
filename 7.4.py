prompt = "\nPodaj dodatki do pizzy: "
addon = ""

while True:
    addon = input(prompt)
    if addon == 'koniec':
        break
    else:
        print(f"\nDodaję {addon.title()} do pizzy!")

