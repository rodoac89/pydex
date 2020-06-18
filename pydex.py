
from pokedex import check_pokedex, get_pokemon_data, get_learnset, get_move, print_asciiart_pokemon
from pokemon_scrapping import download_pokemon_photos, check_folder

import sys, os

# Argumentos para comprobar integridad de los datos y descargar previamente las imagenes
arguments = sys.argv
if 'check' in arguments:
    check_pokedex()
    exit()
if 'scrap' in arguments:
    download_pokemon_photos()
    exit()


print ("...::: PyDex :::...")
print ("Binvenido a pydex, para iniciar la búsqueda, ingrese el nombre de un pokémon")
print ("Nota: Esta herramienta aún está en desarrollo, no soporta espacios o simbolos, si desea buscar una forma regional o especial debe ingresar el nombre del pokemon junto con la forma que busca, ej: si busca Mega Absol debe ingresar 'absolmega'")
name_pokemon = ""


pokedex_on = True
while(pokedex_on):
    name_pokemon = input("Ingrese el nombre del Pokémon: ")
    name_pokemon = name_pokemon.lower().strip()
    os.system('clear')
    pokemon = get_pokemon_data(name_pokemon)

    if pokemon is not None:
        # Integracion de ascii art para mostrar imagen ascii del pokemon
        print('Imagen del Pokémon: \n')
        if check_folder():
            print_asciiart_pokemon(pokemon['num'])

        # Muestra los datos principales del pokemon
        print ("\nNumero del Pokémon: ", pokemon['num'])
        print ("Sus tipos son: ")
        for pokemon_type in pokemon["types"]:
            print("  - ",pokemon_type)
        if "genderRatio" in pokemon:
            print("Posibilidad de aparición según género: ")
            print("  - Macho = ", (pokemon["genderRatio"]["M"] * 100), "%")
            print("  - Hembra = ",(pokemon["genderRatio"]["F"] * 100), "%")
        elif "gender" in pokemon:
            print("Género único:")
            if pokemon["gender"] == "N":
                print("  - Neutral")

            elif pokemon["gender"] == "F":
                print("  - Hembra")

            elif pokemon["gender"] == "M":
                print("  - Macho")
        
        if "evos" in pokemon:
            print("Siguiente evolución: ")
            for evo in pokemon["evos"]:
                pokemon_evo = get_pokemon_data(evo)
                print("  - ", pokemon_evo["species"])

               

        if "otherFormes" in pokemon:
            print("Otras formas del Pokémon: ")
            for other_form in pokemon["otherFormes"]:
                form_pokemon = get_pokemon_data(other_form)                
                new_name_pokemon = str(form_pokemon["species"]).split('-')
                print ("  - ", new_name_pokemon[1], new_name_pokemon[0])
        print('Movimientos que puede aprender el pokémon: ')
        for move in get_learnset(name_pokemon):

            print('  - ', str(get_move(move)['name']))
    else:
        print("Pokémon no encontrado :(")

    

