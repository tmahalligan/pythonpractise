name = input('What is your name? ')

if len(name) < 3:
    print("Name must be greater than 3 letters")
elif len(name) > 50:
    print("Name must be less than 50 letters")
else:
    print(f"Name is {name}")
