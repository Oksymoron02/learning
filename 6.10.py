favorite_numbers = {
    'marek': [44],
    'stjepan': [23, 56],
    'dominik': [4, 22],
    'kuba': [7],
    'darek': [67],
}

for name, numbers in favorite_numbers.items():
    print(name.title() + ": ")
    for number in numbers:
        print("\t" + str(number))