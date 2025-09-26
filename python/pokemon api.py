import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("Invalid Pokemon")


pokemon123 = input("What pokemon do you want to know about? ").strip().lower()
pinfo = get_pokemon_info(pokemon123)
if pinfo:
    print(f"Name: {pinfo["name"].capitalize()}")
    print(f"Type: {pinfo['types'][0]['type']['name']}")
    print(f"Id: {pinfo["id"]}")
    print(f"Height: {pinfo["height"]/10} Meters")
    print(f"Weight: {pinfo["weight"]/10} Kg")