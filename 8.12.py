def skladniki(*skladniks):
    print("\nOto zamówione przez Ciebie składniki: ")
    for skladnik in skladniks:
        print("- " + skladnik)

skladniki('pepperoni', 'cebula', 'ser')