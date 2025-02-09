def make_pizza(size, *toppings):
    print(f"\nPrzygotowuję pizzę o wielkości {str(size)} cm, z następującymi dodatkami: ")
    for topping in toppings:
        print(f"- {topping}")