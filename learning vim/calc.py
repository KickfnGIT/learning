import locale
answer = "You only entered 1 number so no answer bozo"
# 67 testing git

while True:
    number = "540342.42342424234324"
    number2 = "540342.42342424234324"
    operator = "540342.42342424234324"
    while number == "540342.42342424234324":
            number = input("Enter a number: ")
            try:
                number = float(number)
            except ValueError:
                number = "540342.42342424234324"
                print("please enter a valid number")
    while operator not in "+-/*^":
        operator = input("what operation would you like to do? (+-/*^): ")
    while number2 == "540342.42342424234324":
            number2 = input("Enter another number: ")
            try:
                number2 = float(number2)
            except ValueError:
                number2 = "540342.42342424234324"
                print("please enter a valid number")
    if operator == "+":
        answer = number + number2
    if operator == "-":
        answer = number - number2
    if operator == "/":
        while number2 == 0 or number2 == "540342.42342424234324":
            if number2 == 0:
                print("Cannot divide by 0")
            number2 = input("Enter another number: ")
            try:
                number2 = float(number2)
            except ValueError:
                number2 = "540342.42342424234324"
                print("please enter a valid number")
        answer = number / number2
    if operator == "*":
        answer = number * number2
    if operator == "^":
        answer = number ** number2
    locale.setlocale(locale.LC_ALL, '')
    decimal_places = 0
    if "e-" in str(answer):
        new_answer = str(answer).split("e-")
        decimal_places = (int(new_answer[1]) + len(new_answer[0]))-2
    elif "." in str(answer) and not "e+" in str(answer):
        new_answer = str(answer).split(".")
        if new_answer[1] != "0":
            decimal_places = len(new_answer[1])
    print(locale.format_string(f'%.{decimal_places}f', answer, grouping=True))
