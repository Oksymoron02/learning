import json

filename = 'username.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("Jak masz na imię? ")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("Twoje imię zostało zapisane i bedzie używane później, " + username + "!")
else:
    print(f"Witamy ponownie, {username}!")