import os
import sys

def creo_contacto(nombre):
    print(f'##Add new Contacts: {nombre}')
    telf = int(input('Tlf: '))
    correo = str(input('Email: '))
    ciudad = str(input('City: '))
    local = str(input('location: '))
    nac = str(input('Date of birth:'))
