alien_0 = {'x_position': 0, 'y_position': 26, 'speed': 'średnio'}
print(f"Początkowa wartość x-position: " + str(alien_0['x_position']))

#Przesunięcie obcego w prawo.
#Ustalenie odległości, jaką powinien pokonać obcy poruszający się z daną szybkością.
if alien_0['speed'] == 'wolno':
    x_increment = 1
elif alien_0['speed'] == 'średnio':
    x_increment = 2
else:
    #To musi być szybki obcy.
    x_increment = 3

#Nowe położenie to suma dotychczasowego położenia i wartości x_increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"Nowa wartość x-position: " + str(alien_0['x_position']))