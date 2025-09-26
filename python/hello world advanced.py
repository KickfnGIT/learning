import string
import time

password = r"Hello World"
list = list(string.printable)
final_text = ""

for char in password:
    item = 0
    letter = list[item]
    while not letter == char:
        print(final_text + letter)
        item += 1
        letter = list[item]
        time.sleep(0.02)

    final_text = final_text + letter

print(final_text)
