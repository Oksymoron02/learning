favorite_languages = {
    'janek': ['python', 'ruby'],
    'sara': ['c'],
    'edward': ['ruby', 'go'],
    'paweł': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print("\n Ulubione języki programowania użytkownika " + name.title() +
          " to:")
    for language in languages:
        print("\t" + language.title())