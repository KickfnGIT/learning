import pytemperature

unit = input("Farenheight or Celcius? (f/c): ").lower().strip()
while unit not in ("f", "c"):
    unit = input("Farenheight or Celcius? (f/c): ").lower().strip()
Tempreture = input("Whats the tempreture?: ").strip()
while not Tempreture.isdigit():
    Tempreture = input("Whats the tempreture?: ").strip()

if unit in ("f"):
    print(pytemperature.f2c(int(Tempreture)))
elif unit in ("c"):
    print(pytemperature.c2f(int(Tempreture)))
