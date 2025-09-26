username = input("Enter a username (no spaces or digits): ")
while not username.isalpha() or len(username) >= 12:
    print("invalid username")
    username = input("Please enter a valid username: ")
print("You have created your username")
print(username)