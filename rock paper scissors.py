import random

will_continue = "y"
ties = 0
wins = 0
loses = 0

def computer_choice():
    pick = random.randint(1,3)
    if pick == 1:
        computer_choice = "🗿"
    elif pick == 2:
        computer_choice =  "📃"
    elif pick == 3:
        computer_choice = "✂️"
    return computer_choice

def get_winner(player, computer):
    global ties, wins, loses
    if player == "s":
        if computer == "✂️":
            print("You chose ✂️")
            print("Computer chose ✂️")
            print("Tie")
            ties += 1
        if computer == "📃":
            print("You chose ✂️")
            print("Computer chose 📃")
            print("You Win!!!")
            wins += 1
        if computer == "🗿":
            print("You chose ✂️")
            print("Computer chose 🗿")
            print("You Lose :(")
            loses += 1
    if player == "p":
        if computer == "✂️":
            print("You chose 📃")
            print("Computer chose ✂️")
            print("You Lose :(")
            loses += 1
        if computer == "📃":
            print("You chose 📃")
            print("Computer chose 📃")
            print("Tie")
            ties += 1
        if computer == "🗿":
            print("You chose 📃")
            print("Computer chose 🗿")
            print("You Win!!!")
            wins += 1
    if player == "r":
        if computer == "✂️":
            print("You chose 🗿")
            print("Computer chose ✂️")
            print("You Win!!!")
            wins += 1
        if computer == "📃":
            print("You chose 🗿")
            print("Computer chose 📃")
            print("You Lose :(")
            loses += 1
        if computer == "🗿":
            print("You chose 🗿")
            print("Computer chose 🗿")
            print("Tie")
            ties += 1



while will_continue == "y":
    cc = computer_choice()
    choice = input("Rock, paper, or scissors? (r/p/s): ").strip().lower()
    while choice not in ("r", "p", "s"):
        print("Invalid Choice")
        choice = input("Rock, paper, or scissors? (r/p/s): ").strip().lower()
    get_winner(choice, cc)
    will_continue = input("Continue? (y/n): ").strip().lower()
    while will_continue not in ("y", "n"):
        print("Invalid choice")
        will_continue = input("Continue? (y/n): ").strip().lower()
    print(" ")

if will_continue == "n":
    print("Wins:", wins)
    print("Loses:", loses)
    print("Ties:", ties)




    