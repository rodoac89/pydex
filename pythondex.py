from __future__ import print_function
import json
import sys; 
from PIL import Image; 
import numpy as np
import os


pokedex_on = True
poke_data = {}
with open('dex.json') as f:
    poke_data = json.load(f)

chars = np.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
f = ''
SC = float(0.15)
GCF = float(1) 
WCF = 7.0/4.0

print ("Bienvenido")
name_pokemon = ""
while(pokedex_on):
    name_pokemon = str(input("Ingrese el nombre del pokemon: "))
    name_pokemon = name_pokemon.lower()
    os.system('clear')
    if name_pokemon in poke_data:
        pokemon = poke_data[name_pokemon]

        # Integracion de asciinator
        # para mostrar imagen ascii del pokemon
        f = 'pokemon_images/'+ '{:04d}'.format(pokemon['num'])+'.png'
        img_pokemon = Image.open(f)
        S = (int(img_pokemon.size[0]*SC*WCF), int(img_pokemon.size[1]*SC))
        img_pokemon = np.sum( np.asarray(img_pokemon.resize(S), dtype="float"), axis=2)
        img_pokemon -= img_pokemon.min()
        img_pokemon = (1.0 - img_pokemon/img_pokemon.max())**GCF*(chars.size-1)

        print( "\n".join(("".join(r) for r in chars[img_pokemon.astype(int)])))
        print()

        # Muestra los datos principales del pokemon
        print ("Numero del pokemon: ", pokemon['num'])
        print ("Sus tipos son: ")
        for t in pokemon["types"]:
            print("  - ",t)
        if "genderRatio" in pokemon:
            print("Posibilidad de aparicion segun genero: ")
            print("  - Macho = ", (pokemon["genderRatio"]["M"] * 100), "%")
            print("  - Hembra = ",(pokemon["genderRatio"]["F"] * 100), "%")
        elif "gender" in pokemon:
            print("Genero unico:")
            if pokemon["gender"] == "N":
                print("  - Neutral")

            elif pokemon["gender"] == "F":
                print("  - Hembra")

            elif pokemon["gender"] == "M":
                print("  - Macho")
        
        if "evos" in pokemon:
            print("Siguiente evolucion: ")
            for evo in pokemon["evos"]:
                pokemon_evo = poke_data[evo]
                print("  - ", pokemon_evo["species"])

               

        if "otherFormes" in pokemon:
            print("Otras formas del pokemon: ")
            for other_form in pokemon["otherFormes"]:
                form_pokemon = poke_data[other_form]                
                new_name_pokemon = str(form_pokemon["species"]).split('-')
                print ("  - ", new_name_pokemon[1], new_name_pokemon[0])
    else:
        print("Pokemon no encontrado :(")

    

