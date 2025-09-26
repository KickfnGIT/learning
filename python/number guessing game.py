import random

guess = 101
random_number = random.randint(0,100)

while int(guess) != random_number:
    guess = input("Guess the number between 0 and 100: ").strip()
    while guess.isdigit() ==False or 1 < int(guess) > 100:
        print("Invalid choice!")
        guess = input("Guess the number between 0 and 100: ").strip()
    if float(random_number) > float(guess):
        print("Too low!")
    elif float(random_number) < float(guess): print("Too high!")
print(f"You guess it correctly, the number was {random_number}!")

