franek = {
    'type': 'cat',
    'color': 'black',
    'name': 'franek',
}

gangsterek = {
    'type': 'cat',
    'color': 'black',
    'name': 'gangsterek',
}

jadzia = {
    'type': 'cat',
    'color': 'white',
    'name': 'jadwiga',
}

puma = {
    'type': 'cat',
    'color': 'black',
    'name': 'puma',
}

pets = [
    ('franek', franek),
    ('gangsterek', gangsterek),
    ('jadzia', jadzia),
    ('puma', puma),]

for name, pet in pets:
    print(f"Name: {name}.")
    print(f"Informacje: {pet}.")
    print()