filename = 'learning_python.txt'

with open(filename, 'r', encoding='utf-8') as file_name:
    zawartość = file_name.read()
    print(zawartość.replace('Pythonie', "C"))

print()

with open(filename, 'r', encoding='utf-8') as lines:
    for line in lines:
        print(line.replace('Pythonie', "C").strip())

print()

with open(filename, 'r', encoding='utf-8') as file:
    linie = file.readlines()

for linia in linie:
    print(linia.replace('Pythonie', "C"))