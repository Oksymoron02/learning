responses = {}

polling_active = True

while polling_active:
    name = input("\nJak masz na imię? ")
    response = input("Na który szczyt chciałbyś się wspiąć pewnego dnia? ")

    responses[name] = response

    repeat = input("Czy ktokolwiek iiny chce wziąć udział w ankiecie? (tak / nie) ")
    if repeat == 'nie':
        polling_active = False

print("\n--- Wyniki ankiety ---")
for name, response in responses.items():
    print(f"{name.title()} chciałby się wspiąć na {response.title()}.")