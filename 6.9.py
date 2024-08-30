favorite_places = {
    'mehashin': ['pizzeria', 'komputer', 'auszfic'],
    'franulitta': ['siłownia', 'dom', 'kino'],
    'oksy': ['łóżko', 'fotel', 'chata'],
}

for name, places in favorite_places.items():
    print(name.title() + ":")
    for place in places:
        print("\t" + place.title())