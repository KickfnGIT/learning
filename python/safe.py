# wait.py
import time
import os
import keyboard

def sleep(seconds):
    elapsed = 0
    while elapsed < seconds:
        if keyboard.is_pressed('q'):
            print("exiting")
            time.sleep(0.1)
            os._exit(0)
        time.sleep(0.1)
        elapsed += 0.1