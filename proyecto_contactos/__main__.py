from actions.add import creo_contacto
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) == 2:
        creo_contacto(sys.argv[1])
