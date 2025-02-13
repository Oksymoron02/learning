from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['janek'] = 'python'
favorite_languages['sara'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['paweł'] = 'python'

for name, languages in favorite_languages.items():
    print(f"Ulubiony język programowania użytkownika {name.title()} to {languages.title()}.")