import sys
from os import remove

def delete_contact(name):
    f = open(f'/home/mel/.contacts-store/{name}.txt')
    remove(f)
