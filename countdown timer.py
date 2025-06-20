import time
import math
import os

countdown = (int(input("How long do you want the countdown to be for? (seconds): ")))
flush = True
while countdown > -1:        
    countdown1 = math.floor(countdown / 3600)
    countdown2 = math.floor((countdown / 60)-(60 * countdown1))
    countdown3 = math.floor(countdown)-(3600 * countdown1)-(60 * countdown2)
    os.system("cls")
    print (f"{countdown1:02}:{countdown2:02}:{countdown3:02}") 
    countdown -= 1
    time.sleep(1)
print("Countdown Over!!!!!!!!!!")