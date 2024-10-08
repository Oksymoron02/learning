sandwich_order = ['z kurczakiem', 'z pomidorem', 'z sałatą', 'z szynką']

finished_sandwiches = []

while sandwich_order:
    sandwich_done = sandwich_order.pop()
    print(f"Przygotowano kanapkę {sandwich_done}.")
    finished_sandwiches.append(sandwich_done)

print('\nLista zrobionych kanapek: ')
print(finished_sandwiches)