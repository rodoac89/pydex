from PIL import Image
import numpy 
import json

def load_db(dex_db=None):
    try:
        db_file = open('dexdb.json')
        data = json.load(db_file)
        if dex_db is not None:
            return data[dex_db]
        else:
            return data
    except:
        return None

def print_asciiart_pokemon(num_pokemon = 0):
    '''
    Imprime en pantalla el asciiart del pokemon consultado
    '''
    # Configuración del asciiart
    chars = numpy.asarray(list(' .,:;irsXA253hMHGS#9B&@'))
    f = ''
    SC = float(0.15)
    GCF = float(1) 
    WCF = 7.0/4.0

    # Impresión del pokémon en la consola
    try:
        f = 'pokemon_images/'+ '{:04d}'.format(num_pokemon)+'.png'
        img_pokemon = Image.open(f)
        S = (int(img_pokemon.size[0]*SC*WCF), int(img_pokemon.size[1]*SC))
        img_pokemon = numpy.sum( numpy.asarray(img_pokemon.resize(S), dtype="float"), axis=2)
        img_pokemon -= img_pokemon.min()
        img_pokemon = (1.0 - img_pokemon/img_pokemon.max())**GCF*(chars.size-1)

        print( "\n".join(("".join(r) for r in chars[img_pokemon.astype(int)])))
        print()
    except:
        print('No se logró encontrar la imagen para el pokémon seleccionado')

def get_pokemon_data(pokemon=None):
    pokemon_data = load_db('pokemon')
    if pokemon_data is not None:
        if pokemon is None:
            return pokemon_data
        if pokemon in pokemon_data:
            return pokemon_data[pokemon]
    else:
        print("Base de datos no encontrada")
        return None

def get_move(move):
    move_list = load_db('move_list')
    return move_list[move] if move in move_list else None

def get_learnset(pokemon):
    learnset = load_db('learnset')
    if learnset is not None:
        return learnset[pokemon]
    else:
        print("Base de datos no encontrada")

def check_pokedex():
    print('Comprobando integridad de los datos, por favor espere...')
    if load_db() is not None:
        data = []
        ok_data = []
        count_error = 0
        count_ok = 0
        for pokemon in get_pokemon_data().keys():
            learnset = get_learnset(str(pokemon))
            if learnset is not None:
                for move in learnset:
                    try:
                        ok_data.append(get_move(move)['name'])
                        count_ok += 1
                    except:
                        if move not in data:
                            data.append(move)
                            count_error+=1
        if count_error > 0:
            print(data)
            print('We found {} errors.\nThese attack are not in dex: '.format(count_error))
        else:
            print('No error found')
        print('Data ok ', count_ok)
    else:
        print("Base de datos no encontrada")
