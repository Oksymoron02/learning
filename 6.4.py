glosary = {
    'string': 'Służy do określania wartości łańcuchowej dla kategorii lub komórki w tabeli przestawnej. Argument jest wartością łańcuchową. Można również przekazać wartość liczbową, która zostanie przekształcona w łańcuch.',
    'integer': 'Typ int (ang. integer) reprezentuje liczby całkowite dodatnie lub ujemne bez kropki dziesiętnej. Nie mają one limitu dopuszczalnych wartości tzn. mogą być tak długie, jak tylko chcesz.',
    'list': 'W Pythonie używamy do tego listy (ang. list), która reprezentuje zbiór wartości. Wartości mają na niej swoją kolejność oraz mogą się powtarzać. Listy mogą się także zmieniać, w przeciwieństwie do tupli, o których pomówimy później.',
    'dictionary': 'W Pythonie słownik (dictionary) jest dynamiczną strukturą danych, która przechowuje pary klucz-wartość. Słownik jest jednym z wbudowanych typów danych i jest bardzo użyteczny w przypadku przechowywania i manipulowania danymi, w których klucze odnoszą się do odpowiadających im wartości.',
    'tuple': 'Krotka1 jest sekwencją wartości, podobnie jak lista. Wartości zapisane w krotce mogą być dowolnego typu i są indeksowane liczbami całkowitymi. Ważną różnicą jest to, że krotki są niezmienne. Krotki są również porównywalne i haszowalne, więc możemy sortować ich listy i używać krotek jako kluczy w słownikach.'
}

for key, value in glosary.items():
    print(key)
    print(value)