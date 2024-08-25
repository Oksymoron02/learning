avalible_toppings = ('pieczarki', 'oliwki', 'boczek', 'pepperoni', 'ananas', 'podwójny ser')

requested_toppings = ['pieczarki', 'frytki', 'podwójny ser']

for requested_topping in requested_toppings:
    if requested_topping in avalible_toppings:
        print(f"Dodaję " + requested_topping + ".")
    else:
        print(f"Przepraszamy, ale obecnie nie mamy dodatku " + requested_topping + '.')

print(f"\nTwoja pizza jest już gotowa!")