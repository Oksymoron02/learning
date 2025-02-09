def make_pizza(size, *toppings):
    print(f"\nPrzygotowuję pizzę o wielkości {str(size)} cm, z następującymi dodatkami: ")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(40, 'pepperoni')
make_pizza(30, 'pieczarki', 'zielona papryka', 'podwójny ser')