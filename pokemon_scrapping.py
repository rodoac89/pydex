import cv2
import numpy as np
import urllib.request
import time
import os.path
from pathlib import Path

start_time = time.time()
path_to_image = 'pokemon_images/'
for i in range(1, 806):
    try:
        req = urllib.request.Request(
            'https://assets.pokemon.com/assets/cms2/img/pokedex/detail/' + '{:03d}'.format(i) + '.png')
        response = urllib.request.urlopen(req)
        rr = response.read()
        ba = bytearray(rr)
        image = np.asarray(ba, dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
        cv2.imwrite(path_to_image + '{:04d}'.format(i) + ".png", image)
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
        #         cv2.imwrite(path_to_image + '{:04d}'.format(i) + '_f' + j + '.png', image)
        #         print("Saved " + '{:04d}'.format(i) + ".png")
           
        # except Exception as e:
        #     print("No tiene mas formas ",e )
        
    except Exception as e:
        print("Error Occured for Pokemon " + '{:04d}'.format(i))
        print(str(e))
        
end_time = time.time()
print("Done")
print("Time Taken = ", end_time - start_time, "sec")