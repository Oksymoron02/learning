filename = 'cats.txt'
filename2 = "dogs.txt"

try:
    with open(filename, 'r', encoding='utf-8') as imiona:
        for i in imiona:
            print(i)
except FileNotFoundError:
    pass