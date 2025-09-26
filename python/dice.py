import random

counter = 0
roll = input("Roll the dice? (y/m/n): ").strip().lower()
rolls = [(0, 0)]

while roll != 'n':
    if roll == 'y':
        counter += 1
        Dice1 = random.randint(1, 1000000)
        Dice2 = random.randint(1, 1000000)
        print (f"({Dice1}, {Dice2})")
        print("Rolled", counter, "times")
        rolls.append((Dice1, Dice2))
        roll = input("Roll the dice? (y/m/n): ").strip().lower()
    elif roll == 'm':
        times = input("How many times do you want to roll: ").strip()
        intimes = int(times)
        while intimes != 0:
            intimes -= 1
            counter += 1
            Dice1 = random.randint(1, 1000000)
            Dice2 = random.randint(1, 1000000)
            rolls.append((Dice1, Dice2))
            print (f"({Dice1}, {Dice2})")
            print("Rolled", counter, "times")
        roll = input("Roll the dice? (y/m/n): ").strip().lower()
    else:
        print("Invalid Input")
        roll = input("Roll the dice? (y/m/n): ").strip().lower()
print(max(rolls))
print("Thanks for playing!")