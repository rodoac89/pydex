from __future__ import print_function
from PIL import Image
from dex import get_pokemon_data, get_pokemon_learnset, get_move
import numpy as np
import sys, os

def check_pokedex():
    print('Testing integrity data, please wait...')
    data = []
    for pokemon in get_pokemon_data().keys():
        learnset = get_pokemon_learnset(str(pokemon))
        if learnset is not None:
            for move in learnset:
                try:
                    get_move(move)['name']
                except:
                    if move not in data:
                        data.append(move)
    print('These attack are not in dex: ')
    print(data)

# Args
argumentos = sys.argv
if 'check' in argumentos:
    check_pokedex()
    exit()


#Asscinator setup
chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
f = ''
SC = float(0.15)
GCF = float(1) 
WCF = 7.0/4.0

print ("Bienvenido")
name_pokemon = ""


pokedex_on = True
while(pokedex_on):
    name_pokemon = input("Ingrese el nombre del Pokémon: ")
    name_pokemon = name_pokemon.lower()
    os.system('clear')
    pokemon = get_pokemon_data(name_pokemon)

    if pokemon is not None:
        # Integracion de asciinator para mostrar imagen ascii del pokemon
        f = 'pokemon_images/'+ '{:04d}'.format(pokemon['num'])+'.png'
        img_pokemon = Image.open(f)
        S = (int(img_pokemon.size[0]*SC*WCF), int(img_pokemon.size[1]*SC))
        img_pokemon = np.sum( np.asarray(img_pokemon.resize(S), dtype="float"), axis=2)
        img_pokemon -= img_pokemon.min()
        img_pokemon = (1.0 - img_pokemon/img_pokemon.max())**GCF*(chars.size-1)

        print( "\n".join(("".join(r) for r in chars[img_pokemon.astype(int)])))
        print()

        # Muestra los datos principales del pokemon
        print ("Numero del Pokémon: ", pokemon['num'])
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
        #for move in get_pokemon_learnset(name_pokemon):

            #print('  - ', str(get_move(move)['name']))
    else:
        print("Pokemon no encontrado :(")

    

