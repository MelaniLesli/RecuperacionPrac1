from actions.add import creo_contacto
from help import show_help
import sys
import os

if __name__ == '__main__':
    if  sys.argv[1] == 'help':
       show_help()
    elif sys.argv[1] == 'add':
       print(f'##Add new Contacts: {sys.argv[2]}')
       telf = int(input('Tlf: '))
       correo = str(input('Email: '))
       ciudad = str(input('City: '))
       local = str(input('location: '))
       nac = str(input('Date of birth:'))
       creo_contacto(sys.argv[2], telf, correo, ciudad, local, nac)
