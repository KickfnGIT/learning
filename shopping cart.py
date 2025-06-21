import os
cart = []
file_path = os.path.expandvars("%USERPROFILE%\\Downloads\\cart.txt")

while True:
    will_continue = input("Would you like to add anything to your cart? (y/m/n): ").strip().lower()
    if will_continue in ("y", "n", "m"):
        if will_continue == "y":
            fruit = input("What would you like to add to your cart? ").strip().title()
            print("")
            cart.append(fruit)
        if will_continue == "m":
            items = input("How many items would you like to add to your cart? ").strip()
            if items.isdigit():
                for i in range(int(items)):
                    fruit = input("What would you like to add to your cart? ").strip().title()
                    print("")
                    cart.append(fruit)
            else:
                print("Invalid Input")
                print("")
        if will_continue == "n":
            break
    else:
        print("Invalid Input")
        print("")
print("")
with open(file_path, 'w') as file:
    for item in cart:
        file.write(item + '\n')
print(f"List is located in {file_path}")