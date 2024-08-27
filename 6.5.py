rivers = {
    'nil': 'egipt',
    'wisła': 'polska',
    'odra': 'polska',
}

for river, city in rivers.items():
    print(river.title() + ' przepływa przez ' + city.title() + '.')

for river in rivers.keys():
    print(river.title())

for city in rivers.values():
    print(city.title())