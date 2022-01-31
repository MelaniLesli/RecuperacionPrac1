import sys
from os import remove 
from commands.rm import delete_contact

def rm_contact():
    delete_contact(sys.argv[2])
    print(f'The contacts{sys.argv[2]}, he was removed')
