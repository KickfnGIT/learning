numbers = input("How many even numbers do you want to print? ")

while numbers.isdigit() is False:
    numbers = input("Invalid Input. Please enter a valid number: ")

for i in range(int(numbers)+3):
    if i % 2 == 0 and i not in [0]:
        print(i, "is an even number.")