prompt = "Jeżeli mógłbyś odwiedzić jedno dowolne miejsce na świecie, gdzie byś pojechał? "
ankieta = {}

flag = True

while flag:
    name = input('Jak masz na imię? ')
    response = input(prompt)

    ankieta[name] = response

    repeat = input("Czy ktokolwiek chciałby jeszcze wziąć udział w ankiecie? ")
    if repeat == 'nie':
        flag = False

print("\n--- Wyniki ankiety ---")
for name, response in ankieta.items():
    print(f"{name.title()} chciałby pojechać {response.title()}.")