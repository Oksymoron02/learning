guests = ['Zuzia', 'Dawid', 'Kacper']

print(f"{guests[0].title()} zapraszam Cię na obiad!")
print(f"{guests[1].title()} zapraszam Cię na obiad!")
print(f"{guests[2].title()} zapraszam Cię na obiad!")

apsent = guests.pop()
print(f"\nNiestety {apsent} nie może przyjść.")
guests.append('Kuba')

print(f"\n{guests[0].title()} zapraszam Cię na obiad!")
print(f"{guests[1].title()} zapraszam Cię na obiad!")
print(f"{guests[2].title()} zapraszam Cię na obiad!")

print(f"\nZnalazłem większy stół więc będzie więcej gości.")

guests.insert(0, 'Andrew')
guests.insert(2, 'Iman')
guests.append('David')

print(f"\n{guests[0].title()} zapraszam Cię na obiad!")
print(f"{guests[1].title()} zapraszam Cię na obiad!")
print(f"{guests[2].title()} zapraszam Cię na obiad!")
print(f"{guests[3].title()} zapraszam Cię na obiad!")
print(f"{guests[4].title()} zapraszam Cię na obiad!")
print(f"{guests[5].title()} zapraszam Cię na obiad!")

print(f"\nNiestety nowy stół nie zostanie dostarczony na czas dlatego mogę zaprosić tylko dwie osoby")

popped_guests = guests.pop()
print(f"\nPrzepraszam, jednak nie dam rady Cię przyjąć {popped_guests}.")
popped_guests = guests.pop()
print(f"\nPrzepraszam, jednak nie dam rady Cię przyjąć {popped_guests}.")
popped_guests = guests.pop()
print(f"\nPrzepraszam, jednak nie dam rady Cię przyjąć {popped_guests}.")
popped_guests = guests.pop()
print(f"\nPrzepraszam, jednak nie dam rady Cię przyjąć {popped_guests}.")

print(f"\n{guests[0].title()} zapraszam Cię na obiad!")
print(f"{guests[1].title()} zapraszam Cię na obiad!")

del guests[0]
del guests[0]

print(guests)