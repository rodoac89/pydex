'''
Este módulo permite hacer scrapping a pokemon.com para obtener las imagenes oficiales de los pokémon
'''
import cv2
import numpy as np
import urllib.request
import time
import os
import sys
import subprocess 
import logging
from pathlib import Path


FOLDER = 'pokemon_images/'
LOG_FILE = os.path.join('.','scrapping.log')

def check_folder():
    '''
    Verifica si existe la carpeta en el directorio actual
    '''
    return os.path.isdir(FOLDER)
        

def create_folder():
    '''
    Crea la carpeta donde se almacenarán las imagenes de pokemon.com
    '''
    mkdir = 'md' if sys.platform == 'win32' else 'mkdir'
    subprocess.call([mkdir, 'pokemon_images'])


def download_photos():
    '''
    Esta funcion descarga todas las imagenes desde Pokemon.com
    NOTA: Esta función aún es un WIP, ya que se necesita saber la cantidad exacta de pokemon a descargar
    además no está considerando las formas regionales
    '''    

    if not check_folder():
        create_folder()

    start_time = time.time()

    for i in range(1, 806):
        try:
            req = urllib.request.Request(
                'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(i) + '.png')
            response = urllib.request.urlopen(req)
            rr = response.read()
            ba = bytearray(rr)
            image = np.asarray(ba, dtype="uint8")
            image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
            cv2.imwrite(FOLDER + '{:04d}'.format(i) + ".png", image)
            print("Saved " + '{:04d}'.format(i) + ".png")
            # try:            
            #     print("Buscando formas...")
            #     for j in range(1,10):
            #         requ = urllib.request.Request(
            #         'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(i) + '_f' + j + '.png')
            #         responses = urllib.request.urlopen(requ)
            #         rrr = response.read()
            #         bas = bytearray(rrr)
            #         images = np.asarray(bas, dtype="uint8")
            #         images = cv2.imdecode(images, cv2.IMREAD_UNCHANGED)
            #         cv2.imwrite(FOLDER + '{:04d}'.format(i) + '_f' + j + '.png', image)
            #         print("Saved " + '{:04d}'.format(i) + ".png")
            
            # except Exception as e:
            #     print("No tiene mas formas ",e )
            
        except Exception as e:
            print("Error Occured for Pokemon " + '{:04d}'.format(i))
            print(str(e))
            
    end_time = time.time()
    print("Done")
    print("Time Taken = ", end_time - start_time, "sec")

def download_photo(pnum):
    '''
    Esta funcion descargar la imagen bajo demanda desde Pokemon.com
    '''    

    if not check_folder():
        create_folder()
    
    try:
        req = urllib.request.Request(
            'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(pnum) + '.png')
        response = urllib.request.urlopen(req)
        rr = response.read()
        ba = bytearray(rr)
        image = np.asarray(ba, dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
        cv2.imwrite(FOLDER + '{:04d}'.format(pnum) + ".png", image)
        logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = LOG_FILE,
                    filemode = 'w',)
        logging.info('Imagen del pokémon {} descargada exitosamente'.format(pnum) )
        return True

    except Exception as e:
        logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = LOG_FILE,
                    filemode = 'w',)
        logging.error('Error al intentar descargar la imagen')
        return False
        # print("Error Occured for Pokemon " + '{:04d}'.format(pnum))
        # print(str(e))