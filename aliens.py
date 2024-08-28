#Utworzenie pustej listy przeznaczonej do przechowywania obcych.
aliens = []

#Utworzenie 30 zielonych obcych.
for alien_number in range(30):
    new_alien = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'zielony':
        alien['color'] = 'żółty'
        alien['speed'] = 'średnio'
        alien['points'] = 10
    elif alien['color'] == 'żółty':
        alien['color'] = 'czerwony'
        alien['speed'] = 'szybko'
        alien['points'] = 15

#Wyświetlenie pierwszych pięciu obcych.
for alien in aliens[:5]:
    print(alien)
print("...")

#Wyświetlenie całkowitej liczby utworzonych obcych.
#print("Całkowita liczba obcych: " + str(len(aliens)))