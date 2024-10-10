sandwich_order = ['z pastrami', 'z kurczakiem', 'z pastrami', 'z pomidorem', 'z sałatą', 'z pastrami', 'z szynką']

finished_sandwiches = []

print("Przepraszamy, niestety pastrami się skończyło.")

while sandwich_order:
    sandwich_done = sandwich_order.pop()
    if sandwich_done == 'z pastrami':
        del(sandwich_done)
        continue
    print(f"Przygotowano kanapkę {sandwich_done}.")
    finished_sandwiches.append(sandwich_done)

print('\nLista zrobionych kanapek: ')
print(finished_sandwiches)