guests = ['Kuba', 'Dawid', 'Kacper']

print(f"{guests[0]} zapraszam Cię na obiad!")
print(f"{guests[1]} zapraszam Cię na obiad!")
print(f"{guests[2]} zapraszam Cię na obiad!")

apsent = guests.pop()
print(f"\nNiestety {apsent} nie może przyjść.")
guests.append('Zuzia')
print(f"{guests[0]} zapraszam Cię na obiad!")
print(f"{guests[1]} zapraszam Cię na obiad!")
print(f"{guests[2]} zapraszam Cię na obiad!")