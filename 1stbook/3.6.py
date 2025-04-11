guests = ['Kuba', 'Dawid', 'Kacper']

print(f"{guests[0].title()} zapraszam Cię na obiad!")
print(f"{guests[1].title()} zapraszam Cię na obiad!")
print(f"{guests[2].title()} zapraszam Cię na obiad!")

apsent = guests.pop()
print(f"\nNiestety {apsent} nie może przyjść.")
guests.append('Zuzia')

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