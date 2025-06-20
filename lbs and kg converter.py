print("1: Lbs to Kg")
print("2: Kg to Lbs")
while True:
    Conversion = input("How do you wish to convert? (1,2): ").strip()
    if Conversion == "1":
        Amount = input("How many Pounds to convert: ").strip()
        while not Amount.isdigit():
            print("Invalid Input")
            Amount = input("How many Pounds to convert: ").strip()
        print(f"{Amount} Pounds is roughly {round(float(Amount)*0.4535924, 2)} Kilograms")
        break
    elif Conversion == "2":
        Amount = input("How many Kilograms to convert: ").strip()
        while not Amount.isdigit():
            print("Invalid Input")
            Amount = input("How many Kilograms to convert: ").strip()
        print(f"{Amount} Kilograms is roughly {round(float(Amount)/0.4535924, 2)} Pounds")
        break
    else:
        print("Invalid Input") 
        