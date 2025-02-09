def make_album(disc, artist, songs = ""):
        if songs != "":
            album = {"płyta": disc, "artysta": artist, "utwory": songs}
            return album
        else:
            album = {"płyta": disc, "artysta": artist}
            return album

ready = True

while ready:
    print("Aby zakończyć program, wpisz 'XXX'")
    disc = input("Podaj nazwę płyty: ")
    if disc == 'XXX':
        break
    artist = input("Podaj nazwę artysty: ")
    if artist == "XXX":
        break
    songs = input("Podaj liczbę utworów: ")
    if songs == "XXX":
        break
    print()
    print(make_album(disc, artist, songs))
    print()