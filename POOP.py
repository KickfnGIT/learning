from POOPclass import car
import time


car1 = car("bugatti chiron", 2025, "blue", True)
car2 = car("bentley", 2022, "black", False)
car3 = car("corvette", 2013, "white", False)

Cars = [car1, car2, car3]

for i in Cars:
    i.describle()
    time.sleep(2)
    i.drive()
    time.sleep(6)
    i.stop()
    time.sleep(3)
    print("")

