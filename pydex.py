"""
PyDex Beta 0.1
PyDex nace producto del ocio que tuve hace unos años y las ganas que tenía por desarrollar mi propia pokedex
PyDex permite hacer scrapping básico a pokemon.com para obtener las imagenes de los pokemon actuales
y así poder mostrarlos por consola en ascii.
Este script aún está en desarrollo, si quieren contribuir pueden hacerlo sin problemas
rodoaravena
"""
from dex import check_dex, get_data, get_learnset, get_move, print_asciiart
from pokescrapping import scrapping
from optparse import OptionParser

import sys, os

def main(name_key):
    name_key = name_key.lower().strip()
    os.system('clear')
    dex_data = get_data(name_key)

    if dex_data is not None:
        # Integracion de ascii art para mostrar imagen ascii del pokémon
        print('Imagen del Pokémon: \n')
        print_asciiart(dex_data['num'])

        # Muestra los datos principales del pokémon
        print ("\nNumero del Pokémon: ", dex_data['num'])
        print ("Sus tipos son: ")
        for mon_type in dex_data["types"]:
            print("  - ",mon_type)
        if "genderRatio" in dex_data:
            print("Posibilidad de aparición según género: ")
            print("  - Macho = ", (dex_data["genderRatio"]["M"] * 100), "%")
            print("  - Hembra = ",(dex_data["genderRatio"]["F"] * 100), "%")
        elif "gender" in dex_data:
            print("Género único:")
            if dex_data["gender"] == "N":
                print("  - Neutral")

            elif dex_data["gender"] == "F":
                print("  - Hembra")

            elif dex_data["gender"] == "M":
                print("  - Macho")
        
        if "evos" in dex_data:
            print("Siguiente evolución: ")
            for evo in dex_data["evos"]:
                pokemon_evo = get_data(evo)
                print("  - ", pokemon_evo["species"])   

        if "otherFormes" in dex_data:
            print("Otras formas del Pokémon: ")
            for other_form in dex_data["otherFormes"]:
                form_pokemon = get_data(other_form)                
                new_name_key = str(form_pokemon["species"]).split('-')
                print ("  - ", new_name_key[1], new_name_key[0])
        print('Movimientos que puede aprender el pokémon: ')
        if len(get_learnset(name_key))>0: 
            for move in get_learnset(name_key):
                print('  - ', str(get_move(move)['name']))
        else:
            print("No se logró obtener los movimietos")
    else:
        print("Pokémon no encontrado :(")

# Argumentos para comprobar integridad de los datos y descargar previamente las imagenes

def process_arguments(option, opt_str, value, parser, *args, **kwargs):

    if opt_str in ['-p', '--pokemon']:
        main(value)
    if opt_str in ['-s', '--scrap']:
        scrapping()
    if opt_str in ['-c', '--check']:
        check_dex()
    exit()

usage = "Uso: %prog [options] \nSi no se agrega algún argumento encenderá la PyDex "
parser = OptionParser(usage=usage)
parser.add_option('-p', '--pokemon',
                    action="callback", dest="poke",
                    help="Consulta directamente el pokemon deseado sin encender PyDex", callback=process_arguments, type=str)
parser.add_option("-s", "--scrap",
                  action="callback", callback=process_arguments,
                  help="Realiza scrapping a pokemon.com (opcional)")
parser.add_option("-c", "--check",
                  action="callback", 
                  help="Revisa la integridad de los datos (opcional)", callback=process_arguments)

(options, args) = parser.parse_args()


print ("...::: PyDex :::...")
print ("Binvenido a pydex, para iniciar la búsqueda, ingrese el nombre de un pokémon")
print ("Nota: Esta herramienta aún está en desarrollo, no soporta espacios o simbolos, si desea buscar una forma regional o especial debe ingresar el nombre del pokemon junto con la forma que busca, ej: si busca Mega Absol debe ingresar 'absolmega'")
name_key = ""


dex_on = True
while(dex_on):    
    main(input("Ingrese el nombre del Pokémon: "))

    

