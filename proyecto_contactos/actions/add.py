from pathlib import Path
import os
import sys

def creo_contacto(nombre, telf, correo, ciudad, local, nac):
    f = open(f'/home/mel/.contacts-store/{nombre}.txt', 'w+')
    f.write(f'Name: {nombre}\nTelf: {telf}\nEmail: {correo}\nCity: {ciudad}\nLocality: {local}\nDate of Birth: {nac}')
