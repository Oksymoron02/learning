pizzas = ['pepperoni', 'salami', 'capriczoza']
friend_pizzas = pizzas[:]

pizzas.append('rukola')
friend_pizzas.append('margeritta')

print("Moje ulubione rodzaje pizzy to: ")
for pizza in pizzas:
    print(pizza)

print("Ulubione rodzaje pizzy mojego przyjaciela to: ")
for fpizz in friend_pizzas:
    print(fpizz)