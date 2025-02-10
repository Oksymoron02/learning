def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

def make_great(magicians, better):
    while magicians:
        for magician in magicians:
            magician = magicians.pop()
            magician = "Doskonały " +  str(magician)
            better.append(magician)
        continue

magicians = ['hokus', 'pokus', 'ezekiel']
better_magicians = []

make_great(magicians[:], better_magicians)
show_magicians(magicians)
print()
show_magicians(better_magicians)