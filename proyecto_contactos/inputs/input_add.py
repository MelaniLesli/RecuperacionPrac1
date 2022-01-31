from commands.add import creo_contacto
import sys
import os

def input_add():
    print(f'##Add new Contacts: {sys.argv[2]}')
    telf = int(input('Tlf: '))
    correo = str(input('Email: '))
    ciudad = str(input('City: '))
    local = str(input('location: '))
    nac = str(input('Date of birth:'))
    creo_contacto(sys.argv[2], telf, correo, ciudad, local, nac)

