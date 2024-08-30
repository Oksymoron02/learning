cities = {
    'gdańsk': {
        'country': 'poland',
        'population': 100000,
        'fact': 'big miasto',
    },
    'warszawa':{
        'country': 'poland',
        'population': 10000000,
        'fact': 'syf',
    },
    'łódź': {
        'country': 'poland',
        'population': 1000,
        'fact': 'tam śmierdzi',
    },
}

for city, data in cities.items():
    print(city.title() + ":")
    for dat, dejt in data.items():
        print("\t" + dat + ": " + str(dejt))