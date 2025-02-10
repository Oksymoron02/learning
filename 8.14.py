def auta(marka, model, **aditional):
    autka = {}
    autka['marka'] = marka
    autka['model'] = model
    for key, value in aditional.items():
        autka[key] = value
    return autka

car = auta('bmw', 'e36', nadwozie='coupe', color='arctissliber')
print(car)