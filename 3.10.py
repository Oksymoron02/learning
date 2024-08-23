list = ['dom', 'rower', 'paryż', 'drzwi', 'biznes', 'ruletka', 'gry', 'czas', 'kamień', 'siano', 'czerwony', 'wagon']

list[0] = 'czarny'  #dodaje element na początek listy
list.append('zielony')  #dodaje element na koniec listy
list.insert(5, 'tysiąc')    #dodaje element na wybranym miejscu
del list[0]     #usuwa pierwszy element z listy
list.pop()      #usuwa ostatni element z listy
list.remove('siano')    #usuwa element po wartości
list.sort()     #sortuje liste alfabetycznie
list.sort(reverse=True)     #trwale sortuje liste w kojelności odwrotnej do alfabetycznej
print(sorted(list))     #sortuje liste alfabetycznie ale nie trwale
print(sorted(list, reverse=True))      #sortuje listę odwrotnie niż alfabetycznie nie trwale
list.reverse()      #odwraca listę
list.reverse()      #ponownie odwraca listę
print(len(list))       #sprawdza ile elementów zawiera lista