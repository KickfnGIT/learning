import os
import keyboard

i = 1
final = i
while i != 10 and not keyboard.is_pressed("e"):
    i += 2
    final =  str(final) + ", " + str(i)
    os.system("cls")
    print(final)