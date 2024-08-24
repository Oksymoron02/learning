age = int(input(f"Ile masz lat? "))

if age < 2:
    print(f"Jesteś niemowlęciem.")
elif age < 13:
    print(f"Jesteś dzieckiem.")
elif age < 20:
    print(f"Jesteś nastolatkiem.")
elif age < 65:
    print(f"Jesteś dorosły.")
else:
    print(f"Jesteś seniorem.")